even = 0
odd = 0
positive = 0
negative = 0

for i in range(5):
	n = int(input())
	if n%2==0:
		even+=1
	if n%2!=0:
		odd+=1
	if n>0:
		positive+=1
	if n<0:
		negative+=1

print("%i valor(es) par(es)" % (even))
print("%i valor(es) impar(es)" % (odd))
print("%i valor(es) positivo(s)" % (positive))
print("%i valor(es) negativo(s)" % (negative))