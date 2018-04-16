# 1.	Write a Python program to find those numbers which are divisible by 7 and 
# multiple of 5, between 1500 and 2700 (both included). 

for value in range(1500,2701):
	if (value % 7 == 0) and (value % 5 == 0):
		print("The numbers divisible by 7 and multiples of 5 are:",value)


# 2.Write a Python program to get the Fibonacci series between 0 to 50. 

value = 0
sum = 1
while(sum<50):
	print(sum)
	value,sum = sum,value+sum

#3. task to print 1-50 integers, where multiples of 3 as fizz and multiples of 5 as buzz,
# multiples of 3 & 5 as fizzbuzz except are as same

for val in range(1,51):
	if (val%3==0) and (val%5==0):
		val = "Fizzbuzz"
		print(val)
	elif val%3==0:
		val = "fizz"
		print(val)
	elif val%5==0:
		val = "buzz"
		print(val)
	else:
		val = val
		print(val)

# 4.	What will be the output for the follwing code?
x = 'abcd'
for i in range(len(x)):
    x = 'a'
    print(x)

# 5.Write a Python program to convert temperatures to and from celcius, fahrenheit 
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 

temp_in_cel = 30
temp_in_fah = (9/5)*temp_in_cel+32
print(temp_in_cel,"celsius is",temp_in_fah,"fahrenheit")

temp_in_fah = 86
temp_in_cel = ((temp_in_fah-32)/9)*5
print(temp_in_fah,"fahrenheit is",temp_in_cel,"celsius")

# 6.	Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output : 
# Number of odd numbers : 5
# Number of even numbers : 4

odd_count = 0
even_count = 0
numbers = (1,2,3,4,5,6,7,8,9)
for val in numbers:
	if val % 2 != 0:
		odd_count = odd_count + 1
	if val % 2 == 0:
		even_count = even_count + 1
print("Number of Odd Numbers:",odd_count)
print("Number of Even Numbers:",even_count)
