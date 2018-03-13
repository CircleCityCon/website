#!/usr/binenv python
# -*- coding: utf-8 -*-
from csv import DictReader
from jinja2 import Template
from BeautifulSoup import BeautifulSoup as soup
import argparse, json, re, os, requests

bios = {}
talks = []
training = []

bio_tmpl = Template(u'''---
title: "{{ bio['full_name']|title }}"
bio_image: "/images/bios/{{ avatar }}"
show_title: true
{% if bio['training']|length > 0 %}
training:
{% for i in bio['training'] %}
   - training/{{ i }}
{% endfor %}
{% endif %}
{% if bio['talks']|length > 0 %}
talks:
{% for i in bio['talks'] %}
  - talks/{{ i }}
{% endfor %}
{% endif %}
---

{{ bio['bio'] }}
''')

training_tmpl = Template(u'''---
title: "{{ training['title'] }}"
trainers:
{% for i in training['speakers'] %}
  - "bios/{{ i }}"
{% endfor %}
{% if training['draft'] %}draft: true{% endif %}
show_title: true
---

{{ training['description'] }}
''')

talk_tmpl = Template(u'''---
title: "{{ talk['title'] }}"
speakers:
{% for i in talk['speakers'] %}
  - "bios/{{ i }}"
{% endfor %}
{% if talk['draft'] %}draft: true{% endif %}
show_title: true
---

{{ talk['description'] }}
''')


def parse_speaker(e, spn):
    '''
    Parse a speaker out of the CSV row
    '''
    full_name = '{} {}'.format(
        e['speaker {}: first_name'.format(spn)],
        e['speaker {}: last_name'.format(spn)])
    if len(full_name) > 3:
        return {
            'full_name': full_name,
            'file': '{}.md'.format(full_name.lower().replace(' ','.')),
            'bio': soup(e['speaker {}: bio'.format(spn)]).text,
            'url': e['speaker {}: url'.format(spn)],
            'twitter': e['speaker {}: twitter_username'.format(spn)],
            'avatar': e['speaker {}: avatar_url'.format(spn)],
            'talks': [],
            'training': [],
        }
    return None

def parse_talk(e, args):
    '''
    Parse a talk dictionary out of the CSV row
    '''
    # The talk dictionary.  Yes, there is a lot of nasty here.
    talk = {
        'title': e['title'],
        'file': '{}.md'.format(re.sub(r'\W+', '', e['title'].replace(' ', '_').lower())),
        'description': soup(e['description']).text,
        'type': json.loads(e['TalkOrTraining'])[0].split()[0].lower(),
        'talk_length': json.loads(e['TalkOrTraining'])[0].split()[1].strip('()').lower(),
        'accepted': True if e['status'] == 'accepted' else False,
        'draft': True if e['flavor'] == 'ad-hoc' else False,
        'speakers': [],
    }

    # As 2 speakers can exist in the current file, iterate over each speaker
    # and then parse out their Bios.  If the speaker doesn't yet exist in the
    # bios dictionary, then we will want to add them in, otherwise just append
    # the talk or training to the bio.
    for spn in [1, 2]:
        speaker = parse_speaker(e, spn)
        if speaker:
            if not speaker['file'] in bios:
                bios[speaker['file']] = speaker
            if talk['type'] == 'talk':
                bios[speaker['file']]['talks'].append(talk['file'])
            if talk['type'] == 'training':
                bios[speaker['file']]['training'].append(talk['file'])
            talk['speakers'].append(speaker['file'])

    if talk['type'] == 'talk':
        talks.append(talk)
    if talk['type'] == 'training':
        training.append(talk)


def parse_file(args):
    # Read through the CSV outout from the CFP system and compile the bio dict,
    # talk list, and training list based on what has been accepted.
    with open(args.file) as csvfile:
        reader = DictReader(csvfile)
        for e in reader:
            if e['status'] == 'accepted':
                parse_talk(e, args)

    # Work through each speaker, pulling together the avatar and the markdown
    # and writing them out to disk.
    for i in bios:
        bio = bios[i]
        resp = requests.get(bio['avatar'], stream=True)
        ifn = '{}.{}'.format(
            bio['full_name'].lower().replace(' ', '.'), 
            resp.headers['Content-Disposition'].split('.')[-1])

        # Stream the Image file into the right location.
        with open(os.path.join(args.path, 'static', 'images', 'bios', ifn), 'wb') as imgfile:
            print('Writing Bio Avatar {}'.format(ifn))
            for chunk in resp.iter_content(1024):
                if chunk:
                    imgfile.write(chunk)

        # Write the markdown file for the Bio.
        with open(os.path.join(args.path, 'content', 'bios', bio['file']), 'wb') as biofile:
            print('Writing Bio {}'.format(bio['file']))
            biofile.write(re.sub(r'\n+', '\n', bio_tmpl.render(bio=bio, avatar=ifn)).encode('utf-8'))

    # For each training item, render the template and write the file to disk
    for i in training:
        with open(os.path.join(args.path, 'content', 'training', i['file']), 'wb') as tfile:
            print('Writing Training {}'.format(i['file']))
            tfile.write(re.sub(r'\n+', '\n', training_tmpl.render(training=i)).encode('utf-8'))

    # For each talk item, render the template and write the file to disk
    for i in talks:
        with open(os.path.join(args.path, 'content', 'talks', i['file']), 'wb') as tfile:
            print('Writing Talk {}'.format(i['file']))
            tfile.write(re.sub(r'\n+', '\n', training_tmpl.render(training=i)).encode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
    A simple utility for parsing the CSV output from the CFP/CFT tooling and
    using the data to generate the Bios, Training, and Talk files.
    ''')
    parser.add_argument('file',
        help='location of the CSV file to parse.')
    parser.add_argument('-p', '--path',
        dest='path',
        default='.',
        help='location of the root folder for the website.')
    parser.add_argument('-f', '--force',
        dest='force',
        action='store_true',
        help='Do we overwrite existing files?')
    args = parser.parse_args()
    parse_file(args)