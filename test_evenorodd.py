from evenorodd import evenorodd

def test_even_number():
    assert evenorodd(10) == "Even"

def test_odd_number():
    assert evenorodd(7) == "Odd"
