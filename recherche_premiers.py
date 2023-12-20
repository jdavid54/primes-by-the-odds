
#all primes under max
max=10000
root=[]

for n in range(3,max//3):
	if n%2!=0:
		#print(n)
		root.append(n)
#print(root)

ticks=[]
for n,v in enumerate(root):
	for w in root[n:]:
		if v*w not in ticks and v*w<max:
			ticks.append(v*w)
ticks.sort()
#print(ticks)	

primes=[2,3,5,7]
for k in range(len(ticks)-1):
	bas=ticks[k]
	haut=ticks[k+1]
	#print(f"{bas}-{haut}:",end="")
	for j in range(1,haut-bas):
		v=bas+j
		
		if v%2!=0:
			#print(v,end=",")
			primes.append(v)
	print()
	
print(primes)	