class Value:
    def __init__(self, val: float, children: tuple = ()):
        self.val = val
        self.gradient = 0
        self._prev = set(children) #parents
        self._backward = lambda: None
    #c = a + b
    #from c's perspective, its parents are a and b, 
    #basically the child nodes from which c was built. 
    #the values that were used to produce me!
    
    def __repr__(self):
        return f"Value is {self.val}"
    
    def __add__(self, other):
        val = self.val + other.val
        result = Value(val, (self, other))
        
        def _backward():
            self.gradient += result.gradient
            other.gradient += result.gradient
            
        result._backward = _backward #assign the function, NOT CALL IT with ()
        return result
    
    def __mul__(self, other):
        val = self.val * other.val 
        result = Value(val, (self, other))
        
        def _backward():
            self.gradient += other.val * result.gradient
            other.gradient += self.val * result.gradient 
            #+= becasue if both self and other are the same object i do not want to overwrite but accumulate
            
        result._backward = _backward
        return result
