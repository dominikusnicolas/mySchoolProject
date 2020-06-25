a = input().split()
d1 = int(a[1])

b = input().split(" : ")
h1,m1,s1 = list(map(int,b))


c = input().split()
d2 = int(c[1])

d = input().split(" : ")
h2,m2,s2 = list(map(int,d))

d = d2-d1

h = h2-h1
if h<0:
	h += 24
	d -= 1

m = m2-m1
if m<0:
	m += 60
	h -= 1

s = s2-s1
if s<0:
	s += 60
	m -= 1

if d<=0:
	d = 0

print("%i dia(s)" % (d))
print("%i hora(s)" % (h))
print("%i minuto(s)" % (m))
print("%i segundo(s)" % (s))