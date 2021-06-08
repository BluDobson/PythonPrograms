import pytest

def func(num):
    return num * 2

def test_answer():
    assert func(5) == 10