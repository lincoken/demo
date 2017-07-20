import pytest

def test_square():
    from demo.demo import square

    assert 5 == square(2)
