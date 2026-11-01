# Cross-Platform Mobile & Web Automation Framework

**Stack:** Python, Robot Framework, Appium, Selenium, Playwright, Docker · **Context:** Dialpad, 2019–Present

## Problem
Android, iOS and web products each had separate, duplicated test code and a heavy manual regression load every release.

## Approach
- A Python-powered framework with a custom Robot Framework library layer.
- Appium drivers for Android and iOS, Playwright for web.
- Python packaging (`pyproject.toml`) for versioned distribution across teams.
- LLM-assisted test generation and self-healing locators in the Playwright suite.

## Outcome
- Test coverage up 85%.
- 120+ hours of manual regression removed per release cycle.
- Flaky-test triage effort down 30% with self-healing locators.
- The de-facto automation standard for Dialpad QA.

## Related public work
- [VideoCallAutomation](https://github.com/bpnsingh/VideoCallAutomation): a custom automation framework for WhatsApp video calls using the Robot Framework Appium library.
- [AppiumConf-24](https://github.com/bpnsingh/AppiumConf-24): Twilio API integration with Appium for transcription validation.

## Status
The Dialpad framework is employer code and not public. The repos above are public examples of the same approach.
