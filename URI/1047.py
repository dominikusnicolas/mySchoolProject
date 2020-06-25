a,b,c,d = input().split()
a,b,c,d = int(a), int(b), int(c), int(d)

result1 = c-a
result2 = d-b

if result1==0 and result2==0:
	result1+= 24

elif result1==0 and result2<0:
	result2+= 60
	result1+= 23

elif result1>0 and result2<0:
	result2+= 60
	result1-= 1

elif result1<0 and result2==0:
	result1+= 24

elif result1<0 and result2>0:
	result1+= 24

elif result1<0 and result2<0:
	result1+= 23
	result2+= 60

print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (result1, result2))


'''
elif result1 >=24 and result2!=0:
	result1-= 24
'''