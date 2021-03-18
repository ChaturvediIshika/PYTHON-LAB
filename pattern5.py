n=eval(input("enter no. of lines"))
t=n
for i in range(1,n*2,+2):
	for k in range(0,t):
		print(" ",end=" ")
	t-=1
	for j in range(0,i):
		print("*",end=" ")
	print()
