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