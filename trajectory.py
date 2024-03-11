import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def projectile_motion(v0, theta, g=9.81, dt=0.01):
    """
    Calculates the trajectory of a projectile motion.

    Parameters:
        v0 (float): Initial velocity magnitude (m/s).
        theta (float): Launch angle in degrees.
        g (float, optional): Acceleration due to gravity (m/s^2). Default is 9.81 m/s^2.
        dt (float, optional): Time step (s). Default is 0.01 s.

    Returns:
        Tuple of arrays: (time, x_position, y_position)
    """
    theta = np.radians(theta)  # Convert angle to radians
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)
    
    t = 0
    x = 0
    y = 0
    time_list = [t]
    x_list = [x]
    y_list = [y]

    while y >= 0:
        t += dt
        x = vx0 * t
        y = vy0 * t - 0.5 * g * t**2

        time_list.append(t)
        x_list.append(x)
        y_list.append(y)

    return np.array(time_list), np.array(x_list), np.array(y_list)

def visualize_trajectory(time, x_position, y_position):
    """
    Visualizes the trajectory of a projectile.

    Parameters:
        time (array-like): Time array.
        x_position (array-like): x position array.
        y_position (array-like): y position array.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(x_position, y_position)
    plt.title('Projectile Motion')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.grid(True)
    plt.show()

def calculate_trajectory():
    try:
        v0 = float(entry_v0.get())
        theta = float(entry_theta.get())
        time, x_position, y_position = projectile_motion(v0, theta)
        visualize_trajectory(time, x_position, y_position)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for initial velocity and launch angle.")

# Create Tkinter GUI
root = tk.Tk()
root.title("Projectile Motion Predictor")

# Create input fields
label_v0 = tk.Label(root, text="Initial Velocity (m/s):")
label_v0.grid(row=0, column=0, padx=5, pady=5)
entry_v0 = tk.Entry(root)
entry_v0.grid(row=0, column=1, padx=5, pady=5)

label_theta = tk.Label(root, text="Launch Angle (degrees):")
label_theta.grid(row=1, column=0, padx=5, pady=5)
entry_theta = tk.Entry(root)
entry_theta.grid(row=1, column=1, padx=5, pady=5)

# Create button to calculate trajectory
calculate_button = tk.Button(root, text="Calculate Trajectory", command=calculate_trajectory)
calculate_button.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
