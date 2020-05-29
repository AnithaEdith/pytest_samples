from pytest import raises

def raisesValueException():
    #raise ValueError
    # pass
   raise UnboundLocalError

def test_exception():
    with raises(UnboundLocalError):
        raisesValueException()