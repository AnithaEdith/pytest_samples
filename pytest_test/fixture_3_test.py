import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    retVal = request.param
    print("\n setup! retval={}".format(retVal))
    return retVal

def test1(setup):
    print("\n setup = {}".format(setup))
    assert True

