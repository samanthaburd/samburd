#--print functions--

def say_goodbye(name):
	print("Goodbye," , name)

#--return functions--

def area_circle(radius):
	area = 3.14 * (radius **2)
	print(area)

def subtract(a, b):
	print(a-b)

def multiply(a,b):
	return(a*b)

def divide(a,b):
	return(a/b)

#--conditionals--
def temp_min_max(temps):
	return min(temps),  max(temps)

Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday = [1,2,3,4,5,6,7,]

def is_weekend(day):
	if day >= 6:
		return True
	else:
		return False
def  fuel_efficiency(distance,gallons):
	return(distance/gallons)

def secret_code(number):
	last_digit = number % 10
	start_of_number = number // 10
	num_digits = len(str(start_of_number))
	encrypted =  last_digit * 10**num_digits + start_of_number
	return encrypted 

def evil_oski(x,y):
	result = 1
	for i in range(y):
		result = result * x
	return result

#--min and max w loops--

def min_value(integers):
	smallest = integers[0]
	for i in integers:
		if i < smallest:
			smallest = i
	return smallest

def max_value(integers):
	largest = integers[0]
	for i in integers:
		if i > largest:
			largest = i
	return largest

def maxi_value(integers):
	the_largest = integers[0]
	index = 0
	while index < len(integers):
		if integers[index] > the_largest:
			the_largest = integers[index]
		index = index + 1
	return the_largest

def mini_values(integers):
	the_smallest = integers[0]
	index = 0
	while index < len(integers):
		if integers[index] < the_smallest:
			the_smallest = integers[index]
		index = index +1
	return the_smallest	

def sum_of_digits(number):
	total = 0
	while number > 0:
		last_digit = number % 10
		total = total + last_digit
		number = number // 10
	return total		
		
number = 65428
result = secret_code(number)

print(f"The Result of the Secret Code (5.4) with number = {number} is {result}")