a,b,c = input().split(" ")
A = float(a)
B = float(b)
C = float(c)
T = (A * C) / 2
CIRC = C**2 * 3.14159
TRAP = (B + A) / 2 * C
Q = B * B
R = A * B
print ("TRIANGULO: %.3f" %T)
print ("CIRCULO: %.3f" %CIRC)
print ("TRAPEZIO: %.3f" %TRAP)
print ("QUADRADO: %.3f" %Q)
print ("RETANGULO: %.3f" %R)
