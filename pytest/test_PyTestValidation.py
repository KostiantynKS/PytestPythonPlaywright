# Fixtures  (Basically a Hook class like precondition for the every test)
import pytest


@pytest.fixture(scope="module")   # Annotation to set up fixture (precondition)
def preWork():                    # scope="module" will run the precondition just one time no matter how many tests are on the page
    print("I setup browser instance")  # If it would be scope="function" it would run multiple times for every test we have
                                       # Almost the same as scope="slass" is to have it within the all tests in class

@pytest.fixture(scope="function")
def secondWork():
    print("I setup browser instance")
    return "fail"


def test_initialCheck(preWork, secondWork):  # Pytest recognizes the test_ part in the method name, and treat this as a test
    print("This is first test")  # Fixture precondition should be passed as an argument to the test
    assert secondWork == "fail"   # Example of assertions that comparing the value returned by precondition

def test_SecondCheck(preWork):  # Pytest recognizes the test_ part in the method name, and treat this as a test
    print("This is Second test")