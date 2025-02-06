# File that supposed to be in the same foulder as tests
# In this file Pytest will check fixture annotations if it will not find it within the class
# Good practice is to store fixtures here


###############Types of scope fixtures ################

# scope="session"   - will be executed only onse during the whole execution
# scope="module" will run the precondition within the file just one time no matter how many tests are on the page
# scope="function" it would run multiple times for every test we have
# scope="slass" almost the same as module. Will have it within the all tests in class

import pytest


@pytest.fixture(scope="function")
def preSertupWork():
    print("I setup browser instance from conftest file")