import pytest

def test_square():
    from demo.demo import square

    assert 4 == square(2)
