keyDict = {' ' : 0,
           'a' : 1,
           'b' : 2,
           'c' : 3,
           'd' : 4,
           'e' : 5,
           'f' : 6,
           'g' : 7,
           'h' : 8,
           'i' : 9,
           'j' : 10,
           'k' : 11,
           'l' : 12,
           'm' : 13,
           'n' : 14,
           'o' : 15,
           'p' : 16,
           'q' : 17,
           'r' : 18,
           's' : 19,
           't' : 20,
           'u' : 21,
           'v' : 22,
           'w' : 23,
           'x' : 24,
           'y' : 25,
           'z' : 26
           }
def cipher( string, keys ):
    newString = ''
    for i in range(len(string)):
        offset = keyDict[keys[(i+1) % len(keys)]]
        order = ord(string[i])
        if order == 32: order = 96
        newOrd = order + offset
        if newOrd > 122: newOrd -= 27
        if newOrd == 96: newOrd = 32
        newString += chr(newOrd)
    return newString

def getString():
    inputString = input("Enter string statement to be encrypted:\n")
    return inputString

def getKey():
    inputKey = input("Enter string key to encrypt:\n")
    return inputKey


def main():
    string = getString()
    key = getKey()
    encrypted = cipher(string, key)
    print("Encrypted message:")
    print (encrypted)

if __name__ == "__main__":
    main()
