class Value:
    def __init__(self, val: float):
        self.val = val
        self.gradient = 0
        self._prev = ()
        self._backward = lambda: None
    
    def __repr__(self):
        return f"Value is {self.val}"