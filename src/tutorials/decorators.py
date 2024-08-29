from functools import wraps

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

print(printfib())


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
print(printfib.__name__)
print(printfib.__doc__)
printfib()

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

print(pfib())

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

pfib()