import pytest

@pytest.fixture
def data_val():
    return { "Name":"Durga",
            "Age": 30,
            "Salary": 10000,
            "Designation": "SDE",
            "Location": "Hyderabad"}

def test_data(data_val):
    print("----Values from test_data ----")
    print(f"Name: {data_val['Name']}")
    print(f"Age: {data_val['Age']}")
    print(f"Salary: {data_val['Salary']}")
    print(f"Designation: {data_val['Designation']}")
    print(f"Location: {data_val['Location']}")

def my_fun(data_val):
    print("---Values from my_fun---")
    print(f"Name: {data_val['Name']}")
    print(f"Age: {data_val['Age']}")
    print(f"Salary: {data_val['Salary']}")
    print(f"Designation: {data_val['Designation']}")
    print(f"Location: {data_val['Location']}")


def test_my_fun(data_val):
    my_fun(data_val)

# Explanation:
# The my_fun function now accepts data_val as an argument.
# A new test function test_my_fun is added to call my_fun with the data_val fixture.
# This ensures that the fixture is used correctly within the pytest framework.

