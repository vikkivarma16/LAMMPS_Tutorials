#!/bin/bash

# Ensure the script is run as root

# Update and upgrade the package list
echo "Updating package list..."
sudo apt update
sudo apt upgrade -y

# Install Python3 and pip
echo "Installing Python3 and pip..."
sudo apt install -y python3 python3-pip

# Install Python libraries
echo "Installing Python libraries: matplotlib, scipy, numpy, tqdm..."
pip3 install matplotlib scipy numpy tqdm

# Install additional tools
echo "Installing additional tools: vi, gnuplot..."
pip3 install -y vim gnuplot

# Install LAMMPS
echo "Installing LAMMPS..."
sudo apt install -y lammps

# Confirm installation
echo "Verifying installations..."
python3 --version
pip3 --version
vim --version
gnuplot --version
lmp -help | head -n 5

sudo apt install python3-scipy

sudo apt install python3-matplotlib 

sudo apt install python3-numpy

# Success message
echo "All requested packages and tools have been installed successfully."

