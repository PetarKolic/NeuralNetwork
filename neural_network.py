import helper_fun as hf
from neuron import Neuron
# from first_layer_neuron import FirstLayerNeuron
# import layer as la
from layer import Layer
from first_layer_neuron import FirstLayerNeuron

import math
import ast

class NeuralNetwork:
	
	@staticmethod
	def error_calc(result, actual_res):
		return -(1 - actual_res) * math.log(result) - actual_res * math.log(1 - result)
	def line_parsing_neuron_layer(self, line, layer):
		
		tmp_weights = hf.find_between(line, "[", "]")
		line = line.partition(tmp_weights)[2]
		tmp_weights = list(map(float, tmp_weights.split(",")))
		neuron = None
		# if len(self.layers) == 1:
		# 	neuron = FirstLayerNeuron(tmp_weights[0])
		# else:
		# 	neuron = Neuron(tmp_weights[0])
		neuron = Neuron(tmp_weights[0])
		for i in range(1, len(tmp_weights)):
			neuron.append_weight(tmp_weights[i])
		
		layer.append_neuron(neuron)
		for i in range(1, len(tmp_weights)):
			# print(i)
			# neuron.append_weight(tmp_weights[i])
			if (len(self.layers) > 1):
				for neuron_dependent in self.layers[-2].neurons:
					neuron.append_dependent_neuron(neuron_dependent)
		return line
	
	def parse_input_output_data_set(self, line):
		
		line = line.replace(" ", "").replace("\t", "").replace("\n", "")
		line = line.split("],[")
		
		input_data_set = ast.literal_eval(line[0] + "]")
		output_data_set = ast.literal_eval("[" + line[1])
		
		self.inputDataSets.append(input_data_set)
		self.outputDataSets.append(output_data_set)
	
	def parse_input_output_data(self, file_input_output_data):
		
		with open(file_input_output_data, 'r') as f:
			line = f.readline()
			
			while line != '':  # line of code
				# layer = Layer()
				# self.layers.append(layer)\
				self.parse_input_output_data_set(line)
				line = f.readline()
	
	def parse_tmp_weights(self, file_tmp_weights):
		with open(file_tmp_weights, 'r') as f:
			# num_input_parameters = int(f.readline())		#number, exception handling missing
			line = f.readline()
			
			# line = f.readline()
			while line != '':  # line of code
				line = line.replace(" ", "").replace("\t", "").replace("\n", "")
				layer = Layer()
				self.layers.append(layer)
				while len(line) > 1:  # maybe 1 is better to be checked
					line = self.line_parsing_neuron_layer(line, layer)
				line = f.readline()
	
	def __init__(self, file_tmp_weights, file_input_output_data):
		
		self.layers = []
		self.inputDataSets = []
		self.outputDataSets = []
		self.flag_first_iteration = True
		self.parse_input_output_data(file_input_output_data)
		
		self.parse_tmp_weights(file_tmp_weights)
	
	def update_second_layer_dependent_neurons(self):
		
		if len(self.layers) >= 2:
			update_layer = self.layers[1]
			for neuron in update_layer.neurons:
				if len(neuron.dependent_neurons) > 0:
					neuron.remove_all_dependant_neurons()
				for dependent_neuron in self.layers[0].neurons:
					neuron.append_dependent_neuron(dependent_neuron)
	
	def check_first_layer_filled(self):
		if len(self.layers) > 0 and len(self.layers[0].neurons) > 0 \
				and isinstance(self.layers[0].neurons[0], FirstLayerNeuron):
			return True
		else:
			return False
	

	def final_error_formula(self,result_list, i, j):
		result = result_list[i][j]
		actual_res = self.outputDataSets[i][j]
		if result <= 0:
			return float('NaN')  # Return NaN for non-positive numbers
		else:
			return self.error_calc(result, actual_res)
	def calculate_error(self, result_list):
		
		total_error = 0
		for i in range(len(result_list)):
			for j in range(len(result_list[i])):
				total_error += self.final_error_formula(result_list, i, j)
		return total_error
	

	def calculate_error_last_layer(self):
		
		# for i  in range(self.outputDataSets):
		for i in range(len(self.layers[-1].neurons)):
			neuron = self.layers[-1].neurons[i]
			error = 0
			for j in range(len(self.outputDataSets)):
				activation = neuron.activate_neuron()
				error += NeuralNetwork.error_calc(activation, self.outputDataSets[j][i])
				neuron.set_error(error)
			
	def calculate_neuron_error_non_last_layer(self, neuron, neuron_index, output_layer):
		error = 0
		forward_neurons = output_layer.neurons
		for i in range(len(output_layer.neurons)):
				prvi_index = forward_neurons[i].weights[neuron_index] * forward_neurons[i].error
				drugi_index = neuron.activate_neuron() * (1 - neuron.activate_neuron())
				error += prvi_index + drugi_index
				
				
		neuron.set_error(error)
	def backward_propagation(self):
		
		self.calculate_error_last_layer()
		# other_layers = self.layers[1:]
		for i in range(len(self.layers) - 2, 0, -1):
			for j in range(len(self.layers[i].neurons)):
				neuron = self.layers[i].neurons[j]
				self.calculate_neuron_error_non_last_layer(neuron, j, self.layers[i+1])
		
	def update_weights(self):
		for layer in self.layers:
			for neuron in layer.neurons:
				for i in range(len(neuron.weights)):
					neuron.update_weights(4, 0.1, 0.1, layer)
					
				
	
	def activate_network(self):
		result_list = []
		# for neuron in self.layers[-1].neurons:
		# 	res = neuron.activation_function2()
		# 	result_list.append(res)
		result_matrix = []
		for input_set in self.inputDataSets:
			
			layer = Layer()
			if self.check_first_layer_filled():
				self.layers[0] = layer
			else:
				self.layers.insert(0, layer)
			
			# self.layers[0] = layer
			
			for input_parameter in input_set:
				n = FirstLayerNeuron(input_parameter)
				layer.append_neuron(n)
			
			self.update_second_layer_dependent_neurons()
			
			
			exit_num = len(self.layers[-1].neurons)
			for i in range(exit_num):
				neuron = self.layers[-1].neurons[i]
				res = neuron.activate_neuron()
				result_list.append(res)
			# print(result_list)
			result_matrix.append(result_list)

			result_list = []
		total_error = self.calculate_error(result_matrix)
		return print(total_error)
