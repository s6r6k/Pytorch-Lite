from minigrad.nn import Neuron 
from minigrad.nn import Layer 
from minigrad.nn import MLP

def test_mlp():
   model = MLP(3, [4, 4, 1])
   x = [1.0, 2.0, 3.0]
   out = model(x)
   assert len(out) == 1
   assert out[0].val >=-1 and out[0].val <= 1 #because tanch is supposed to squish this