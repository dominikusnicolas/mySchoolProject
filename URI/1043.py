A,B,C = input().split()
A,B,C = float(A), float(B), float(C)

perimeter = A+B+C
Area = ((A+B)*C)/2

if A+B>C and A+C>B and B+C>A:
	print("Perimetro = %.1f" % (perimeter))
else:
	print("Area = %.1f" % (Area))