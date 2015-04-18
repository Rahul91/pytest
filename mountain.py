n=int(raw_input())
a=[]
for i in range(n):
	a.insert(i,int(raw_input()))

i=0
path = ""
while (i<=n):
	if i==0:
		if a[i]>a[i+1]:
			path = path + "B"
		else:
			path = path + "A"

	i=i+3
	j=0
	if (i<n):
		A=a[i]+a[i-1]
		B=a[i+1]+a[i-1]

		#print i,i-3,A, B, path[j]


		if A>B:
			if path[j]=="A":
				path = path + "CB"
			else:
				path = path + "B"
		else:
			if path[j]=="B":
				path = path	+ "CA"
			else:
				path = path + "A"

		j+=1

print path