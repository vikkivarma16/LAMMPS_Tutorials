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
# Generate random non-white color
# -----------------------------
# RGB values between 0 and 0.85 to avoid white/light colors
random_color = np.random.uniform(0.0, 0.85, size=3)

# -----------------------------
# Create plot
# -----------------------------
plt.figure(figsize=(8, 6))
plt.plot(
    density,
    viscosity,
    marker='o',
    linestyle='-',
    color=random_color,
    label='Viscosity vs Density'
)

# Add labels and title
plt.xlabel("Density (ρ)")
plt.ylabel("Viscosity (η, LJ units)")
plt.title("Viscosity vs Density for LJ Fluid (Green-Kubo)")

# Add legend and grid
plt.legend()
plt.grid(True)

# Save figure as high-resolution PNG
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close()

print(f"Plot saved as {output_file} with color {random_color}")

