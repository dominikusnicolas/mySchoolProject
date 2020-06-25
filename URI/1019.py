time = int(input())

pecahanWaktu = [3600,60,1]
result = []

for waktu in pecahanWaktu:
	reminder = time //waktu
	time -= (reminder*waktu)
	result.append(reminder)

print("%i:%i:%i" % (result[0], result[1], result[2]))