from minigrad.engine import Value

def test_value_init():
    val3 = Value(3.0)
    assert val3.val == 3.0 
    assert val3.gradient == 0
    assert val3._prev == set()
    assert callable(val3._backward)