import pytest

def test_square_2():
    from demo.demo import square

    assert 4 == square(2)

    
def test_square_negitive():
    from demo.demo import square

    assert 4 == square(-2)

    
def test_square_decimal():
    from demo.demo import square

    assert 6.25 == square(2.5)
 #change
