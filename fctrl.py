t=input()
def calc2(no):
	total=0
	i=1
	while no/(2**i)>=1:
		total+=int(no/(2**i))
		i+=1
	return total

def calc5(no):
	total=0
	i=1
	while no/(5**i)>=1:
		total+=int(no/(5**i))
		i+=1
	return total

for i in range(t):
	inp=input()
	print min(calc5(inp),calc2(inp))
