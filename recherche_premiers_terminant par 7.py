# https://www.youtube.com/watch?v=cONhad3q10s

debug = False
#all primes ending with 7 smaller than max
max=500
root3=[]
root9=[]
root7=[]
root11=[]

for n in range(max//3):
    root3.append(10*n+3)
    root9.append(10*n+9)
for n in range(max//7):
    root7.append(10*n+7)
    root11.append(10*n+11)
    
if debug:
    print(root3)
    print(root9)
    print(root7)
    print(root11)

ticks=[]

# (10k+7)*(10k+11)
for n,v in enumerate(root7):
    for w in root11[n:]:
        if v*w not in ticks and v*w<max:
            ticks.append(v*w)
# (10k+3)*(10k+9)
for n,v in enumerate(root3):
    for w in root9[n:]:
        if v*w not in ticks and v*w<max:
            ticks.append(v*w)
ticks.sort()
print("ticks",ticks)

primes_7=[7,17]
for k in range(len(ticks)-1):
    bas=ticks[k]
    haut=ticks[k+1]
    #print(f"{bas}-{haut}:",end="")
    for j in range(1,(haut-bas)//10):
        v=bas+j*10        
        primes_7.append(v)
        #print(v,end=",")
    #print()
print()
print(len(primes_7),primes_7)
