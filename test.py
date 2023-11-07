import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# INPUT DATA
ke = 9e9
Q = 9e-9  # Charge of electron 1 (Q)
A = 9e-9  # Charge of electron 2 (A)

xQ = -1  # Coordinates of electron 1 (Q)
yQ = 0
zQ = 0

xA = 1  # Coordinates of electron 2 (A)
yA = 0
zA = 0

# CALCULATION
Nx = 20
Ny = 20
Nz = 20
x = np.linspace(-1, 2, Nx)
y = np.linspace(-1, 1, Ny)
z = np.linspace(-1, 1, Nz)
X, Y, Z = np.meshgrid(x, y, z)

Ex_Q = np.zeros(X.shape)
Ey_Q = np.zeros(Y.shape)
Ez_Q = np.zeros(Z.shape)

Ex_A = np.zeros(X.shape)
Ey_A = np.zeros(Y.shape)
Ez_A = np.zeros(Z.shape)

rQ = np.sqrt((X - xQ) ** 2 + (Y - yQ) ** 2 + (Z - zQ) ** 2)
rA = np.sqrt((X - xA) ** 2 + (Y - yA) ** 2 + (Z - zA) ** 2)

EQ = ke * Q / rQ ** 3
EA = ke * A / rA ** 3

Ex_Q += 0.1 * EQ * (X - xQ)  # x-component of vector field for electron 1 (Q)
Ey_Q += 0.1 * EQ * (Y - yQ)  # y-component of vector field for electron 1 (Q)
Ez_Q += 0.1 * EQ * (Z - zQ)  # z-component of vector field for electron 1 (Q)

Ex_A += 0.1 * EA * (X - xA)  # x-component of vector field for electron 2 (A)
Ey_A += 0.1 * EA * (Y - yA)  # y-component of vector field for electron 2 (A)
Ez_A += 0.1 * EA * (Z - zA)  # z-component of vector field for electron 2 (A)

# Create masks to exclude points close to the electrons
conditionQ = rQ < 0.1
conditionA = rA < 0.1

Ex_Q[conditionQ] = 0
Ey_Q[conditionQ] = 0
Ez_Q[conditionQ] = 0

Ex_A[conditionA] = 0
Ey_A[conditionA] = 0
Ez_A[conditionA] = 0

# FIGURE
fig = plt.figure(figsize=(20, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot electric field for electron 1 (Q)
ax.quiver(X, Y, Z, Ex_Q, Ey_Q, Ez_Q, normalize=True, color='r', length=0.1, label='Electric Field (Q)')

# Plot electric field for electron 2 (A)
ax.quiver(X, Y, Z, Ex_A, Ey_A, Ez_A, normalize=True, color='g', length=0.1, label='Electric Field (A)')

# Draw electrons
radius = 0.05
u = np.linspace(0, 2 * np.pi, 10)
v = np.linspace(0, np.pi, 10)

# Electron 1 (Q)
xQ_surface = radius * np.outer(np.cos(u), np.sin(v)) + xQ
yQ_surface = radius * np.outer(np.sin(u), np.sin(v)) + yQ
zQ_surface = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + zQ
ax.plot_surface(xQ_surface, yQ_surface, zQ_surface, color='r', alpha=0.5)

# Electron 2 (A)
xA_surface = radius * np.outer(np.cos(u), np.sin(v)) + xA
yA_surface = radius * np.outer(np.sin(u), np.sin(v)) + yA
zA_surface = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + zA
ax.plot_surface(xA_surface, yA_surface, zA_surface, color='g', alpha=0.5)

# Axis properties
ax.set_xlabel('X, m')
ax.set_ylabel('Y, m')
ax.set_zlabel('Z, m')
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.view_init(-10, 20)
ax.set_box_aspect([1, 1, 1])

ax.legend()

plt.show()
