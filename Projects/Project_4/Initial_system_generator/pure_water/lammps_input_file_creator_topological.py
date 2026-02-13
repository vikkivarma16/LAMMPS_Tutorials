import datetime

# -----------------------------
# File paths
data_file = "cord_water.txt"   # <--- NEW INPUT FILE
topology_file = "topology.txt"
output_file = "input_water_with_topology.txt"
# -----------------------------

# Read coordinates & attributes from TXT file
coordinates = []
atom_types_list = []
mol_ids = []

with open(data_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split()

        # Format:
        # index   x   y   z   element   atom_type   element_id   mol_id
        if len(parts) < 8:
            continue

        idx = int(parts[0])
        x, y, z = map(float, parts[1:4])
        element = parts[4]
        atom_type = int(parts[5])
        element_id = int(parts[6])
        mol_id = int(parts[7])

        coordinates.append((x, y, z))
        atom_types_list.append(atom_type)
        mol_ids.append(mol_id)

num_atoms = len(coordinates)

# -----------------------------
# Read topology file as before
# -----------------------------
bonds = []
angles = []
dihedrals = []
impropers = []
body = {}

section = None
with open(topology_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line or not line or line.startswith("#") or line.lower().startswith("summary"):
            continue

        if line.lower().startswith("bonds"):
            section = "bonds"
            continue
        elif line.lower().startswith("angles"):
            section = "angles"
            continue
        elif line.lower().startswith("dihedrals"):
            section = "dihedrals"
            continue
        elif line.lower().startswith("impropers"):
            section = "impropers"
            continue

        parts = line.split()

        if section == "bonds":
            _, a1, a2, bidx = map(int, parts[:4])
            bonds.append((a1, a2))
            body[a1] = bidx
            body[a2] = bidx

        elif section == "angles":
            _, A, B, C, bidx = map(int, parts[:5])
            angles.append((A, B, C))
            body[B] = bidx

        elif section == "dihedrals":
            _, A, B, C, D, bidx = map(int, parts[:6])
            dihedrals.append((A, B, C, D))
            body[B] = bidx

        elif section == "impropers":
            _, n1, center, n2, n3, bidx = map(int, parts[:6])
            impropers.append((center, n1, n2, n3))
            body[center] = bidx

# Counts
num_bonds = len(bonds)
num_angles = len(angles)
num_dihedrals = len(dihedrals)
num_impropers = len(impropers)

# Example box
xlo, xhi = -60.0, 60.0
ylo, yhi = -40.0, 40.0
zlo, zhi = -40.0, 40.0

# Determine number of atom types from file
atom_types = max(atom_types_list)
bond_types = 1
angle_types = 1
dihedral_types = 1
improper_types = 1

# -----------------------------
# Write LAMMPS data file
# -----------------------------
with open(output_file, "w") as f:
    f.write(f"LAMMPS data file. Generated {datetime.datetime.now()}\n")
    f.write(f"{num_atoms} atoms\n")
    f.write(f"{num_bonds} bonds\n")
    f.write(f"{num_angles} angles\n")
    f.write(f"{num_dihedrals} dihedrals\n")
    f.write(f"{num_impropers} impropers\n")
    f.write(f"{atom_types} atom types\n")
    f.write(f"{bond_types} bond types\n")
    f.write(f"{angle_types} angle types\n")
    f.write(f"{dihedral_types} dihedral types\n")
    f.write(f"{improper_types} improper types\n")
    f.write(f"{xlo} {xhi} xlo xhi\n")
    f.write(f"{ylo} {yhi} ylo yhi\n")
    f.write(f"{zlo} {zhi} zlo zhi\n\n")

    # Masses (placeholder)
    f.write("Masses\n\n")
    for t in range(1, atom_types + 1):
        f.write(f"{t} 12.0107\n")
    f.write("\n")

    # Atoms section
    f.write("Atoms # molecular\n\n")
    for i, ((x, y, z), atype, mol) in enumerate(zip(coordinates, atom_types_list, mol_ids), 1):
        f.write(f"{i} {mol} {atype}  {x:.6f} {y:.6f} {z:.6f}\n")
    f.write("\n")

    # Bonds
    f.write("Bonds\n\n")
    for i, (a1, a2) in enumerate(bonds, 1):
        f.write(f"{i} 1 {a1} {a2}\n")
    f.write("\n")

    # Angles
    f.write("Angles\n\n")
    for i, (A, B, C) in enumerate(angles, 1):
        f.write(f"{i} 1 {A} {B} {C}\n")
    f.write("\n")

    # Dihedrals
    f.write("Dihedrals\n\n")
    for i, (A, B, C, D) in enumerate(dihedrals, 1):
        f.write(f"{i} 1 {A} {B} {C} {D}\n")
    f.write("\n")

    # Impropers
    f.write("Impropers\n\n")
    for i, (center, n1, n2, n3) in enumerate(impropers, 1):
        f.write(f"{i} 1 {center} {n1} {n2} {n3}\n")

print(f"LAMMPS input file '{output_file}' generated successfully!")

