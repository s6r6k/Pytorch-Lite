from minigrad.engine import Value

def test_value_init():
    val3 = Value(3.0)
    assert val3.val == 3.0 
    assert val3.gradient == 0
    assert val3._prev == set()
    assert callable(val3._backward)
    
def test_add_init():
    a = Value(3)
    b = Value(2)
    add3_2 = a + b
    
    assert add3_2.val == 5
    assert a in add3_2._prev
    assert b in add3_2._prev
    
def test_mul_init():
    a = Value(6)
    b = Value(6)
    mul6_6 = a * b
    
    assert mul6_6.val == 36
    assert a in mul6_6._prev
    assert b in mul6_6._prev
    
def test_radd_init():
    result = Value(3) + 2
    assert result.val == 5
   # assert Value(5) == Value(3) + 2 , does not work as we have not define __eq__ so checks ref equality
   
def test_rmul_init():
    result = Value(3) * 2
    assert result.val == 6
    
def test_neg_init():
    result = -Value(3)
    assert -3 == result.val
    
def test_sub_init():
    result = Value(3) - Value(2)
    assert result.val == 1
    
def test_pow_init():
    result = Value(3) ** 2
    assert result.val == 9
    
def test_truediv_init1():
    result = Value(3) / 1
    assert result.val == 3
    
def test_truediv_ini2t():
    result = Value(3) / Value(1)
    assert result.val == 3
