import helper_fun as hf
from neuron import Neuron
# from first_layer_neuron import FirstLayerNeuron
# import layer as la
from layer import Layer


class NeuralNetwork:
	
	def line_parsing_neuron_layer(self, line, layer):
		tmp_weights = hf.find_between(line, "[", "]")
		line = line.partition(tmp_weights)[2]
		tmp_weights = list(map(float, tmp_weights.split(",")))
		neuron = Neuron(tmp_weights[0])
		layer.append_neuron(neuron)
		for i in range(1, len(tmp_weights)):
			# print(i)
			neuron.append_weight(tmp_weights[i])
		if len(self.layers) > 1:
			for neuron_dependent in self.layers[-2].neurons:
				neuron.append_dependent_neuron(neuron_dependent)
		return line
	
	def parse_file_tmp_weights(self, file_tmp_weights):
		with open(file_tmp_weights, 'r') as f:
			# num_input_parameters = int(f.readline())		#number, exception handling missing
			line = f.readline()
			
			while line != '':  # line of code
				line = line.replace(" ", "").replace("\t", "").replace("\n", "")
				layer = Layer()
				self.layers.append(layer)
				while len(line) > 1:  # maybe 1 is better to be checked
					line = self.line_parsing_neuron_layer(line, layer)
				line = f.readline()
	def __init__(self, file_tmp_weights, file_tmp_test_data):
		
		self.layers = []
		self.parse_file_tmp_weights(file_tmp_weights)
	
	# print(self.layers)
	
	def activate_network(self):
		result_list = []
		# for neuron in self.layers[-1].neurons:
		# 	res = neuron.activation_function2()
		# 	result_list.append(res)
		for i in range(len(self.layers[-1].neurons)):
			neuron = self.layers[-1].neurons[i]
			res = neuron.activate_neuron()
			result_list.append(res)
		return result_list