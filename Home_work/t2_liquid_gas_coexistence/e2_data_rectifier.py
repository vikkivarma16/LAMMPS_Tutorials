import numpy as np

def parse_lammps_chunk_data(filename):
    time_data = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        timestep = None
        i=0
        threshold =0
        for line in lines:
            
            parts = line.strip().split()
            
           
            if len(parts) == 2 and i == 0:
                timestep = int(parts[0])*0.005
                time_data[timestep] = []
                threshold = int (parts[1])
                i = i+1
               # print("time step is given as", timestep, threshold, parts)
                
            elif len(parts) == 2 and i <= threshold :
                chunk, count = map(int, parts)
                time_data[timestep].append((chunk, count))
                i=i+1
                #print("data for the first time is being recorded as: ", chunk, count)
                
                if ( i > threshold):
                    i = 0 
                
                
  
    return time_data
        
    
# Function to calculate average density per bin over all timesteps
def calculate_average_density(time_data, bin_volume, dx):
    """
    Calculate average particle density per bin across all timesteps.
    
    Parameters:
        time_data (dict): Dictionary with timesteps as keys and list of (bin_id, count) tuples as values.
        bin_volume (float): Volume of each bin.
        dx (float): Distance between bins.
        
    Returns:
        bin_positions (list): List of bin positions along the z-axis.
        densities (list): List of average densities per bin.
    """
    bin_sums = {}
    bin_counts = {}
    
    for timestep, data in time_data.items():
        for bin_id, count in data:
            if bin_id not in bin_sums:
                bin_sums[bin_id] = 0
                bin_counts[bin_id] = 0
            bin_sums[bin_id] += count
            bin_counts[bin_id] += 1
    
    bin_positions = []
    densities = []
    
    for bin_id in sorted(bin_sums.keys()):
        avg_count = bin_sums[bin_id] / bin_counts[bin_id]
        density = avg_count / bin_volume
        bin_positions.append(bin_id * dx)
        densities.append(density)
    
    return bin_positions, densities

# Save the results to a file
def save_density_profile(filename, bin_positions, densities):
    """
    Save bin positions and densities to a text file.
    
    Parameters:
        filename (str): Output filename.
        bin_positions (list): List of bin positions.
        densities (list): List of densities.
    """
    with open(filename, 'w') as f:
        for pos, dens in zip(bin_positions, densities):
            f.write(f'{pos} {dens}\n')

# Example usage
if __name__ == '__main__':
    
    filename = 'bin_particles.lammpstrj'
    
    xmin = 0
    xmax = 15
    ymin = 0
    ymax = 15
    zmin = 20
    zmax = 70
    total_volume = (xmax - xmin) * (ymax - ymin) * (zmax - zmin)
    
    relative_bin_size = 0.02*(zmax-zmin) 
    dx= relative_bin_size
    bin_volume = 0.02*total_volume   # Replace with actual bin volume
    
    
    time_data = parse_lammps_chunk_data(filename)
    bin_positions, densities = calculate_average_density(time_data, bin_volume, dx)
    
    
    half_length = len(bin_positions) // 2
    bin_positions_half = bin_positions[:half_length]
    densities_half = densities[:half_length]
    filename = "averaged_density_profile.txt"
    # Save to file
    with open(filename, 'w') as file:
        for pos, dens in zip(bin_positions_half, densities_half):
            file.write(f"{pos} {dens}\n")
    print(f"Density profile saved to averaged_density_profile.txt {filename}")
    
    

