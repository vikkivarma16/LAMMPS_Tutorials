import matplotlib.pyplot as plt
import numpy as np

filename = "velocity_profile.txt"

# ---- Set timestep threshold ----
timestep_threshold = 2000000    # only use data from timesteps > this value
# --------------------------------

vx_list, vy_list, vz_list = [], [], []

with open(filename, "r") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()

    if line.startswith("#") or line == "":
        i += 1
        continue

    parts = line.split()

    # timestep header: "1000 20"
    if len(parts) == 2:
        timestep, nrows = int(parts[0]), int(parts[1])
        i += 1

        # ****** Skip blocks before threshold ******
        if timestep <= timestep_threshold:
            i += nrows  # skip the block of rows
            continue
        # ******************************************

        # Keep velocity data from selected timesteps
        for _ in range(nrows):
            row = lines[i].strip().split()
            if len(row) == 4:
                _, vx, vy, vz = row
                vx_list.append(float(vx))
                vy_list.append(float(vy))
                vz_list.append(float(vz))
            i += 1
    else:
        i += 1

# reshape into (num_timesteps_after_threshold, nbins)
vx_arr = np.array(vx_list).reshape(-1, 20)
vy_arr = np.array(vy_list).reshape(-1, 20)
vz_arr = np.array(vz_list).reshape(-1, 20)

# average over selected timesteps
vx_avg = vx_arr.mean(axis=0)
vy_avg = vy_arr.mean(axis=0)
vz_avg = vz_arr.mean(axis=0)

bins = np.arange(1, 21)

plt.figure(figsize=(8, 5))
plt.plot(bins, vx_avg, label="Vx")
plt.plot(bins, vy_avg, label="Vy")
plt.plot(bins, vz_avg, label="Vz")

plt.xlabel("Bin Number")
plt.ylabel("Average Velocity")
plt.title(f"Average Velocity Profile (timesteps > {timestep_threshold})")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plot.png", dpi=600)

