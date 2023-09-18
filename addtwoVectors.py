import numpy as np
import math

ax = math.cos(math.pi/4)
ay = ax

bx = 2*math.cos(math.pi/3)
by = 2*math.sin(math.pi/3)

A = (ax,ay)
B = (bx,by)

print("Vector A: ", A,"\n","Vector B: ",B)

S = np.array([ax+bx,ay+by])
print(S)