from pythonisms import __version__
from pythonisms.pythonisms import *


def test_version():
    assert __version__ == '0.1.0'

def test_factors_1():
    actual = factors_one(300)
    expected = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20,25,30,50,60,75,100,150,300]
    assert actual == expected