import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Input and output files
# -----------------------------
input_file = "viscosity_vs_density.txt"
output_file = "viscosity_vs_density.png"

# -----------------------------
# Load data
# -----------------------------
# Assumes two columns: density (rho) and viscosity (eta)
data = np.loadtxt(input_file)
density = data[:, 0]
viscosity = data[:, 1]

# -----------------------------
# Create plot
# -----------------------------
plt.figure(figsize=(8, 6))
plt.plot(density, viscosity, marker='o', linestyle='-', color='b', label='Viscosity vs Density')

# Add labels and title
plt.xlabel("Density (ρ)")
plt.ylabel("Viscosity (η, LJ units)")
plt.title("Viscosity vs Density for LJ Fluid (Green-Kubo)")

# Add legend and grid
plt.legend()
plt.grid(True)

# Save figure as high-resolution PNG
plt.savefig(output_file, dpi=300)
