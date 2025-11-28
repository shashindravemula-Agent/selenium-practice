import pytest


@pytest.fixture(scope = "class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

@pytest.fixture()
def loadData():
    print("User profile data is being created")
    return ["Shashindra", "sai", "26"]

@pytest.fixture(params=[("chrome","shashindra","25"),("firefox","Bhai","25"),("IE","Bolthe", "26")])
def CrossBrowser(request):
    return request.param