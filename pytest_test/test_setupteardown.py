
def setup_module(module):
    print("Setup module!")

def teardown_module(module):
    print("Teardown module!")


def setup_function(function):
    if function == test1:
        print("\n setting up test1")
    elif function == test2:
        print("\n setting up test2")
    else:
        print("\n setting up unknown test!")

def teardown_function(function):
    if function == test1:
        print("\n Tearing Down test1")
    elif function == test2:
        print("\n Tearing Down test2")
    else:
        print("\n Tearing Down unknown test!")

def test1():
    print("Executing test1")
    assert True


def test2():
    print("Executing test2")
    assert True
