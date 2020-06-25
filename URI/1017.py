time = int(input()) #dalam h
avgSpeed = int(input()) #dalam km/h
#using a car that does 12 km/L
cost = avgSpeed / 12

result = cost*time

print("%.3f" % (result))