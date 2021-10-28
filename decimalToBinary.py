def decimalToBinary(n):

	if(n > 1):
		# divide with integral result
		# (discard remainder)
		decimalToBinary(n//2)

	print(n%2, end=' ')

# Take number input	
number_to_convert = input()
converted_number = int(number_to_convert) # Convert from string to int

# Driver Code
if __name__ == '__main__':
	decimalToBinary(converted_number)