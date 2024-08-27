import string
import collections
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

def main():
  # 01 namedTuple Tutorial
  Point = collections.namedtuple("Point", "x y")
  p1 = Point(10, 20)
  p2 = Point(30, 40)

  print(p1, p2)
  print(p1.x, p1.y)

  p1 = p1._replace(x=100)# use _replace to create a new instance
  print(p1)

  # 02 defaultdict Collection Tutorial
  fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

  fruitCounter = defaultdict(int)
  for fruit in fruits:
    fruitCounter[fruit] += 1

  for (k, v) in fruitCounter.items():
    print(k + ": " + str(v))
  
  # 03 Counter Collection Tutorial
  class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah", "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]
  class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank", "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

  c1 = Counter(class1)
  c2 = Counter(class2)

  print(c1["James"])
  print(sum(c1.values()), "students in class 1")

  c1.update(class2)
  print(sum(c1.values()), "students in class 1 and 2")

  print(c1.most_common(3))
  c1.subtract(class2)
  print(c1.most_common(1))

  print(c1 & c2)

  # 04 orderdict Tutorial
  sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]
    
  sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

  teams = OrderedDict(sortedTeams)
  print(teams)

  tm, wl = teams.popitem(False)
  print("Top team: ", tm, wl)

  for i, team in enumerate(teams, start=1):
    print(i, team)
    if i == 4:
      break

  a = OrderedDict({"a": 1, "b": 2, "c": 3})
  b = OrderedDict({"a": 1, "c": 3, "b": 2})
  print("Equality test: ", a == b)

  # 05 deque Tutorial
  d = collections.deque(string.ascii_lowercase)
  print("Item count: " + str(len(d)))

  for elem in d:
    print(elem.upper(), end=",")

  d.pop()
  d.popleft()
  d.append(2)
  d.appendleft(1)
  print(d)

  print(d)
  d.rotate(1)
  print(d)

if __name__ == "__main__":
    main()
