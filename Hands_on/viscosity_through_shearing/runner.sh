#!/bin/bash
#SBATCH --job-name=Brownian-dynamics
#SBATCH --account=project_2016841
#SBATCH --partition=test
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=2  
#SBATCH --mem=0
#SBATCH --mail-type=BEGIN,END


# Load modules
module --force purge
module load gcc/11.2.0 openmpi/4.1.2 cmake/3.31.9

# OpenMP environment variables
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PROC_BIND=close
export OMP_PLACES=cores

# Run LAMMPS with KOKKOS CPU backend
srun --cpu-bind=cores --distribution=block:block /projappl/project_2016841/lammps-kokkos-build/bin/lmp -in lj_viscosity_shearing.in   #CHANGE THE NAME OF THE LAMMPS FILE
