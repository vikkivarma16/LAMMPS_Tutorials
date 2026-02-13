import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Input / output files
# -----------------------------
input_file = "liquid_vapor_densities.txt"
output_file = "binodal_curve.png"

# -----------------------------
# Load data
# Columns:
# T | rho_vapor | rho_liquid
# -----------------------------
data = np.loadtxt(input_file)

T = data[:, 0]
rho_v = data[:, 1]
rho_l = data[:, 2]

# -----------------------------
# Estimate critical point
# Critical point occurs where
# rho_liquid - rho_vapor -> minimum
# -----------------------------
delta_rho = rho_l - rho_v
crit_index = np.argmin(delta_rho)

T_c = T[crit_index]
rho_c = 0.5 * (rho_l[crit_index] + rho_v[crit_index])

# -----------------------------
# Plot binodal curve
# -----------------------------
plt.figure(figsize=(6, 6))

# Vapor branch
plt.plot(rho_v, T, 'bo-', label='Vapor branch')

# Liquid branch
plt.plot(rho_l, T, 'ro-', label='Liquid branch')

# Critical point
plt.plot(rho_c, T_c, 'ks', markersize=8, label='Critical point')

# Labels and title
plt.xlabel("Density")
plt.ylabel("Temperature")
plt.title("Liquid–Vapor Binodal Curve")

# Formatting
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save high-resolution figure
plt.savefig(output_file, dpi=600)
plt.show()

# -----------------------------
# Print critical point info
# -----------------------------
print("Estimated critical point:")
print(f"  T_c   = {T_c:.5f}")
print(f"  rho_c = {rho_c:.5f}")
