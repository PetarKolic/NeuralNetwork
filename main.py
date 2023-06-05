#import neural_network as nn
from neural_network import NeuralNetwork

if __name__ == '__main__':

	# file_tmp_weights = "C:/Users/icentic/OneDrive - Icentic/Desktop/neural_network.txt"
	# file_input_output_data_set = "C:/Users/icentic/OneDrive - Icentic/Desktop/neural_network_res.txt"

	file_tmp_weights = "/home/perica/Desktop/neural_network.txt"
	file_input_output_data_set = "/home/perica/Desktop/neural_network_res.txt"

	neural_network = NeuralNetwork(file_tmp_weights, file_input_output_data_set)


	for i in range(10000):
		list_result = neural_network.activate_network()
		
		neural_network.backward_propagation()
		
		neural_network.update_weights()