# Using map to Convert to Floats: The map(float, input().split()) function splits the input into a list of strings
#      and then converts each string to a float.

A, B, C = map(float, input().split())

tri = 1/2 * A * C
cir = 3.14159 * (C**2)
tra = 1/2 * (A+B) * C
squ = B ** 2
rec = A * B

print("TRIANGULO: {:.3f}".format(tri))
print("CIRCULO: {:.3f}".format(cir))
print("TRAPEZIO: {:.3f}".format(tra))
print("QUADRADO: {:.3f}".format(squ))
print("RETANGULO: {:.3f}".format(rec))
