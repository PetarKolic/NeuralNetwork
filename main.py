import numpy as np
#import neural_network as nn
from neural_network import NeuralNetwork



def fun(b):
	b = b + 4

if __name__ == '__main__':
	neural_network = NeuralNetwork("/home/perica/Desktop/neural_network.txt", "/home/perica/Desktop/neural_network_res.txt")
	# aba = " fafaf  ffa faf af affrekrej j      k5erer"
	# aba = aba.replace(" ", "")
	# print(aba)
	# str = "[1,2,3,4],[5,6,7],[8,9,10,11]"
	# str = str.split("],[")
	
	# while len(str) > 1:
	# 	str = str.partition(tmp_weights)[2]
	# 	print(tmp_weights)
	# lista = []
	
	# lista.append(4)
	# lista.append(3)
	# lista.append(7)
	
	# print (lista)
	# a = 5
	# fun(a)
	# print(a)
	list_result = neural_network.activate_network()
	print(list_result)


print("sve ok")