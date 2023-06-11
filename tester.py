import math

def error_calc(result, actual_res):
	return -(actual_res * math.log(result)) - (1 - actual_res) * math.log(1 - result)
def activation_function(z):
	return 1 / (1 + math.exp(-z))



# print(activation_function(-4.8408 ))

print(error_calc(0.34746, 0) + error_calc(0.3255, 1) +  error_calc(0.00519, 1) + error_calc(0.007838798698541058, 0))


# print()

# resenje
# 6.816325243195173


# 1.54935 + 4.853873198418815 = 6,403223198333