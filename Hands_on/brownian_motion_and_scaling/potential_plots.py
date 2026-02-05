import numpy as np
import matplotlib.pyplot as plt

# =============================
# Parameters from LAMMPS
# =============================

# LJ/cut (1–1)
epsilon_lj = 0.01
sigma_lj = 1.3
r_cut_lj = 2.0

# Cosine/squared (2–2)
epsilon_cs = 8.0
sigma_cs = 0.30
r_cut_cs = 0.35

# =============================
# Distance arrays
# =============================

r_lj = np.linspace(0.9, r_cut_lj, 600)
r_cs = np.linspace(0.25, 0.40, 800)

# =============================
# LJ/cut (shifted to zero at cutoff)
# =============================

def lj_cut(r, epsilon, sigma, rcut):
    lj = 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)
    lj_shift = 4 * epsilon * ((sigma / rcut)**12 - (sigma / rcut)**6)
    return lj 

U_lj = lj_cut(r_lj, epsilon_lj, sigma_lj, r_cut_lj)

# =============================
# Cosine-squared (LAMMPS definition)
# =============================

U_cs = np.zeros_like(r_cs)

# r < sigma
mask1 = r_cs < sigma_cs
U_cs[mask1] = -epsilon_cs

# sigma <= r < r_cut
mask2 = (r_cs >= sigma_cs) & (r_cs < r_cut_cs)
U_cs[mask2] = -epsilon_cs * np.cos(
    np.pi * (r_cs[mask2] - sigma_cs) / (2 * (r_cut_cs - sigma_cs))
)**2

# r >= r_cut → already zero

# =============================
# Plotting (2 × 1)
# =============================

fig, axes = plt.subplots(2, 1, figsize=(6, 8))

title_fs = 16
label_fs = 16
tick_fs = 16

# LJ plot (first)
axes[0].plot(r_lj, U_lj, linewidth =  3)
axes[0].set_title("LJ/Cut Potential (1–1)", fontsize=title_fs)
axes[0].set_xlabel("r", fontsize=label_fs)
axes[0].set_ylabel("U(r)", fontsize=label_fs)
axes[0].axhline(0, linestyle="--", linewidth=0.8)
axes[0].tick_params(axis="both", labelsize=tick_fs)
axes[0].set_xticks ([0, 1, 2, 3])

# Cosine-squared plot (second)
axes[1].plot(r_cs, U_cs, linewidth =  3)
axes[1].set_title("Cosine-Squared Potential (2–2)",
                  fontsize=title_fs)
axes[1].set_xlabel("r", fontsize=label_fs)
axes[1].set_ylabel("U(r)", fontsize=label_fs)
axes[1].axvline(sigma_cs, linestyle=":", linewidth=0.8)
axes[1].axvline(r_cut_cs, linestyle=":", linewidth=0.8)
axes[1].tick_params(axis="both", labelsize=tick_fs)
axes[1].set_xticks ([0.2, 0.3, 0.4])


plt.tight_layout()

# =============================
# Save figure
# =============================
plt.savefig(
    "lammps_lj_and_cosine_squared_exact.png",
    dpi=600,
    bbox_inches="tight"
)

