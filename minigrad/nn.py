import random
from minigrad.engine import Value
#cannot from minigrad alone as minigrad is the folder, the package needa import from exact file with value class

class Neuron:
    
    #just initialising the weights of the neurons so we take the number of weights 
    #for the neuron, we dont add the exact weights yet we dk yet.
    def __init__(self, n_inputs: int):
        self.weights = []
        for i in range(n_inputs):
            #weights[i] = random.randint(-1,1) cannot index on an empty list. randint only gives -1 0 1. we want a range
            #weights and biases are not created by any parents they are raw parameters.
            self.weights.append(Value(random.uniform(-1,1)))
        self.bias = Value(random.uniform(-1, 1))
        
    #fully connected does not mean each input connects to eacch weight in neuron
    #fc means each input is connceted to every neuron using one wieght per neuron
    def __call__(self, x_inputs: list):
        zipped = zip(self.weights, x_inputs)
        total = self.bias
        for x, w in zipped:
            total += x*w
        return total.tanh()
    
    def parameters(self):
        #return self.weights.append(self.bias) modfies list in place and returns None
        return self.weights + [self.bias]
    
    
class Layer:
    
    def __init__(self, n_inputs: int, n_neurons: int):
        self.neurons = []
        for i in range(n_neurons):
            self.neurons.append(Neuron(n_inputs))
        
    def __call__(self, x_inputs: list):
        result = []
        #so i have all the inputs and each input will have a neuron weight
        for neuron in self.neurons:
            result.append(neuron(x_inputs))
        return result 
    
    #extend rather than append ensures no nested list but one flatted list
    def parameters(self):
        result = []
        for neuron in self.neurons:
            result.extend(neuron.parameters())
        return result
    
class MLP:
    def __init__(self, n_inputs: int, layer_sizes: list):
        self.layer_list = []
        for layer_sz in layer_sizes:
            self.layer_list.append(Layer(n_inputs, layer_sz))
            n_inputs = layer_sz
        
    def __call__(self, x_inputs):
        for layer in self.layer_list:
            out = layer(x_inputs) 
            x_inputs = out
        return x_inputs
    
    def parameters(self):
        result = []
        for layer in self.layer_list:
            result.extend(layer.parameters())
        return result
            