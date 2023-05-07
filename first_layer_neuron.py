from neuron import Neuron


class FirstLayerNeuron(Neuron):
	
	def __init__(self, bias):
		super().__init__(bias)
		
	@property
	def activation_function2(self):
		# return self.bias
		return self.bias
	
	def assign_neuron(self, neuron, index):
		pass
	
	def append_dependent_neuron(self, neuron):
		pass
	
	def remove_neuron(self, index):
		pass
	
	def append_weight(self, weight):
		pass
	
	def assign_weight(self, weight, index):
		pass
	
	def set_bias(self, bias):
		self.bias = bias

