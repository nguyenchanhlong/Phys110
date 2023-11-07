import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

class ElectronMotionAnimation:
    def __init__(self):
        # Constants
        self.e = -1.6e-19  # Charge of the electron (in Coulombs)
        self.m = 9.11e-31  # Mass of the electron (in kg)
        self.E = 200.0  # Electric field strength (in N/C)
        self.vi = 3.0e6  # Initial velocity (in m/s)
        self.l = 0.1  # Horizontal length of the plates (in meters)

        # Calculate acceleration due to electric field
        self.a_e = self.e * self.E / self.m

        # Calculate time of flight
        self.t = self.l / self.vi

        # Create an array of time values
        self.time_values = np.linspace(0, self.t, num=100)

        # Initialize position arrays
        self.xi = 0  # Initial horizontal position
        self.yi = 0.035  # Initial vertical position
        self.vxi = self.vi  # Initial horizontal velocity
        self.vyi = 0  # Initial vertical velocity

        self.x_values = []
        self.y_values = []
        self.vx_values = []  # Store horizontal velocity components for each frame
        self.vy_values = []  # Store vertical velocity components for each frame

        # Calculate the positions and velocity components at each time point
        for t_value in self.time_values:
            self.x_values.append(self.xi + self.vxi * t_value)
            self.y_values.append(self.yi + self.vyi * t_value + 0.5 * self.a_e * (t_value ** 2))
            self.vx_values.append(self.vxi)
            self.vy_values.append(self.vyi + self.a_e * t_value)

        # Create a figure for the animation
        self.fig = plt.figure(figsize=(10, 5))

        # Create the animation
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.time_values), interval=50)

    def update(self, frame):
        plt.clf()
        plt.plot(self.x_values[:frame], self.y_values[:frame], 'g')  # Change path color to green
        plt.quiver(self.x_values[frame], self.y_values[frame], 0.5 * self.vx_values[frame], 0.5 * self.vy_values[frame], angles='xy', scale_units='xy', color='b', label='Velocity')  # Change velocity vector color to blue and adjust the scale
        plt.xlabel('Horizontal Position (m)')
        plt.ylabel('Vertical Position (m)')
        plt.title('Electron Motion in Uniform Electric Field')
        plt.grid(True)
        plt.xlim(0, self.l)  # Set fixed x-axis limits
        plt.ylim(0, max(self.y_values))  # Set fixed y-axis limits
        plt.legend()

    def show_animation(self):
        # Display the animation
        plt.show()

if __name__ == "__main__":
    electron_animation = ElectronMotionAnimation()
    electron_animation.show_animation()
