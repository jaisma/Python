import os

def getInput():
  numStars = int(raw_input("Enter the amount of stars you want to see"))
  while (numStars < 0):
    numStars = int(raw_input("Enter the amount of stars you want to see."))
  drawStar(numStars)

def drawStar(numStars):
  for i in range(numStars):
    print  ('*' , end = '')

def powerList(startVal, endVal, exponent = 2):
  powList = [i** exponent for i in range(startVal, endVal + 1)]
  return powList
  
def drawHyphens(lista):
  for i in lista:
    for j in range(i):
      print ('-', end = ' ')
    print ("(" + str(i) + ")")

def main():
  getInput()
  print (powerList(3, 7, 3))
  lista = [3, 7, 3]
  drawHyphens(lista)
  os.system("pause")
    
if __name__ == "__main__":
  main()
