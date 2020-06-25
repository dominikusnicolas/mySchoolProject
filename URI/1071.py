X = int(input())
Y = int(input())

sums = 0

if(X>Y):
    Z=X
    X=Y
    Y=Z

if(X%2 != 0):
    X += 2
    while(X < Y):
        if(X%2 !=0):
            sums += X
        X += 1
else:
    X += 1
    while(X < Y):
        if(X%2 !=0):
            sums += X
        X += 1

print(sums)