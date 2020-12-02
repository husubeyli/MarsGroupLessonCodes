import pytest
from unittest.mock import Mock

from code import A

@pytest.fixture(scope="module")
def mock_a():
    print('worked')
    return A()