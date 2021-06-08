import pytest
from Programs import double

def test_answer():
    assert double.func(5) == 10