import math #imports math library

def notUsingIF():
    #takes two characters and prints them in pairs
    #with 12 pairs (24 characters) per line
    #assume users are all smart and enter only one character
    a = input("First Character: ")
    b = input("Second Character: ")
    c = abs(ord(a.upper()) - ord(b.upper()))    #checks for num val of char and its difference
    d = math.floor(c/12)    #rounding down to nearest int
    e = math.floor(c/24)
    f = c%12
    print(((a+b)* round(d * 12))[:24])
    print((a+b) * round(e * 12))
    print((a+b) * f)
    return None

def usingIF():
    #assume users are all fucking smart and only enter one character
    a = input("First Character: ")
    b = input("Second Character: ")
    c = abs(ord(a.upper()) - ord(b.upper()))
    if ((c > 12) & (c < 24)):
        temp = c - 12
        print((a+b) * 12)
        print((a+b) * temp)
    elif (c > 24):
        temp = c - 24
        print((a+b) * 12)
        print((a+b) * 12)
        print((a+b) * temp)
    elif (c == 24):
        print((a+b) * 12)
        print((a+b) * 12)
    else:
        print((a+b) * c)
    return None

    
notUsingIF()
usingIF()

