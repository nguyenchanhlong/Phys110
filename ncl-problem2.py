import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 8.99e9  # Electrostatic constant (N m^2/C^2)

# Define charge and voltage values for problem A
Q_A = 9e-9  # Charge in Coulombs
V_values_A = [0.1, 1.0, 10.0]  # Voltage values in Volts

# Define charges and voltage values for problem B
Q1_B = 9e-9  # Charge 1 in Coulombs
Q2_B = 9e-9  # Charge 2 in Coulombs
separation_distance = 1.0  # Separation distance in meters
V_values_B = [0.1, 1.0, 10.0]  # Voltage values in Volts

# Create a grid of points in space
x = np.linspace(-2, 2, 400)  # Adjust the range and resolution as needed
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Initialize potential arrays for problem A and B
V_A = np.zeros_like(X)
V_B = np.zeros_like(X)

# Calculate electric potentials for problem A
for V in V_values_A:
    V_A += k * Q_A / np.sqrt((X**2 + Y**2))

# Calculate electric potentials for problem B
for V in V_values_B:
    r1 = np.sqrt((X - separation_distance/2)**2 + Y**2)
    r2 = np.sqrt((X + separation_distance/2)**2 + Y**2)
    V_B += k * (Q1_B / r1 + Q2_B / r2)

# Create contour plots for problem A
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.contourf(X, Y, V_A, cmap='coolwarm')
plt.colorbar()
plt.title('Electric Potential for Problem A (V=0.1V)')

plt.subplot(132)
plt.contourf(X, Y, V_A, cmap='coolwarm')
plt.colorbar()
plt.title('Electric Potential for Problem A (V=1.0V)')

plt.subplot(133)
plt.contourf(X, Y, V_A, cmap='coolwarm')
plt.colorbar()
plt.title('Electric Potential for Problem A (V=10.0V)')

plt.tight_layout()

# Create contour plots for problem B
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.contourf(X, Y, V_B, cmap='coolwarm')
plt.colorbar()
plt.title('Electric Potential for Problem B (V=0.1V)')

plt.subplot(132)
plt.contourf(X, Y, V_B, cmap='coolwarm')
plt.colorbar()
plt.title('Electric Potential for Problem B (V=1.0V)')

plt.subplot(133)
plt.contourf(X, Y, V_B, cmap='coolwarm')
plt.colorbar()
plt.title('Electric Potential for Problem B (V=10.0V)')

plt.tight_layout()
plt.show()
