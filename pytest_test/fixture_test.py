import pytest

@pytest.fixture()
def setup1():
    print("\n setup1")
    yield
    print("\n teardown 1")


@pytest.fixture()
def setup2(request):
    print("\n setup 2")
    def teardowna():
        print("teardowna")

    def teardownb():
        print("teardownb")

    request.addfinalizer(teardowna)
    request.addfinalizer(teardownb)

def test1(setup1):
    print("Executing test1")
    assert True


#@pytest.mark.usefixtures("setup")
def test2(setup2):
    print("Executing test2")
    assert True