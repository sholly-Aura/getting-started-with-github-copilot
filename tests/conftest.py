import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_store


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activity data after each test.

    The application uses a module-level `activities` dict, which is mutated
    by signup/unregister operations. Resetting it ensures tests are isolated.
    """

    original = copy.deepcopy(activities_store)
    yield
    activities_store.clear()
    activities_store.update(copy.deepcopy(original))


@pytest.fixture
def client():
    return TestClient(app)
