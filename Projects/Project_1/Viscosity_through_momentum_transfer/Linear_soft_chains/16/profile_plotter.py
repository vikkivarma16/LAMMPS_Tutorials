import matplotlib.pyplot as plt
import numpy as np

filename = "velocity_profile.txt"

vx_list = []
bins_list = []

with open(filename, "r") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
    
    # skip comment or empty lines
    if line.startswith("#") or line == "":
        i += 1
        continue

    parts = line.split()

    # timestep header: "51000 20 2457.0"
    if len(parts) == 3:
        timestep, nrows, _ = int(parts[0]), int(parts[1]), float(parts[2])
        i += 1
        
        # read the nrows following velocity entries
        for _ in range(nrows):
            row = lines[i].strip().split()
            if len(row) == 4:  # format: chunk bin Ncount vx
                _, bin_val, _, vx = row
                vx_list.append(float(vx))
                bins_list.append(float(bin_val))
            i += 1
    else:
        i += 1

# determine number of bins from first timestep
num_bins = int(len(vx_list) / (len(vx_list) // nrows))

# reshape based on number of bins
vx_arr = np.array(vx_list).reshape(-1, num_bins)
bins = np.array(bins_list[:num_bins])

# average over timesteps
vx_avg = vx_arr.mean(axis=0)

plt.figure(figsize=(8, 5))
plt.plot(bins, vx_avg, marker='o', linestyle='-', color='r', label="Vx")

plt.xlabel("Bin (Coord1)")
plt.ylabel("Average Velocity vx")
plt.title("Time-Averaged Velocity Profile")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("velocity_profile_avg.png", dpi=600)
