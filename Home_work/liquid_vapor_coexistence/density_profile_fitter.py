import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the tangent hyperbolic mean-field function for fitting
def tanh_profile(z, rho_l, rho_g, z0, alpha):
    """
    Tanh function describing the liquid-gas density profile.
    
    Parameters:
        z (float or array): Spatial coordinate.
        rho_l (float): Liquid density.
        rho_g (float): Gas density.
        z0 (float): Interface position.
        alpha (float): Interfacial width parameter.
        
    Returns:
        float or array: Density profile at position z.
    """
    return 0.5 * (rho_l + rho_g) + 0.5 * (rho_l - rho_g) * np.tanh((z - z0) / alpha)

# Load data from file (replace 'data.txt' with your actual file)
# Data format: First column -> z, Second column -> density
z, rho_noisy = np.loadtxt('averaged_density_profile.txt', unpack=True)

# Estimate initial parameters from data
rho_l_init = np.max(rho_noisy)
rho_g_init = np.min(rho_noisy)
z0_init = z[np.argmax(np.abs(np.gradient(rho_noisy)))]
alpha_init = (np.max(z) - np.min(z)) / 10

# Fit the density profile to the tangent hyperbolic function
popt, pcov = curve_fit(tanh_profile, z, rho_noisy, p0=[rho_l_init, rho_g_init, z0_init, alpha_init])

# Extract fitted parameters
rho_l_fit, rho_g_fit, z0_fit, alpha_fit = popt

print(f"Fitted Liquid Density: {rho_l_fit}")
print(f"Fitted Gas Density: {rho_g_fit}")
print(f"Fitted Interface Position (z0): {z0_fit}")
print(f"Fitted Interface Width (alpha): {alpha_fit}")

# Calculate interface boundaries (e.g., z0 ± 2*alpha)
interface_start = z0_fit - 2 * alpha_fit
interface_end = z0_fit + 2 * alpha_fit

# Plot the results and export as high-resolution image
plt.figure(figsize=(8, 6))
plt.scatter(z, rho_noisy, label='Data', s=10, color='gray')
plt.plot(z, tanh_profile(z, *popt), label='Fitted Profile', color='red')
plt.axvline(interface_start, color='blue', linestyle='--', label='Interface Start')
plt.axvline(interface_end, color='green', linestyle='--', label='Interface End')
plt.xlabel('z')
plt.ylabel('Density')
plt.legend()
plt.title('Liquid-Gas Density Profile Fitting')
plt.savefig('density_profile_fit.png', dpi=300)
plt.close()

print('Plot saved as density_profile_fit.png')

