a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

number = [a,b,c]

sorted_number = sorted(number)

print("%i" % (sorted_number[0]))
print("%i" % (sorted_number[1]))
print("%i" % (sorted_number[2]))
print('')
print("%i" % (number[0]))
print("%i" % (number[1]))
print("%i" % (number[2]))