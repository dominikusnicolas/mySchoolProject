N = int(input())

for i in range(N):
	value = int(input())
	if value%2==0:
		if value==0:
			print("NULL")
		elif value>0:
			print("EVEN POSITIVE")
		elif value<0:
			print("EVEN NEGATIVE")
	else:
		if value>0:
			print("ODD POSITIVE")
		elif value<0:
			print("ODD NEGATIVE")