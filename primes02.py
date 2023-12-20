from numpy import sqrt
max = 50000
odds=[]
primes = []
ops=0
debug = False

def dummy(*args, **kargs): pass

if not debug: 
    #don't print
    xprint = dummy
else:
    #please print for debug
    xprint = print

print(f"Searching primes until {max}")
for n in range(3,max,2):
    prime=True
    #odds.append(n)
    for k in primes:
        ops+=1
        xprint(n,k,n%k==0,end="")
        if (n%k) == 0:
            prime = False
            xprint()
            xprint(n," is not prime!")
            xprint()
            break
        else:
            xprint()
    # after divisions with all primes or n not prime   
    if prime and n not in primes:
        xprint(n," is prime !")
        primes.append(n)
        xprint()
                
primes = [2] + primes               
#xprint(odds)
print(primes)
xprint(ops)	