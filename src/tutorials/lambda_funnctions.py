def addition(base, *args):
    result = 0
    for arg in args:
        result += arg

    return result
  
def CelsisusToFahrenheit(temp):
  return (temp * 9/5) + 32

def FahrenheitToCelsisus(temp):
  return (temp-32) * 5/9


def main():
  print(addition(5, 10, 15, 20))
  print(addition(1, 2, 3))

  myNums = [5, 10, 15, 20]
  print(addition(*myNums))
  
  ctemps = [0, 12, 34, 100]
  ftemps = [32, 65, 100, 212]

  print(list(map(FahrenheitToCelsisus, ftemps)))
  print(list(map(CelsisusToFahrenheit, ctemps)))

  print(list(map(lambda t: (t-32) * 5/9, ftemps)))
  print(list(map(lambda t: (t * 9/5) + 32, ctemps)))


if __name__ == "__main__":
  main()
