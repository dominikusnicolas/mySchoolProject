A,B,C = input().split()
A,B,C = float(A), float(B), float(C)

if A<0:
	A = abs(A)
if B<0:
	B = abs(B)
if C<0:
	C = abs(C)

angka = [A,B,C]
angka.sort(reverse = True)

A = angka[0]
B = angka[1]
C = angka[2]

if A>= B+C:
	print("NAO FORMA TRIANGULO")

elif A**2 >(B**2+C**2):
	print("TRIANGULO OBTUSANGULO")
	if A==B!=C or B==C!=A or A==C!=B:
		print("TRIANGULO ISOSCELES")
	if A==B==C:
		print("TRIANGULO EQUILATERO")

elif A**2 <(B**2+C**2):
	print("TRIANGULO ACUTANGULO")
	if A==B==C:
		print("TRIANGULO EQUILATERO")
	if A==B!=C or B==C!=A or A==C!=B:
		print("TRIANGULO ISOSCELES")

if A**2 ==(B**2+C**2):
	print("TRIANGULO RETANGULO")

