lista=[]
n=input("Romanos: ")
n=n.replace("I", "1+")
n=n.replace("V", "5+")
n=n.replace("X", "10+")
n=n.replace("L", "50+")
n=n.replace("C", "100+")
n=n.replace("D", "500+")
n=n.replace("M", "1000+")
n=n.replace("+", " ")
n=n.split()
n="+".join(n)
n=n.replace("+", " + ")
n=n.split()
l=len(n)-1
while l>=2:
	if int(n[l-2])<int(n[l]):
		R=n[l-2]
		n[l-2]=n[l]
		n[l]=R
		n[l-1]="-"
	if l!=1 and l!=0:
		l=l-2
lista=n
n=""
for k in lista:
	n=n+k
print("O número em decimal é", eval(n))