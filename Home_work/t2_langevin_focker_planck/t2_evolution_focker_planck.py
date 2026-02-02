import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm  # For the progress bar

# Parameters for the simulation
x_min, x_max = -5, 5   # Spatial domain
dx = 0.2               # Spatial step
t_max = 40.0            # Maximum time
dt = 0.01             # Time step
D = 1.0                # Diffusivity


# Caution: If you are taking dt too small the code will not converge.. in that case you would have to take dx greater to keep the total value alpha =  D dt/dx*dx < 0.5... which is a restriction to solve this code...


# Discretize the spatial domain
x = np.arange(x_min, x_max + dx, dx)
N = len(x)

# Initial condition: Gaussian centered at x=0
P = np.exp(-x**2) / np.sqrt(np.pi)
P /= np.sum(P * dx)  # Normalize

# Precompute the coefficient for the finite difference scheme
alpha = D * dt / dx**2

# Prepare the plot
fig, ax = plt.subplots()
line, = ax.plot(x, P, lw=2)
time_text = ax.text(0.95, 0.95, '', transform=ax.transAxes, 
                    ha='right', va='top', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
ax.set_xlim(x_min, x_max)
ax.set_ylim(0, 1)
ax.set_xlabel("x")
ax.set_ylabel("P(x, t)")
ax.set_title("Evolution of P(x, t) (Fokker-Planck Equation)")

# Update function for animation with a progress bar
def update(frame):
    global P
    # Apply the finite difference scheme (explicit method)
    P_new = P.copy()
    P_new[1:-1] = P[1:-1] + alpha * (P[2:] - 2 * P[1:-1] + P[:-2])
    P = P_new.copy()
    line.set_ydata(P)
    time_text.set_text(f"Time: {frame * dt:.2f} s")
    
    # Update the progress bar
    if frame == 0:
        tqdm_bar.update(0)  # Initialize progress bar at start
    tqdm_bar.update(1)  # Update the progress bar after each frame
    
    return line, time_text

# Create the progress bar using tqdm
frames = int(t_max / dt)
tqdm_bar = tqdm(total=frames, desc="Simulation Progress", position=0)

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, blit=True, interval=30)

# Save the animation as a GIF

ani.save("fokker_planck_evolution.gif", writer='pillow', fps=30)


# Close the progress bar when the animation is finished
tqdm_bar.close()


