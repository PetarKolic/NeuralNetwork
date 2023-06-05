import math


class Neuron:
	
	def __init__(self, bias=0):
		self.weights = []
		self.dependent_neurons = []
		self.bias = bias
		# self.activation = 0
		self.error = 0
		self.delta = 0
	
	# @property
	def activate_neuron(self):
		activation_sum = self.bias
		for i in range(min(len(self.weights), len(self.dependent_neurons))):
			
			activation_neuron = 0
			
			neuron = self.dependent_neurons[i]
			if (isinstance(self.dependent_neurons[i], Neuron)):
				activation_neuron = neuron.activate_neuron()
			activation_sum += activation_neuron * self.weights[i]
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
	
	def set_error(self, error):
		self.error = error
	
	def get_error(self):
		return self.error
	
	def assign_weight(self, weight, index):
		if index < len(self.weights):
			self.weights[index] = weight
	
	def remove_all_dependant_neurons(self):
		self.dependent_neurons = []
	
	def update_weights(self, m, lambda_const, gradient_const, layer):
		
		for neuron in layer.neurons:
			self.update_delta(neuron.activate_neuron())
		
		for i in range(len(self.weights)):
			dD = 1 / m * self.delta + lambda_const * self.weights[i]
			self.weights[i] -= dD * gradient_const
	
	def update_delta(self, activation_value):
		self.delta += activation_value * self.error

# write me a method which returns hello world as a result
# def activation_function(self):
# 	return "Hello world"

# write me a quicksort algorithm
# def quicksort(array):
