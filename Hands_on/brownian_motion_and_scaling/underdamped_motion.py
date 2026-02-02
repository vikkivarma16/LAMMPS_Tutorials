import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------
m = 1.0          # mass
gamma = 0.1      # friction coefficient (underdamped: gamma < 2*sqrt(k/m))
kB = 1.0         # Boltzmann constant
T = 1.0          # temperature
dt = 0.01        # time step
steps = 5000     # number of steps

# -----------------------------
# Initialize arrays
# -----------------------------
pos = np.zeros((steps, 2))  # positions x, y
vel = np.zeros((steps, 2))  # velocities vx, vy

# -----------------------------
# Langevin dynamics (Euler-Maruyama)
# -----------------------------
for i in range(1, steps):
    # Gaussian random force
    eta = np.sqrt(2 * gamma * kB * T / dt) * np.random.randn(2)
    
    # Update velocity
    vel[i] = vel[i-1] + dt * (-gamma * vel[i-1] / m) + dt * eta / m
    
    # Update position
    pos[i] = pos[i-1] + vel[i] * dt

# -----------------------------
# Plot trajectory
# -----------------------------
plt.figure(figsize=(6,6))
plt.plot(pos[:,0], pos[:,1], lw=1)
plt.scatter(pos[0,0], pos[0,1], color='green', label='Start')
plt.scatter(pos[-1,0], pos[-1,1], color='red', label='End')
plt.title("2D Langevin Dynamics (Underdamped)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis('equal')
plt.tight_layout()
plt.savefig("langevin_trajectory_underdamped.png", dpi=300)
