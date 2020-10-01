import pytest

from .payloads import test_tips


@pytest.fixture(scope="module")
def tips():
    return test_tips
