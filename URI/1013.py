a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

MaiorAB = (a+b+abs(a-b))/2
MaiorAC = (MaiorAB+c+abs(MaiorAB-c))/2

print("%i eh o maior" % (MaiorAC))