import math

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
        other = other if isinstance(other, Value) else Value(other)
        val = self.val + other.val
        result = Value(val, (self, other))
        
        def _backward():
            self.gradient += result.gradient
            other.gradient += result.gradient
            
        result._backward = _backward #assign the function, NOT CALL IT with ()
        return result
    
    def __radd__(self, other):
        return self + other #this triggers __add__ where Value is the first object 
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        val = self.val * other.val 
        result = Value(val, (self, other))
        
        def _backward():
            self.gradient += other.val * result.gradient
            other.gradient += self.val * result.gradient 
            #+= becasue if both self and other are the same object i do not want to overwrite but accumulate
            
        result._backward = _backward
        return result
    
    def __rmul__(self, other):
        return self * other
        
    #given a Value return a new Value that is just its negative so that i dont need a __subs__ method and 
    #i can just add negative to a number to get subs
    def __neg__(self):
        val = -self.val
        result = Value(val, (self,))
        
        def _backward():
            self.gradient += -1 * result.gradient
        #backward func sets the graident of the parent.
        #what i thought is that self.gradient refers to result.gradient since i called on 
        #result._backward, but thats not true, self refer to whatever was passed in at that tme i defined the method 
        #which is self in the method neg which is the initial parent value.
        result._backward = _backward
        return result
    
    #-(other) calls other.__neg__() which returns a new Value with flipped sign, then self + calls your __add__. Full backward chain included, zero extra code
    def __sub__(self, other):
        return self + -(other)
    
    def __pow__(self, other):
        val = self.val ** other
        result = Value(val, (self,))
        
        #d/dx of x^n = n*(x)^(n-1)
        def _backward():
            self.gradient += result.gradient * other * self.val ** (other -1)
            
        result._backward = _backward
        return result 
        #a^b = c c wrt to a is b* a^b-1
        # c wrt b : 
        
    def __truediv__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return self * other ** -1
    
    #tanh squishes any no. into the range (-1,1). tanh 0 = 0. prevents no.s from exploding.
    #activation functions are needed to prevent the full nn from collapsing into one linear funciton 
    #tanh method lives in Value class bcs any op i wanna do on a number/Value needs to be in Value class la. 
    #output = tanh(w1*x1 + w2*x2)
    #tanh(x) = e^x - e^-x / e^x + e^-x
    #each method needs to have a backward function because it needs to know how much gradient flows back 
    #through this specific op,
    #for add the gradient passes through unchanged
    #mul, gradeitn gets scaled by another operand
    #tanch gradient gets scaled by (1-t^2)
    #val is not automatically a Value object because math.exp is not defined by us and returns a float
    def tanh(self):
        val = (self.exp() - (-self).exp()) / (self.exp() + (-self).exp())
        ##result = Value(val, (self,))
        
        #a ──tanh──► b ──mul──► c ──► loss
        #a.gradient = b.gradient × (1 - val²)
           #= 1.0        × (1 - 0.964²)
           #= 1.0        × (1 - 0.929)
           #= 1.0        × 0.071
           #= 0.071
       ## def _backward():
          ##  self.gradient += result.gradient * (1 - val ** 2)
            
        ##result._backward = _backward
        return val
    
    def exp(self):
        val = math.exp(self.val)
        result = Value(val, (self,))
        
        def _backward():
            self.gradient += result.gradient * val
            
        result._backward = _backward
        return result 
    