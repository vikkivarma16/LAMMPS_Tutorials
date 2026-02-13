import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -----------------------------
# Define the tanh mean-field profile
# -----------------------------
def tanh_profile(z, rho_l, rho_g, z0, alpha):
    """
    Tanh function describing the liquid-gas density profile.
    """
    return 0.5 * (rho_l + rho_g) + 0.5 * (rho_l - rho_g) * np.tanh((z - z0) / alpha)

# -----------------------------
# Load data
# -----------------------------
# Data format: first column -> z, second column -> density
z, rho_noisy = np.loadtxt('averaged_density_profile.txt', unpack=True)

# -----------------------------
# Initial parameter estimates
# -----------------------------
rho_l_init = np.max(rho_noisy)
rho_g_init = np.min(rho_noisy)
z0_init = z[np.argmax(np.abs(np.gradient(rho_noisy)))]
alpha_init = (np.max(z) - np.min(z)) / 10

# -----------------------------
# Curve fitting
# -----------------------------
popt, pcov = curve_fit(
    tanh_profile,
    z,
    rho_noisy,
    p0=[rho_l_init, rho_g_init, z0_init, alpha_init]
)

rho_l_fit, rho_g_fit, z0_fit, alpha_fit = popt

print(f"Fitted Liquid Density: {rho_l_fit}")
print(f"Fitted Gas Density: {rho_g_fit}")
print(f"Fitted Interface Position (z0): {z0_fit}")
print(f"Fitted Interface Width (alpha): {alpha_fit}")

# -----------------------------
# Interface boundaries
# -----------------------------
interface_start = z0_fit - 2 * alpha_fit
interface_end = z0_fit + 2 * alpha_fit

# -----------------------------
# Generate random non-white colors
# -----------------------------
def random_color_nonwhite():
    # RGB values between 0.0 and 0.85 to avoid white/light colors
    return np.random.uniform(0.0, 0.85, size=3)

data_color = random_color_nonwhite()
fit_color = random_color_nonwhite()
start_color = random_color_nonwhite()
end_color = random_color_nonwhite()

# -----------------------------
# Plot results
# -----------------------------
plt.figure(figsize=(8, 6))

plt.scatter(
    z,
    rho_noisy,
    label='Data',
    s=10,
    color=data_color
)

plt.plot(
    z,
    tanh_profile(z, *popt),
    label='Fitted Profile',
    color=fit_color,
    linewidth=2
)

plt.axvline(
    interface_start,
    linestyle='--',
    color=start_color,
    label='Interface Start'
)

plt.axvline(
    interface_end,
    linestyle='--',
    color=end_color,
    label='Interface End'
)

plt.xlabel('z')
plt.ylabel('Density')
plt.title('Liquid–Gas Density Profile Fitting')
plt.legend()
plt.grid(True)

# Save high-resolution figure
plt.savefig('density_profile_fit.png', dpi=300, bbox_inches='tight')
plt.close()

print('Plot saved as density_profile_fit.png with unique colors')

