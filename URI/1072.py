n = int(input())

enter = 0
exit = 0

for i in range(n):
	value = int(input())
	if 10<=value<=20:
		enter+=1
	else:
		exit+=1

print("%i in" % (enter))
print("%i out" % (exit))