import math

a,b,c = input().split()
a,b,c = float(a), float(b), float(c)

Bhaskara = (b**2-4*a*c)
if Bhaskara < 0 or a==0:
	print("Impossivel calcular")
else:
	R1 = (-b+math.sqrt(Bhaskara))/(2*a)
	R2 = (-b-math.sqrt(Bhaskara))/(2*a)
	print("R1 = %.5f" % (R1))
	print("R2 = %.5f" % (R2))
