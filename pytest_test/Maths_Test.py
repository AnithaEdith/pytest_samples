import pytest
from pytest import approx

def test_IntAssert():
    assert 1 == 1

def test_StrAssert():
    assert "str" == "str"

def test_floatAssert():
    assert 1.0 == 1.0

def test_floatAssert1():
    assert 1.0 + 2.0 == 3.00

def test_floatAssert1():
    assert (0.1 + 0.2) == approx(0.3)

def test_arrayAssert1():
    assert [1,2,3] == [1,2,3]

def test_dictAssert1():
    assert {"1":1} == {"1":1}
