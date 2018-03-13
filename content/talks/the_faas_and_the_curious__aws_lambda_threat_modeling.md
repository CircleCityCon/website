---
title: "The FaaS and the Curious - AWS Lambda Threat Modeling"
trainers:
  - "bios/bryan.mcaninch.md"
---
Function as a Service (FaaS) platforms facilitate application deployment and event-driven execution with minimal cloud infrastructure and operational overhead. Consequently, the FaaS market is forecasted to grow 33% with an estimated valuation of $7.75B USD by 2021. However, every benefit has a cost and FaaS is no exception. Despite Amazonâ&euro;&trade;s diligent efforts to secure their Lambda FaaS platform, its intended ability to access a variety of resources and services can be abused for unintended results. This presentation explores the attack surface of the AWS Lambda FaaS platform and how it can be surreptitiously used to circumvent security controls. Specifically, it will demonstrate how to hijack and impersonate Lambda functions, gain persistent remote access to the AWS cloud environment, and reverse engineer the Lambda runtime environment itself.