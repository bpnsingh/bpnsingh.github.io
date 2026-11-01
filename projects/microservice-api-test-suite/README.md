# Python Microservice API Test Suite

**Stack:** Python, Pytest, Pydantic, Requests, PostgreSQL · **Context:** Theatro, 2016–2019

## Problem
Regression testing across a set of REST microservices depended on manual test-data setup and had no contract checks.

## Approach
- A data-driven pytest harness for the REST microservices.
- Pydantic-based contract validation of responses.
- Parameterized fixture pipelines.
- A PostgreSQL-backed test-data factory.

## Outcome
- Contract regression testing across 12 backend services.
- Zero manual data setup.

## Status
Built for an employer, so the source is not public. A small public demo of the same pattern (pytest + Pydantic contracts + a data factory) is planned.
