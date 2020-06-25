lists = []
lists.append(float(input()))
lists.append(float(input()))
lists.append(float(input()))
lists.append(float(input()))
lists.append(float(input()))
lists.append(float(input()))

positive = 0
sums = 0.0

for n in lists:
    if(n>0):
        positive += 1
        sums += n

avg = sums / positive
print("%i valores positivos" % (positive))
print("%.1f" % (avg))