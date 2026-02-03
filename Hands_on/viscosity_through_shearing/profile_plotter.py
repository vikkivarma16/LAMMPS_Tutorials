import numpy as np
import matplotlib.pyplot as plt

# =====================================
# User parameters
# =====================================
vel_file = "velocity_profile.txt"
pxy_file = "pxy.dat"

x_min, x_max = -3.0, 23.0
ignore_edges = True   # ignore first and last bins

# =====================================
# 1. LOAD VELOCITY PROFILE
# =====================================
vy_list = []

with open(vel_file, "r") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()

    if line.startswith("#") or line == "":
        i += 1
        continue

    parts = line.split()
    if len(parts) == 2:
        timestep, nbins = int(parts[0]), int(parts[1])
        i += 1

        for _ in range(nbins):
            row = lines[i].split()
            vy_list.append(float(row[2]))  # vy
            i += 1
    else:
        i += 1

vy_arr = np.array(vy_list).reshape(-1, nbins)
vy_avg = vy_arr.mean(axis=0)

# Build x-axis
x = np.linspace(x_min, x_max, nbins)
dx = x[1] - x[0]

if ignore_edges:
    x_use = x[1:-1]
    vy_use = vy_avg[1:-1]
else:
    x_use = x
    vy_use = vy_avg

# =====================================
# 2. LINEAR FIT TO VELOCITY PROFILE
# =====================================
# vy = a x + b
coeffs = np.polyfit(x_use, vy_use, 1)
slope, intercept = coeffs

vy_fit = slope * x_use + intercept
shear_rate = slope   # dv_y/dx from fit

# Numerical gradient (still useful for visualization)
dvy_dx = np.gradient(vy_use, dx)

# =====================================
# 3. LOAD PXY DATA
# =====================================
pxy = []

with open(pxy_file, "r") as f:
    for line in f:
        if line.startswith("#") or line.strip() == "":
            continue
        _, val = line.split()
        pxy.append(float(val))

pxy = np.array(pxy)
pxy_avg = pxy.mean()

# =====================================
# 4. COMPUTE VISCOSITY
# =====================================
viscosity = -pxy_avg / shear_rate

# =====================================
# 5. OUTPUT RESULTS
# =====================================
print("===================================")
print(f"Fitted shear rate dv_y/dx = {shear_rate:.6e}")
print(f"Average <P_xy>            = {pxy_avg:.6e}")
print(f"Viscosity eta             = {viscosity:.6e}")
print("===================================")

# =====================================
# 6. PLOTS
# =====================================
plt.figure(figsize=(12, 4))

# --- Velocity profile + fit ---
plt.subplot(1, 3, 1)
plt.plot(x_use, vy_use, 'o', label="Data")
plt.plot(x_use, vy_fit, '-', linewidth=2,
         label=rf"Fit: $dv_y/dx = {shear_rate:.3e}$")
plt.xlabel("x")
plt.ylabel(r"$v_y$")
plt.title("Velocity profile")
plt.legend()

# --- Velocity gradient ---
plt.subplot(1, 3, 2)
plt.plot(x_use, dvy_dx, 'o-', alpha=0.7)
plt.axhline(shear_rate, linestyle="--",
            label=rf"Fit slope = {shear_rate:.3e}")
plt.xlabel("x")
plt.ylabel(r"$dv_y/dx$")
plt.title("Velocity gradient")
plt.legend()

# --- Pxy time series ---
plt.subplot(1, 3, 3)
plt.plot(pxy, alpha=0.7)
plt.axhline(pxy_avg, linestyle="--",
            label=rf"$\langle P_{{xy}} \rangle = {pxy_avg:.3e}$")
plt.xlabel("Sample index")
plt.ylabel(r"$P_{xy}$")
plt.title("Shear stress")
plt.legend()

plt.tight_layout()
plt.savefig("viscosity_analysis.png", dpi=600)

