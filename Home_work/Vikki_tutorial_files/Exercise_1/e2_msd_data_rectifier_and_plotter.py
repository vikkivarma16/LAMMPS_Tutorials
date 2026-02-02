import csv
import numpy as np
import matplotlib.pyplot as plt

# Input and output file names
input_file = "msd.dat"
output_file = "msd_processed.txt"

# Constants
time_step_m = 0.005
dimensions = 3  # Number of dimensions for the MSD calculation

# Open the input and output files
with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    # Write header for the output CSV
    lines = infile.readlines()
    timestep = None
    msd_x, msd_y, msd_z, msd_total = None, None, None, None

    for line in lines:
        # Skip comments
        if line.startswith("#"):
            continue
        
        row_index, msd_value = map(float, line.split())
        
        if msd_value == 4.0:
            timestep = row_index 
        else:
            # Assign MSD components based on the row index
            if int(row_index) == 1:
                msd_x = msd_value
            elif int(row_index) == 2:
                msd_y = msd_value
            elif int(row_index) == 3:
                msd_z = msd_value
            elif int(row_index) == 4:
                msd_total = msd_value
                # Write the complete row for this timestep
                outfile.write(f"{timestep * time_step_m} {msd_x} {msd_y} {msd_z} {msd_total}\n")

# Read the processed data
data = np.loadtxt(output_file)
x = data[:, 0][1:]  # Remove the first element from x
y = data[:, 4][1:]  # Remove the first element from y

# Calculate the diffusivity (D) from MSD data
delta_msd = y[-1] - y[0]  # Change in MSD
delta_t = x[-1] - x[0]    # Change in time

ratio = delta_msd/delta_t
D = delta_msd / (2 * dimensions * delta_t)
print(f"Calculated Diffusivity (D) in DPD Unit: {D:.4f}\n")
print(f"Total time in DPD simulation time unit: {delta_t:.4f}\n")
print(f"MSD in DPD simulation length unit: {delta_msd:.4f}")



# Define the function f(x) = D * x
f_x = ratio * x

# Plot the data
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label="MSD total")
plt.plot(x, f_x, linestyle='--', color='r', label=f"f(x) = 6Dt, D={D:.4f}")

# Set logarithmic scale
plt.xscale('log')
plt.yscale('log')

# Add labels and title
plt.xlabel('Time (log scale)')
plt.ylabel('MSD (log scale)')
plt.title('MSD vs Time')

# Add a legend
plt.legend()

# Add grid
plt.grid(True)

# Save the plot as a high-resolution image
plt.savefig("msd_vs_time.png", dpi=300)

# Close the plot
plt.close()

