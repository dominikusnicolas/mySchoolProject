a,b = input().split()
a,b = int(a), int(b)

result = b-a
if result<=0:
	result+= 24

print("O JOGO DUROU %i HORA(S)" % (result))