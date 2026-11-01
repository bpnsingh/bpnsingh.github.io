import pytest
import requests

from factory import DataFactory
from service import Db, Service


@pytest.fixture(scope="session")
def service():
    svc = Service(Db())
    svc.start()
    yield svc
    svc.stop()


@pytest.fixture
def factory(service):
    service.drift = False  # every test starts from the documented contract
    return DataFactory(service.db)


@pytest.fixture
def get(service):
    """Returns a function: get("/users/1") -> requests.Response."""
    return lambda path: requests.get(service.base_url + path, timeout=5)
