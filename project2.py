import math
# 1)
x = int(input('Enter x variable:'))
t = int(input('Enter t variable:'))
z = (math.pow(math.e, x) * (9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - math.fabs(math.sin(t))))
print("z =",z)
