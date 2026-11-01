# Android Performance Logger Daemon

**Stack:** Python, ADB, Asyncio, FastAPI, Grafana · **Context:** Dialpad, 2020–Present

## Problem
Performance regressions on physical Android devices were found late, because nothing monitored CPU, memory, battery and rendering continuously during test runs.

## Approach
- An async Python daemon built on `asyncio` and `subprocess` wrappers around ADB.
- It continuously polls CPU, memory, battery drain and render frame metrics from a device farm.
- Metrics stream to a Grafana time-series dashboard through a Python FastAPI ingest endpoint.

## Outcome
- Real-time performance regression detection during CI runs.
- 15% efficiency improvement on flagship device test runs.

## Related public work
- [Android-App-Profiling](https://github.com/bpnsingh/Android-App-Profiling): an earlier public Android app performance logger.

## Status
**Confidential.** The Dialpad daemon is employer code, so the source and internal details cannot be shared. The description above is limited to what is already on my resume. The repo above is my own public, earlier work on the same idea. Happy to discuss the design in an interview.
