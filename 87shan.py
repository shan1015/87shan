N=input()
l=list(permutations(N))
b=2
for i in range(len(l)):
	if l[i]==l[i][::-1]:
		b=3
		print("yes")
		break
if b==2;
	print("no")
