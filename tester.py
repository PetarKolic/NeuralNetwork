import math


def recursion_function(a):
	if a == 0:
		return 1
	else:
		return a * recursion_function(a-1)
	
def activation_function(z):
		return 1 / (1 + math.exp(-z))

a = 1
print(activation_function(a))

def read_properties(file_name):
    properties = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):  # Skip empty and commented lines
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties

# Usage
file_name = 'file.properties'
properties = read_properties(file_name)

# Example: Print all properties
for key, value in properties.items():
    print(f'{key}: {value}')