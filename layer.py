from neuron import Neuron


class Layer:
	
	def __init__(self):
		# self.neurons = np.array([None] * neurons_num, dtype=Neuron)
		self.neurons = []
		
	def assign_neuron(self, neuron, index):
		self.neurons[index] = neuron
		
	def append_neuron(self, neuron: Neuron):
		self.neurons.append(neuron)
		
	def remove_neuron(self, index):
		self.neurons.pop(index)
	
	# def activatate_function(self):
	