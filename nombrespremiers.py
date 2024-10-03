def primegen(maxn=float("inf"),count=float("inf")):
	# Sequentially output primes. Outputs all p<maxn or the first 'count' primes.
	for n in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47):
		if n>=maxn or count<=0: return
		yield n
		count-=1
	# Recursive generator pour les nombres suivants.
	r,sq,n=7,49,49
	it=iter(primegen())
	while next(it)<r: pass
	comp=dict()
	jump=(1,6,5,4,3,2,1,4,3,2,1,2,1,4,3,
	      2,1,2,1,4,3,2,1,6,5,4,3,2,1,2)
	while n<maxn and count>0:
		# Vérifie si on a un facteur de n.
		f=comp.pop(n,0)
		if n==sq:
			# n=r*r c'est le prochain premier qu'on cherche
			f,r=r,next(it)
			sq=r*r
		elif f==0:
			# n!=sq et c'est pas dans le comp, donc c'est premier.
			yield n
			count-=1
		if f:
			# trouve les facteurs de N. ajouté à compiler.
			q=n//f
			q+=jump[q%30]
			while q*f in comp: q+=jump[q%30]
			comp[q*f]=f
		n+=jump[n%30]

print("Loop iterator test:")
for p in primegen():
	if p>200: break
	print(p)