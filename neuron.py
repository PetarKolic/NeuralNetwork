import math
class Neuron:
	
	def __init__(self, bias=0):
		self.weights = []
		self.dependent_neurons = []
		self.bias = bias

	# @property
	def activate_neuron(self):
		activation_sum = self.bias
		for i in range(min(len(self.weights), len(self.dependent_neurons))):
			activation_sum += self.dependent_neurons[i].activate_neuron() * self.weights[i]
		return Neuron.activation_function(activation_sum)
	
	def assign_neuron(self, neuron, index):
		self.dependent_neurons[index] = neuron
	
	def append_dependent_neuron(self, neuron):
		self.dependent_neurons.append(neuron)
	
	@staticmethod
	def activation_function(z):
		return 1 / (1 + math.exp(-z))
	
	def remove_neuron(self, index):
		self.dependent_neurons.pop(index)
	
	def append_weight(self, weight):
		self.weights.append(weight)
	
	def assign_weight(self, weight, index):
		if index < len(self.weights):
			self.weights[index] = weight