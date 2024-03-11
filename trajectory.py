import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def projectile_motion(v0, theta, g=9.81, dt=0.01, wind_speed=0, wind_angle=0, air_density=1.225):
    """
    Calculates the trajectory of a projectile motion considering environmental variables.

    Parameters:
        v0 (float): Initial velocity magnitude (m/s).
        theta (float): Launch angle in degrees.
        g (float, optional): Acceleration due to gravity (m/s^2). Default is 9.81 m/s^2.
        dt (float, optional): Time step (s). Default is 0.01 s.
        wind_speed (float, optional): Wind speed (m/s). Default is 0 m/s.
        wind_angle (float, optional): Wind angle in degrees (0 degrees means wind is blowing directly against the motion of the projectile). Default is 0 degrees.
        air_density (float, optional): Air density (kg/m^3). Default is 1.225 kg/m^3.

    Returns:
        Tuple of arrays: (time, x_position, y_position)
    """
    def model(state, t):
        x, y, vx, vy = state
        v = np.sqrt(vx**2 + vy**2)
        dxdt = vx
        dydt = vy
        dvxdt = -0.5 * air_density * v * (v + wind_speed) * (vx / v)**2
        dvydt = -g - 0.5 * air_density * v * (v + wind_speed) * (vy / v)**2
        return [dxdt, dydt, dvxdt, dvydt]

    theta = np.radians(theta)  # Convert angle to radians
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)
    state0 = [0, 0, vx0, vy0]
    t = np.arange(0, 100, dt)
    states = odeint(model, state0, t)
    x_position = states[:, 0]
    y_position = states[:, 1]
    return t, x_position, y_position

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
        wind_speed = float(entry_wind_speed.get())
        wind_angle = float(entry_wind_angle.get())
        air_density = float(entry_air_density.get())
        time, x_position, y_position = projectile_motion(v0, theta, wind_speed=wind_speed, wind_angle=wind_angle, air_density=air_density)
        visualize_trajectory(time, x_position, y_position)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for input parameters.")

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

label_wind_speed = tk.Label(root, text="Wind Speed (m/s):")
label_wind_speed.grid(row=2, column=0, padx=5, pady=5)
entry_wind_speed = tk.Entry(root)
entry_wind_speed.grid(row=2, column=1, padx=5, pady=5)

label_wind_angle = tk.Label(root, text="Wind Angle (degrees):")
label_wind_angle.grid(row=3, column=0, padx=5, pady=5)
entry_wind_angle = tk.Entry(root)
entry_wind_angle.grid(row=3, column=1, padx=5, pady=5)

label_air_density = tk.Label(root, text="Air Density (kg/m^3):")
label_air_density.grid(row=4, column=0, padx=5, pady=5)
entry_air_density = tk.Entry(root)
entry_air_density.grid(row=4, column=1, padx=5, pady=5)

# Create button to calculate trajectory
calculate_button = tk.Button(root, text="Calculate Trajectory", command=calculate_trajectory)
calculate_button.grid(row=5, columnspan=2, padx=5, pady=5)

root.mainloop()
