import sys

try:
    _stdout = sys.stdout.write
except IOError:
    _stdout = lambda x: sys.stdout.write(x)
    
def duplicates(q):
    p = set(q)
    if len(p) != len(q):
        return True
    else:
        return False

def diagonal_threat(q):
    for i,a in enumerate(q):
        for j,b in enumerate(q):
            if i != j:
                if abs(j-i) == abs(b-a):
                    return True
    return False
        
def main():
    count = 0
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    for e in range(8):
                        for f in range(8):
                            for g in range(8):
                                for h in range(8):
                                    q = [a,b,c,d,e,f,g,h]
                                    if not duplicates(q) and not diagonal_threat(q):
                                        count += 1
                                        _stdout('Solution number %s is: %s' %(str(count),str(q)))
                                        
        
if __name__ == '__main__':
    main()
    
    
    
    
    
