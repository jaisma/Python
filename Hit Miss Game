import random

def getHouseNumbers():
    hleft = 0
    hmid = 0
    hright = 0
    while ((hleft == hmid) | (hleft == hright) | (hmid == hright)):
        hleft = random.randint(0,9)
        hmid = random.randint(0,9)
        hright = random.randint(0,9)
    return hleft, hmid, hright

def getPlayerNumbers():
    pleft = int (raw_input("Enter digit for left position: "))
    while ((pleft >= 10) | (pleft < 0)):
        print("Invalid Left Entry")
        pleft = int (raw_input("Enter digit for left position: "))
    pmid = int (raw_input("Enter digit for middle position: "))
    while (((pmid  > 9) | (pmid  < 0)) | (pmid == pleft)):
        print("Invalid Mid Entry")
        pmid = int (raw_input("Enter digit for middle position: "))
    pright = int (raw_input("Enter digit for right position: "))
    while (((pright > 9) | (pright < 0)) | ((pright == pleft) | (pright ==pmid))):
        print("Invalid Right Entry")
        pright = int (raw_input("Enter digit for right position: "))
    return pleft, pmid, pright

def checkMatches(a,b,c,d,e,f):
    mcount = 0
    if ((d == b) | (d == c)):
        mcount += 1
    if ((e == a) | (e == c)):
        mcount += 1
    if ((f == a) | (f == b)):
        mcount += 1
    return mcount

def checkHits(a,b,c,d,e,f):
    hcount = 0
    if (d == a):
        hcount += 1
    if (e == b):
        hcount += 1
    if (f == c):
        hcount += 1
    return hcount

def playOneHitAndMatchGame():
    raw_input("Welcome to the Hit && Match Game\nhit any key to start playing...\n")
    a,b,c = getHouseNumbers()
    #print(a, b, c)
    d,e,f = getPlayerNumbers()
    rando0 = checkMatches(a,b,c,d,e,f)
    rando1 = checkHits(a,b,c,d,e,f)

    matchPoint = 0
    matchPoint += int(rando0)
    matchPoint += int(rando1 * 2)
    
    print("%i hit(s)!\n%i match(es)!" %(rando1, rando0))
    print("Come back and play again sometime\n")
    return matchPoint

def main():
    matchPoint = 0
    roundnum = 0
    print 'hit = 2 points; match = 1 point\n'
    while (True):
        roundnum += 1
        print 'Round: ', roundnum
        x = 0
        x = playOneHitAndMatchGame()
        matchPoint += x
        print 'Current Point = ', matchPoint, '\n'
    return 0

if __name__ == '__main__':
    main()
