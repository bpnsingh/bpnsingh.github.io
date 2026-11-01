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

## Public demo
[`demo/`](demo) is a runnable, self-contained version of the same pattern. It uses no employer code or data.

| Piece | File |
|---|---|
| Stand-in microservice (stdlib HTTP + SQLite, with a switch that simulates API drift) | [`service.py`](demo/service.py) |
| Strict Pydantic response contracts (`extra="forbid"`) | [`contracts.py`](demo/contracts.py) |
| Test-data factory, so tests need no manual setup | [`factory.py`](demo/factory.py) |
| Fixtures and tests, including one proving a renamed field is caught | [`conftest.py`](demo/conftest.py), [`test_contracts.py`](demo/test_contracts.py) |

```bash
cd demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Differences from the original: SQLite instead of PostgreSQL, and one small service instead of 12.

## Status
The original suite was built for an employer, so its source is not public. The demo above is the public version.
