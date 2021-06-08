import pytest
from Test_Programs import vowels

def test_hi():
    assert vowels.vowels("hi") == 1

def test_specfication():
    assert vowels.vowels("specification") == 6