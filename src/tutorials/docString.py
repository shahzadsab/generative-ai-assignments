def myFunction(arg1, arg2=None):
  """myFunction(arg1, arg2=None):
  Doesn't really do anything special.

  Parameters:
  arg1: the first argument. Whatever you feel like passing.
  arg2: the second argument. Defaults to None. Whatever makes you happy.
  """
  print(arg1, arg2)

def myFunction2(arg1, arg2, *, suppressExceptions=False):
  print(arg1, arg2, suppressExceptions)


def main():
  print(myFunction.__doc__)
    
  myFunction2(1, 2, suppressExceptions=True)


if __name__ == "__main__":
    main()
