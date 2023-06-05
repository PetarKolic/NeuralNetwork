from neuron import Neuron


class FirstLayerNeuron(Neuron):
	
	def __init__(self, value):
		super().__init__(value)
		self.value = value
		
	# @property
	# def activate_neuron(self):
	# 	# return self.bias
	# 	return self.value
	
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

