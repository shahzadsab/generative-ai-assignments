from enum import Enum, unique, auto

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "Car at ", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 2
        else:
            self.wheels = 3
        self.doors = 0
        self.engine = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "motorcylce at ", self.speed)

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

class Person():
    def __init__(self):
        self.fname = "Shahzad Alam"
        self.lname = " Bhatti"
        self.age = 43

    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age{2}>".format(self.fname, self.lname, self.age)

    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))

class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):    # use getattr to dynamically return a value
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    def __setattr__(self, attr, val):    # use setattr to dynamically return a value
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    def __dir__(self):    # use dir to list the available properties
        return ("rgbolor", "hexcolor")

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level

def main():
    
    car1 = Car("gas")
    car2 = Car("electric")
    mc1 = Motorcycle("gas", True)

    print(mc1.wheels)
    print(car1.engine)
    print(car2.doors)

    car1.drive(30)
    car2.drive(40)
    mc1.drive(50)
    
    # enumeration class Tutorials
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    print(Fruit.APPLE.name, Fruit.APPLE.value)
    print(Fruit.PEAR.value)
    myFruits = {}
    myFruits[Fruit.BANANA] = "This is a test String"
    print(myFruits[Fruit.BANANA])

    # Class convert into str Tutorial    
    cls1 = Person()
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))
    print(bytes(cls1))

    # Computed Attribute Tutorial
    cls1 = myColor()
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    print(cls1.red)
    print(dir(cls1))
    
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    p3 = p1 + p2
    print(p3)

    p4 = p2 - p1
    print(p4)

    p1 += p2
    print(p1)
    
    #class comparision Tutotial
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))

    # Who's more senior?
    print(bool(dept[0] > dept[2]))
    print(bool(dept[4] < dept[3]))

    # sort the items
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)


if __name__ == "__main__":
    main()


