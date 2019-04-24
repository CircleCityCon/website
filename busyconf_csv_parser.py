#!/usr/bin/env python
# -*- coding: utf-8 -*-
from csv import DictReader
from jinja2 import Template
from bs4 import BeautifulSoup as soup
import click, json, re, os, requests

def fix_string(obj):
    return obj.replace('Äú', '"').replace('Äô', '\'')

class Speaker:
    def __init__(self, row, speaker_number=1, url_path='bios'):
        n = speaker_number
        self.first_name = row.get('speaker {}: first_name'.format(n))
        self.last_name = row.get('speaker {}: last_name'.format(n))
        self.bio = soup(row.get(
            'speaker {}: bio'.format(n)), features='html.parser').text
        self.site = row.get('speaker {}: url'.format(n))
        self.twitter = row.get('speaker {}: twitter_username'.format(n))
        self.avatar = row.get('speaker {}: avatar_url'.format(n))
        self.talks = []
        self._bio_path = url_path

    def __eq__(self, other):
        return self.full_name == other.full_name

    @property
    def full_name(self):
        '''
        Returns the full name of the speaker.
        '''
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def url(self):
        '''
        Returns the computed URL for the speaker
        '''
        return '/{}/{}'.format(
            self._bio_path,
            self.full_name.lower().replace(' ','_'))

    @property
    def filename(self):
        '''
        Returns the computed filename for the markdown file.
        '''
        return '{}.md'.format(re.sub(r'[^A-Za-z0-9\_]+', '',
            self.full_name.lower().replace(' ','_')))

    @property
    def avatar_filename(self):
        '''
        Returns the computed filename for the markdown file.
        '''
        return '{}.jpg'.format(re.sub(r'[^A-Za-z0-9\_]+', '',
            self.full_name.lower().replace(' ','_')))

    def get_avatar(self, fobj):
        '''
        Downloads the avatar image and stores the file in the file-object
        specified.
        '''
        resp = requests.get(self.avatar, stream=True)
        for chunk in resp.iter_content(1024):
            if chunk:
                fobj.write(chunk)

    @property
    def markdown(self):
        '''
        Returns the markdown for the bio file
        '''
        return Template('\n'.join([
            '---',
            'title: "{{ speaker.full_name|title }}"',
            'bio_image: "/img/bios/{{ speaker.avatar_filename }}"',
            'banner: "/img/bios/{{ speaker.avatar_filename }}"',
            '---\n\n{{ speaker.bio }}',
            '{% for talk in speaker.talks %}',
            '{% if talk.accepted %}'
            '* **{{ talk.type }}** [{{ talk.title }}]({{ talk.url }})',
            '{% endif %}{% endfor %}',
        ])).render(speaker=self)


class Talk:
    def __init__(self, row):
        self.title = fix_string(row.get('title'))
        self.description = soup(
            fix_string(row.get('description')), features='html.parser').text
        self.accepted = True if row.get('status') == 'accepted' else False
        self.speakers = []

        # Determine if this is a talk or training.
        if 'training' in row.get('track').lower():
            self.type = 'training'
        else:
            self.type = 'talk'

    def __eq__(self, other):
        return self.title == other.title

    @property
    def filename(self):
        '''
        Returns the computed filename for the markdown file.
        '''
        return '{}.md'.format(re.sub(r'[^A-Za-z0-9\_]+', '',
            self.title.lower().replace(' ','_')))

    @property
    def url(self):
        '''
        Returns the computed URL for the talk
        '''
        return '/{}/{}'.format(
            'talks' if self.type.lower() == 'talk' else self.type.lower(),
            re.sub(r'[^A-Za-z0-9\_]+', '', self.title.lower().replace(' ','_')))

    @property
    def markdown(self):
        '''
        Returns the markdown for the bio file
        '''
        return Template('\n'.join([
            '---',
            'title: "{{ talk.title }}"',
            '{% if not talk.accepted %}draft: true{% endif %}',
            '---\n\n{{ talk.description }}',
            '{% for speaker in talk.speakers %}',
            '* **SPEAKER** [{{ speaker.full_name }}]({{ speaker.url }})',
            '{% endfor %}',
        ])).render(talk=self)


@click.command()
@click.option('--report', '-r', 'reports', type=click.File(), multiple=True,
    prompt='Report CSV File', help='The CSV report to process')
@click.option('--avatars-path', '-a', type=click.Path(exists=True),
    default='static/img/bios',
    help='Path to where speaker avatars should be downloaded')
@click.option('--bios-path', '-b', type=click.Path(exists=True),
    default='content/bios',
    help='Path to where Speaker Bio files should be generated')
@click.option('--talks-path', '-t', type=click.Path(exists=True),
    default='content/talks',
    help='Path to where Talk description files should be generated')
@click.option('--workshops-path', '-w', type=click.Path(exists=True),
    default='content/training',
    help='Path to where Workshop description files should be generated')
@click.option('--overwrite', '-o', is_flag=True,
    help='Overwrite existing files?')
def process(reports, overwrite, avatars_path, bios_path, talks_path,
            workshops_path):
    '''
    Process the BusyConf report file into the speaker, talk, and training
    markdown files.
    '''
    speakers = list()
    talks = list()

    # We need to derrive the speaker numbers from the fieldnames  To do so we
    # will pull the numbers out from the fieldnames and store them as a set.
    speaker_ids = set()
    for report in reports:
        csvfile = DictReader(report)
        for fieldname in csvfile.fieldnames:
            res = re.findall(r'speaker (\d+)\:', fieldname)
            if res:
                speaker_ids.add(res[0])

        # now to build the model
        for row in csvfile:
            talk = Talk(row)
            for id in speaker_ids:
                speaker = Speaker(row, id)
                if speaker.first_name and speaker.last_name:
                    if speaker not in speakers:
                        speakers.append(speaker)
                    speakers[speakers.index(speaker)].talks.append(talk)
                    talk.speakers.append(speaker)
            talks.append(talk)

    # finally to write out the files.
    for speaker in speakers:
        biofile = os.path.join(bios_path, speaker.filename)
        avatarfile = os.path.join(avatars_path, speaker.avatar_filename)
        print('Writing Bio {}'.format(biofile))
        with open(biofile, 'w') as bio:
            try:
                bio.write(speaker.markdown)
            except Exception as err:
                print('Error Writing Bio: {} -- {}'.format(bio.filename, err))

        if not os.path.exists(avatarfile) or overwrite:
            print('Writing Avatar image {}'.format(avatarfile))
            with open(avatarfile, 'wb') as avatar:
                speaker.get_avatar(avatar)

    for talk in talks:
        ipath = {'talk': talks_path, 'training': workshops_path}
        talkfile = os.path.join(ipath[talk.type], talk.filename)
        print('Writing Talk {}'.format(talkfile))
        with open(talkfile, 'w') as tobj:
            try:
                tobj.write(talk.markdown)
            except Exception as err:
                print('Error Writing {}: {} -- {}'.format(
                    talk.talk_type, talk.filename, err))



if __name__ == '__main__':
    process()