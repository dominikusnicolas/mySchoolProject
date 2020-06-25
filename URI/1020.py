hari = int(input())

pecahanTahun = [365,30,1]
result = []

for count in pecahanTahun:
	reminder = hari//count
	hari -= reminder*count
	result.append(reminder)

print("%i ano(s)" % (result[0]))
print("%i mes(es)" % (result[1]))
print("%i dia(s)" % (result[2]))