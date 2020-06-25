start = int(input())
count = 0

while True:
	if start%2 !=0:
		count+=1
		print(start)
	start +=1
	
	if count == 6:
		break