import numpy as np
import matplotlib.pyplot as plt

# Define the constant 'a'
a = 25  # Modify this value as needed

# Read data from the file
filename = "e1_rho_vs_pressure.txt"
data = np.loadtxt(filename)

# Ensure the file has two columns: x and y
if data.shape[1] != 2:
    raise ValueError("The input file must have exactly two columns for x and y values.")

x = data[:, 0]  # First column: x values
y = data[:, 1]  # Second column: y values

# Compute the desired expression
result = (y - x) / (a * x**2)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(x, result, marker='o', linestyle='-', color='b', label=f'(y - x) / (a * x^2), a={a}')
plt.xlabel('Density')
plt.ylabel('P - rho/ A.rho^2')
plt.title('P - rho/ A.rho^2 vs Density ')
plt.legend()
plt.grid()

# Save the plot to a file (change the file name and format as needed)
plt.savefig("rho_vs_p_r.png", dpi=300)  # Save as a high-resolution PNG

# Close the plot to avoid it being displayed
plt.close()

