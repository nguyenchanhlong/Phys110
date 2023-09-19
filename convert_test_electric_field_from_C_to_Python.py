import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# INPUT DATA
ke = 9e9
Q = [1e-9]  # charges

xQ = [0]  # coordinates of charges
yQ = [0]
zQ = [0]

xA = 1
yA = 1
zA = 1

r = np.sqrt((xA - xQ[0])**2 + (yA - yQ[0])**2 + (zA - zQ[0])**2)

rx = (xA - xQ[0]) / r
ry = (yA - yQ[0]) / r
rz = (zA - zQ[0]) / r

E0 = ke * Q[0] / r**2

Ex = E0 * rx
Ey = E0 * ry
Ez = E0 * rz

streak_arrow = 0  # Use quiver instead of streakarrow

xmin, xmax = -1, 1
ymin, ymax = -1, 1
zmin, zmax = -1, 1

# CALCULATION
N = len(Q)
Nx = 10
Ny = 10
Nz = 10
x = np.linspace(xmin, xmax, Nx)
y = np.linspace(ymin, ymax, Ny)
z = np.linspace(zmin, zmax, Nz)
X, Y, Z = np.meshgrid(x, y, z)

Ex = np.zeros(X.shape)
Ey = np.zeros(Y.shape)
Ez = np.zeros(Z.shape)

for iN in range(N):
    r = np.sqrt((X - xQ[iN])**2 + (Y - yQ[iN])**2 + (Z - zQ[iN])**2)
    E = ke * Q[iN] / r / r

    Ex += E / r * (X - xQ[iN])  # x-component of vector field
    Ey += E / r * (Y - yQ[iN])  # y-component of vector field
    Ez += E / r * (Z - zQ[iN])  # z-component of vector field

    condition = r < 0.3
    Ex[condition] = 0
    Ey[condition] = 0
    Ez[condition] = 0

# FIGURES
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

if streak_arrow:
    # Replace this with your streakarrow3d implementation or use a different library.
    # streakarrow3d(X, Y, Z, Ex, Ey, Ez, 2, 1)
    pass
else:
    ax.quiver(X, Y, Z, Ex, Ey, Ez, normalize=True, color='b', arrow_length_ratio=0.01)  # Adjust arrow_length_ratio here

# Draw charged particles
for iN in range(N):
    radius = 0.1
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x1 = radius * np.outer(np.cos(u), np.sin(v)) + xQ[iN]
    y1 = radius * np.outer(np.sin(u), np.sin(v)) + yQ[iN]
    z1 = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + zQ[iN]

    ax.plot_surface(x1, y1, z1, color='r', alpha=0.5)

# Axis properties
ax.set_xlabel('X, m')
ax.set_ylabel('Y, m')
ax.set_zlabel('Z, m')
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_zlim(zmin, zmax)
ax.view_init(-20, 30)
ax.set_box_aspect([1, 1, 1])

plt.show()
