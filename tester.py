def recursion_function(a):
	if a == 0:
		return 1
	else:
		return a * recursion_function(a-1)
	
	
print(recursion_function(5))