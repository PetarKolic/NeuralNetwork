#import neural_network as nn
import sys

from neural_network import NeuralNetwork
import configparser

if __name__ == '__main__':

	# file_tmp_weights = "C:/Users/icentic/OneDrive - Icentic/Desktop/neural_network.txt"
	# file_input_output_data_set = "C:/Users/icentic/OneDrive - Icentic/Desktop/neural_network_res.txt"

	# file_tmp_weights = "/home/perica/Desktop/neural_network.txt"
	# file_input_output_data_set = "/home/perica/Desktop/neural_network_res.txt"

	file_config_path = "./config/properties.ini"

	config = configparser.ConfigParser()
	config.read(file_config_path)

	file_tmp_weights = config["file_locations"]["file_tmp_weights"]
	file_input_output_data_set = config["file_locations"]["file_input_output_data_set"]

	neural_network = NeuralNetwork(file_tmp_weights, file_input_output_data_set)


	# for i in range(10000):
	# 	list_result = neural_network.activate_network()
	#
	# 	neural_network.backward_propagation()
	#
	# 	neural_network.update_weights()

	# list_result = neural_network.activate_network()

	# for i in range(1000):
	# 	list_result = neural_network.activate_network()
	# 	neural_network.backward_propagation()
	# 	neural_network.update_weights()
	
	for i in range(100):
		neural_network.activate_network()
		neural_network.backward_propagation()
		neural_network.update_weights()

	print("sve ok")