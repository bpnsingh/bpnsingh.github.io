# AI-Powered Log Parsing & RCA Engine

**Stack:** Python, LangChain, Anthropic Claude API, Pytest, GCP · **Context:** Dialpad, 2022–Present

## Problem
Failures in distributed microservice systems leave logs spread across many services, and finding the root cause by hand is slow.

## Approach
A Python-native microservice that:
1. Ingests distributed system logs from GCP log sinks.
2. Chunks and vectorizes them.
3. Submits structured prompts to Claude through the Anthropic API for context-aware root cause analysis.
4. Runs as a post-failure step in GitHub Actions CI and delivers Slack-formatted RCA reports automatically.

## Outcome
- Reduced L1 debugging effort by 40%.
- Introduced predictive defect surfacing into nightly CI runs.

## Status
Built for an employer, so the source is not public. A sanitized public demo (sample logs, no proprietary data) is planned.
