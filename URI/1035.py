A,B,C,D = input().split()
A,B,C,D = int(A), int(B), int(C), int(D)

sumCD = C+D
sumAB = A+B
statusA = A%2 == 0

if B>C and D>A and sumCD>sumAB and C>0 and D>0 and statusA:
	print("Valores aceitos")

else:
	print("Valores nao aceitos")