def ask_age():
	num1 = sign = num2 =''
	# sign = ''
	# num2 = ''
	while num1 == '' or sign == '' or num2 == '':
		try:
			num1 = int(input('Input your number 1: '))	
			num2 = int(input('Input your number 2: '))
			sign = input('Input your sign:')
			if sign == '+' or sign == '-' or sign == '*' or sign == '/':
				print(num1,sign,num2)
			else:
				sign = ''
				raise ValueError
		except ValueError:
			print('You need to write normal evaluation')

		if sign == '+':
			print(num1,sign,num2,'=',num1+num2)
    if sign == '*':  
      print(num1,sign,num2,'=',num1*num2)
    if sign == '-': 
      print(num1,sign,num2,'=',num1-num2)
		elif sign == '/':
			try:
				print(num1,sign,num2,'=',num1/num2)
			except:
				print('This is division by zero!!!')
		print('The end of program')
def ask_age2():
	age = ''
	while age =='':
		age = int(input('Input your age: '))
		print('Your age is', age)
	print('The end of program')

ask_age()
def timer(func):
	import time
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		print('Time: ', end-start)
	return wrapper

count = 0
def counter(func):
	def wrapper():
		global count
		count += 1
		func()
		print(func.__name__, 'is called ', count)
	return wrapper

def logging(func):
	def wrapper():
		func()
		print('The function that called is',func.__name__)
	return wrapper

@timer
@counter
@logging
def webpage():
	import requests
	page = requests.get('https://www.random.org')
	# print(page.text)

webpage()