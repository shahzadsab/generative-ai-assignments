from functools import wraps, update_wrapper, lru_cache
from time import perf_counter

def bold(func):
    '''Bold decorator'''
    @wraps(func)
    def wrapper():
        '''return html bold tags'''
        result = '<b>' + func() + '</b>'
        return result
    return wrapper

def italics(func):
    '''Italics decorator'''
    @wraps(func)
    def wrapper():
        '''return html italics tags'''
        result = '<i>' + func() + '</i>'
        return result
    return wrapper

@bold
@italics
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'

# print(printfib())


def make_posh(func):
  '''This is the function decorator'''
  @wraps(func)
  def wrapper():
    '''This is the wrapper function'''
    print("+---------+")
    print("|         |")
    result = func()
    print(result)
    print("|         |")
    print("+=========+")
    return result
  #wrapper.__name__ = func.__name__
  #wrapper.__doc__ = func.__doc__
  return wrapper

@make_posh
def printfib():
  '''Print out Fibonacci'''
  return ' Fibonacci '
# print(printfib.__name__)
# print(printfib.__doc__)
# printfib()

def my_decorator(func):
  '''Decorator function'''
  def wrapper(): 
    '''Return string F-I-B-O-N-A-C-C-I'''
    return 'F-I-B-O-N-A-C-C-I'
  return wrapper

@my_decorator
def pfib():
  '''Return Fibonacci'''
  return 'Fibonacci'

# print(pfib())

def make_posh(func):
  def wrapper():
    print('+---------+')
    print('|         |')
    result = func()
    print(result)
    print('|         |')
    print('+=========+')
    return result
  return wrapper
 
@make_posh
def pfib():
  '''Print out Fibonacci'''
  return ' Fibonacci '

# pfib()

'''
Fixed arguments
'''
def print_fib(a, b, c):
    print(a, b, c)

# print_fib(1, 1, 2)

# print_fib(1, 1, 2, 3)

'''
Using *args
'''
def print_fib(a, *args):
    print(a)
    print(args)

# print_fib(1, 1, 2, 3)

# print_fib(1)

'''
Using **kwargs
'''
def print_fib(a, **kwargs):
    print(a)
    print(kwargs)

# print_fib(1, se=1, th=2, fo=3, fi=5)

# print_fib(1)

'''
Using *args and **kwargs
'''
def print_fib(*args, **kwargs):
    print(args)
    print(kwargs)

# print_fib(1, 1, 2, 3)

# print_fib(fi=1, se=1, th=2, fo=3)

# print_fib(1, 1, 2, fo=3, fi=5)

# print_fib()


def print_fib(*args, **kwargs):
    print(args)
    print(kwargs)

def wrapper(*args, **kwargs):
    print('In wrapper ... unpacking args')
    print(*args)
    print_fib(*args, **kwargs)

# wrapper(1, 1, th=2)



def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}s')
        return result
    return wrapper

@timer
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# fib(20)

class Count:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        print(f'Current count: {self.cnt}')
        result = self.func(*args, **kwargs)
        return result

@Count
def fib(n):
    ''' return the Fibonacci sequence '''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# fib(10)

def timer(func):
    total = 0 # scope: timer()
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        total += duration #scope : wrapper()
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}')
        print(f'Total duration: {total:.8f}')
        return result
    return wrapper

def fib_cache(n):
    '''Return the nth value from the Fiboanacci sequence'''
    mem = {0:0, 1:1}

    if n not in mem:
        mem[n] = fib_cache(n-1) + fib_cache(n-2)
    return mem[n]



@lru_cache(maxsize=None)
@timer
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(18)