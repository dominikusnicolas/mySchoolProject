A,B,C = input().split()
A,B,C = float(A), float(B), float(C)

pi = 3.14159

triangle = (A*C)/2
circle = (pi*(C**2))
trapezium = ((A+B)*C)/2
square = B**2
rectangle = A*B

print("TRIANGULO: %.3f" % (triangle))
print("CIRCULO: %.3f" % (circle))
print("TRAPEZIO: %.3f" % (trapezium))
print("QUADRADO: %.3f" % (square))
print("RETANGULO: %.3f" % (rectangle))