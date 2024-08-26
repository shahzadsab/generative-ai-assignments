from string import Template

def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)

    s2 = b.decode('utf-8')
    print(s+s2)
    
    b2 = s.encode('utf-8')
    print(b+b2)
    
    b3 = s.encode('utf-32')
    print(b3)
    
    str1 = "You're watching {0} by {1}".format("Python", "Shahzad Sab")
    print(str1)
    
    templ = Template("You're watching ${title} by ${author}")
    
    str2 = templ.substitute(title="Python", author="Shahzad Sab")
    print(str2)
    
    data = { 
        "author": "Shahzad Sab",
        "title": "Python"
    }
    str3 = templ.substitute(data)    
    print(str3)    
    
if __name__ == "__main__":
    main()
