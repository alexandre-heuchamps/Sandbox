import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the ellipse parameters
lx = 2.5
ly = 0.12
theta = np.linspace(0, 2 * np.pi, 250)

# Define the key angles and times
key_angs = np.radians([0.0, 23.5, 48.79])
key_times = [0.0, 1.2, 2.6]

# Define the times at which to compute the orientations
times = np.linspace(np.min(key_times), np.max(key_times), 50)

# Compute the orientations at the specified times
orientations = np.interp(times, key_times, key_angs)

# Initial ellipse
points = np.array([lx * np.cos(theta), ly * np.sin(theta)])

x = np.empty((len(times), len(theta)))
y = np.empty((len(times), len(theta)))
for i, t in enumerate(orientations):
    rot_mat = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    x[i, :], y[i, :] = rot_mat @ points

# Create a figure and an axis
fig, ax = plt.subplots()

# Set the limits of the axis
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Create a line object for the ellipse
line, = ax.plot([], [], 's', markersize=.1)

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(i):
    line.set_data(x[i], y[i])
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(x), init_func=init, blit=True)
ani.save('ellipse_anim.mp4', fps = 30)

# Display the animation
plt.show()