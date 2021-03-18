n=eval(input("enter no. of lines"))
k=65
for i in range(1,n+1):
	for j in range(0,i):
		print(chr(k),end=" ")
		k+=1
	print()
