import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# -----------------------------
# Parameters
# -----------------------------
# Water-only plot
n_water = 200
water_radius = 0.1
box_size = 10

# Colloid + water plot (zoomed out)
zoom_factor = 10
n_colloid = 10
colloid_radius = 1.0
water_scale_factor = 1 / zoom_factor

# -----------------------------
# Generate positions
# -----------------------------
water_x = np.random.uniform(0, box_size, n_water)
water_y = np.random.uniform(0, box_size, n_water)

colloid_box_size = box_size * zoom_factor
colloid_x = np.random.uniform(0, colloid_box_size, n_colloid)
colloid_y = np.random.uniform(0, colloid_box_size, n_colloid)

n_water_zoom = int((n_water / box_size**2) * colloid_box_size**2)
water_x_zoom = np.random.uniform(0, colloid_box_size, n_water_zoom)
water_y_zoom = np.random.uniform(0, colloid_box_size, n_water_zoom)

# -----------------------------
# Plot 1: Water only
# -----------------------------
plt.figure(figsize=(6, 6))
plt.scatter(water_x, water_y, s=(water_radius * 1000), c='blue', alpha=0.6)
plt.title("Water molecules (molecular scale)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.tight_layout()
plt.savefig("water_only.png", dpi=600)
plt.close()

# -----------------------------
# Plot 2: Colloids + water (zoomed out)
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 6))

# Colloids
ax.scatter(colloid_x, colloid_y,
           s=(colloid_radius * 1000),
           c='red', alpha=0.8, label='Colloids')

# Water
ax.scatter(water_x_zoom, water_y_zoom,
           s=(water_radius * 1000 * water_scale_factor * 0.5),
           c='blue', alpha=0.5, label='Water')

# ---- Black 10x10 square (scale indicator) ----

# ---- Black 10x10 square (outline only, no fill) ----
scale_square = Rectangle(
    (0, 0), 10, 10,
    fill=False,
    edgecolor='black',
    linewidth=2,
    zorder=10
)
ax.add_patch(scale_square)


ax.set_title("Colloids in water (zoomed out, same density)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect('equal')
ax.legend()
plt.tight_layout()
plt.savefig("colloids_in_water_zoomed.png", dpi=600)
plt.close()

