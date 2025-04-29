import json

import pytest

@pytest.fixture
def sample_fixture(request):
    print(f"---- Running test: {request.node.name}")
    return "Fixture Data"

def test_example(sample_fixture):
    assert sample_fixture == "Fixture Data"

# OP:
# April_26.py::test_example ---- Running test: test_example

# In pytest, request.node.name is an attribute of the request fixture
# that provides the name of the currently executing test function or
# test case. It is useful for dynamically accessing or logging the
# name of the test during runtime.




