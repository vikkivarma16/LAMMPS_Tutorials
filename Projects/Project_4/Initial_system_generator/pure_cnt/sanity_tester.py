import numpy as np
from collections import defaultdict

xyz_file = "cord_cnt.xyz"
topology_file = "cnt_full_topology.txt"
vtk_file = "low_dihedral_bonds.vtk"

# ----------------------------------
# Read coordinates (1-indexed)
# ----------------------------------
coords = []
with open(xyz_file, "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 3:
            coords.append(tuple(map(float, parts[:3])))

coords = {i + 1: c for i, c in enumerate(coords)}

# ----------------------------------
# Read bonds and dihedrals
# ----------------------------------
bonds = set()
dihedrals = []

section = None
with open(topology_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        lower = line.lower()

        if lower.startswith("bonds"):
            section = "bonds"
            continue
        elif lower.startswith("dihedrals"):
            section = "dihedrals"
            continue
        elif lower.startswith(("angles", "impropers", "summary")):
            section = None
            continue

        if not line[0].isdigit():
            continue

        parts = line.split()

        if section == "bonds":
            _, a1, a2 = map(int, parts[:3])
            bonds.add(tuple(sorted((a1, a2))))

        elif section == "dihedrals":
            _, A, B, C, D = map(int, parts[:5])
            dihedrals.append((A, B, C, D))

# ----------------------------------
# Count dihedrals per central bond
# ----------------------------------
dihedrals_per_bond = defaultdict(int)

for A, B, C, D in dihedrals:
    central = tuple(sorted((B, C)))
    dihedrals_per_bond[central] += 1

for b in bonds:
    dihedrals_per_bond.setdefault(b, 0)

# ----------------------------------
# Select bonds with < 4 dihedrals
# ----------------------------------
selected_bonds = [
    b for b, n in dihedrals_per_bond.items() if n < 4
]

selected_atoms = sorted(
    {a for b in selected_bonds for a in b}
)

atom_id_map = {aid: i for i, aid in enumerate(selected_atoms)}

# ----------------------------------
# Write VTK file
# ----------------------------------
with open(vtk_file, "w") as f:
    f.write("# vtk DataFile Version 3.0\n")
    f.write("CNT bonds with <4 dihedrals\n")
    f.write("ASCII\n")
    f.write("DATASET POLYDATA\n")

    # Points
    f.write(f"POINTS {len(selected_atoms)} float\n")
    for aid in selected_atoms:
        x, y, z = coords[aid]
        f.write(f"{x} {y} {z}\n")

    # Lines (bonds)
    f.write(f"\nLINES {len(selected_bonds)} {len(selected_bonds) * 3}\n")
    for a, b in selected_bonds:
        f.write(f"2 {atom_id_map[a]} {atom_id_map[b]}\n")

    # Scalar data for coloring
    f.write(f"\nCELL_DATA {len(selected_bonds)}\n")
    f.write("SCALARS dihedrals_per_bond int 1\n")
    f.write("LOOKUP_TABLE default\n")
    for b in selected_bonds:
        f.write(f"{dihedrals_per_bond[b]}\n")

print(f"VTK file written: {vtk_file}")
print(f"Selected bonds  : {len(selected_bonds)}")
print(f"Selected atoms  : {len(selected_atoms)}")

