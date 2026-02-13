import os
import re
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Configuration
# --------------------------------------------------
folder = "cell_bin"
file_pattern = re.compile(r"cell_efficiency_histogram_(\d+)\.txt")

# --------------------------------------------------
# Read histogram files
# --------------------------------------------------
histograms = {}  # iteration -> (bin_starts, cell_counts)

for fname in os.listdir(folder):
    match = file_pattern.match(fname)
    if not match:
        continue

    iteration = int(match.group(1))
    path = os.path.join(folder, fname)

    # skip commented lines
    data = np.loadtxt(path, comments="#")
    bin_starts = data[:, 0].astype(int)
    counts = data[:, 2]

    histograms[iteration] = (bin_starts, counts)

if not histograms:
    raise RuntimeError("No histogram files found in cell_bin/")

# Sort by iteration
iterations = sorted(histograms.keys())

# --------------------------------------------------
# Plot 1: Overlaid histograms
# --------------------------------------------------
plt.figure(figsize=(8, 5))

for it in iterations:
    bins, counts = histograms[it]
    plt.plot(bins, counts, marker="o", label=f"iter {it}")

plt.xlabel("Bin start (particles per cell)")
plt.ylabel("Number of cells")
plt.title("Cell occupancy histogram (time evolution)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# Plot 2: Heatmap (bin vs iteration)
# --------------------------------------------------
# Find maximum number of bins across iterations
max_bins = max(len(histograms[it][0]) for it in iterations)
hist_matrix = np.zeros((len(iterations), max_bins))

for ti, it in enumerate(iterations):
    bins, counts = histograms[it]
    for bi, c in enumerate(counts):
        hist_matrix[ti, bi] = c

plt.figure(figsize=(8, 5))
im = plt.imshow(
    hist_matrix,
    aspect="auto",
    origin="lower",
    interpolation="nearest"
)
plt.colorbar(im, label="Number of cells")
plt.xlabel("Bin index (from bin_start column)")
plt.ylabel("Iteration")
plt.yticks(range(len(iterations)), iterations)
plt.title("Cell occupancy histogram evolution")
plt.tight_layout()
plt.show()

