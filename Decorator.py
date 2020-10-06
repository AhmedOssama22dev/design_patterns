'''
This is an implementation of the decorator design-pattern
Consists of:
	1]Decorating function that is used to decorate any method.
Sample used:
  -Decorating a function by increasing the returned number (n) by +10
'''
from functools import wraps
#1:
def decorator(f):
	@wraps(f)    #To retain the __name__ and __doc__ attributes of the func
	def wrap_f(*args, **kwargs):
		res=f(*args, **kwargs)
    #Decoration code here
		print(f'Decoration is done!\nDecoration:The number after increment by +10 = {n+10} ')
		return res
	return wrap_f

@decorator
def number(n):
	print(f'The number before decoration is = {n}')
	return n
n=90
number(n)
