import itertools

def testFunction(x):
    return x < 40

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"

def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    with open("textfile.txt.bak", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    for m in range(len(days)):
        print(m+1, days[m])

    for i, m in enumerate(days, start=1):
        print(i, m)

    for m in zip(days, daysFr):
        print(m)

    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")
        
    seq1 = ["Asif", "Atif", "Aqib"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals, max)
    print(list(acc))
        
    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    
    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    

    list1 = [1, 2, 3, 0, 5, 6]
    
    print(any(list1))
    print(all(list1))    
    print("min: ", min(list1))
    print("max: ", max(list1))        
    print("sum: ", sum(list1))
    
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    odds = list(filter(filterFunc, nums))
    print(odds)

    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    squares = list(map(squareFunc, nums))
    print(squares)

    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)
    
    
if __name__ == "__main__":
    main()
