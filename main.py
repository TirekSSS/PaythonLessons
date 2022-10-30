def hungry(func):
	def wrapper():
		func()
		print('hungry')
	return wrapper

def stupid(func):
	def wrapper():
		func()
		print('stupid')
	return wrapper

def evil(deco):
	def wrapper():
		deco()
		print('evil')
	return wrapper
  
def poor(func):
	def wrapper():
		func()
		print('poor')
	return wrapper  

def lazy(func):
	def wrapper():
		func()
		print('lazy')
	return wrapper

def unemployed(func):
	def wrapper():
		func()
		print('unemployed')
	return wrapper  

@hungry
@unemployed
@evil
@stupid
@poor
@lazy
def human():
	print('This is human')
human()
