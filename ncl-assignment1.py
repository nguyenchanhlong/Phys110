import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# INPUT DATA
ke = 9e9
Q = [1e-9, -1e-9]  # Multiple charges

xQ = [0.5, -0.5]  # Coordinates of charges
yQ = [0.5, -0.5]
zQ = [0.5, -0.5]

xA = 1
yA = 1
zA = 1

# CALCULATION
N = len(Q)
Nx = 20
Ny = 20
Nz = 20
x = np.linspace(-1, 2, Nx)
y = np.linspace(-1, 2, Ny)
z = np.linspace(-1, 2, Nz)
X, Y, Z = np.meshgrid(x, y, z)

Ex = np.zeros(X.shape)
Ey = np.zeros(Y.shape)
Ez = np.zeros(Z.shape)

for iN in range(N):
    r = np.sqrt((X - xQ[iN])**2 + (Y - yQ[iN])**2 + (Z - zQ[iN])**2)
    E = ke * Q[iN] / r**3

    Ex += E * (X - xQ[iN])  # x-component of vector field
    Ey += E * (Y - yQ[iN])  # y-component of vector field
    Ez += E * (Z - zQ[iN])  # z-component of vector field

# Create a mask to exclude points close to charges
condition = r < 0.3
Ex[condition] = 0
Ey[condition] = 0
Ez[condition] = 0

# FIGURE
fig = plt.figure(figsize=(20, 8))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(X, Y, Z, Ex, Ey, Ez, normalize=True, color='b')

# Draw charged particles
for iN in range(N):
    radius = 0.1
    u = np.linspace(0, 2 * np.pi, 10)
    v = np.linspace(0, np.pi, 10)
    x1 = radius * np.outer(np.cos(u), np.sin(v)) + xQ[iN]
    y1 = radius * np.outer(np.sin(u), np.sin(v)) + yQ[iN]
    z1 = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + zQ[iN]

    ax.plot_surface(x1, y1, z1, color='r', alpha=0.1)

# Axis properties
ax.set_xlabel('X, m')
ax.set_ylabel('Y, m')
ax.set_zlabel('Z, m')
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_zlim(-1, 2)
ax.view_init(-10, 20)
ax.set_box_aspect([1, 1, 1])

plt.show()
