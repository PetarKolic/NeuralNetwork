import math

def error_calc(result, actual_res):
	return -(actual_res * math.log(result)) - (1- actual_res) * math.log(1 - result)


def activation_function(z):
	return 1 / (1 + math.exp(-z))



# print(activation_function(-0.9768))

print(error_calc(0.005199, 1) + error_calc(0.27352, 0))


# print()