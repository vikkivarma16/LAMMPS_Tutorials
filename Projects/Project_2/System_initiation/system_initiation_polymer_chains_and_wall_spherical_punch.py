# periodic_object_creator/an_example_assignment
import math
from math import sin, cos, tan, asin, acos, atan



from periodic_object_creator.assign_mol_id_mod import assign_group_ids
from periodic_object_creator.export_bond_topology_mod import  build_topology
from periodic_object_creator.export_coordinate_particle_mod import export_xyz
from periodic_object_creator.filter_broken_mol_mod import filter_broken_group
from periodic_object_creator.so_cm_calculator_mod import cm_calculator
from periodic_object_creator.so_elements_picker_mod import elements_picker
from periodic_object_creator.so_inverter_mod import inverter
from periodic_object_creator.so_overlap_remover_mod import  overlap_remover
from periodic_object_creator.so_overlap_eliminator_mod import overlap_eliminator
from periodic_object_creator.so_random_translator_mod import randomize_positions
from periodic_object_creator.so_reflector_mod import reflector
from periodic_object_creator.so_replicator_mod import replicator
from periodic_object_creator.so_unwrapper_mod import periodic_unwrapper
from periodic_object_creator.so_rotator_mod import rotator
from periodic_object_creator.so_scissor_mod import scissor
from periodic_object_creator.so_translator_mod import translator
from periodic_object_creator.so_wrapper_cylindrical_mod import wrapper_cylindrical
from periodic_object_creator.so_wrapper_spherical_mod import wrapper_spherical
from periodic_object_creator.vtk_particle_mod import particle_vis
from periodic_object_creator.so_wrapper_mod import periodic_wrapper
from periodic_object_creator.export_object_size_mod import get_object_size
                                    


#def assign_group_ids(obj, group_size=3, start_id=1, id_index_in_element=None):
#def export_xyz (cnt, "cord_cnt"):
#def filter_broken_group(remaining_water_lattic, group_size, group_id_indices ):
#def inverter(input_object, inversion_point):
#def overlap_remover(input_object, molid_idx, particle_idx, mol_type_idx, particle_type_idx, sigma_matrix, moving_mol_id, box, cell_size, iter_max, translation_step, rotation_step, max_particles_per_cell=64, grid_shifting_rate=100000):
#def overlap_eliminator(input_object_1, input_object_2, delete_from='obj1', tolerance=1e-6):
#def particle_vis(input_data_ps, filename):
#def picker(input_object, indices):
#def reflector(input_object, plane_normal, plane_location):
#def replicator(input_object):
#def rotator(input_object, ro_axis_orien, ro_axis_posi, ro_degree):
#def scissor(input_object, plane_origin, plane_normal, keep_side="negative"):
#def translator(input_object, tvector):
#def wrapper_cylindrical(input_object, cylinder_radius, object_size):
#def wrapper_spherical(input_object, sphere_radius, object_size):
#def periodic_unwrapper(object, box, mol_id_index):



# Filling up water molecules.

basis = [[0.0000000, 0.000000,  0.00000, "s", 1, 1]]

box_size =  [15, 15, 3]
particle_size = 1.0
v =  particle_size**3 * acos(-1)/6
phi = .65
a = (4*v/phi)**(1/3) 



unit_cell = []
unit_cell.extend(basis)

old_object = []
old_object.extend(basis)

tvector =  [0.0, a/(2), a/(2)]
new_object_1  =  translator(old_object, tvector)

unit_cell.extend (new_object_1)

tvector =  [a/(2), 0.0, a/(2)]
new_object_2  =  translator(basis, tvector)
unit_cell.extend (new_object_2)

tvector =  [a/(2), a/(2), 0.0]
new_object_3  =  translator(basis, tvector)
unit_cell.extend (new_object_3)





object_1 =  unit_cell

Nx = 10
Ny = 10
Nz = 3



basis_object_1 = []
tvector =  [a, 0.0, 0.0]
old_object  = []
old_object.extend(object_1)
basis_object_1.extend(old_object)
for i in range(Nx-1):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_1.extend(old_object)
    

basis_object_2 = []
tvector =  [0.0, a, 0.0]
old_object  = []
old_object.extend(basis_object_1)
basis_object_2.extend(old_object)
for i in range(Ny-1):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_2.extend(old_object)


basis_object_3 = []
tvector =  [0.0, 0.0, a]
old_object  = []
old_object.extend(basis_object_2)
basis_object_3.extend(old_object)
for i in range(Nz):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_3.extend(old_object)


input_object_1 = basis_object_3





temp =   [[0.0000000, 0.000000,  0.00000, "w", 1, 1]]
tvector  =  [Nx*a/2, Ny*a/2, Nz*a/2]
input_object_2 = translator(temp, tvector)


result_a, result_b = overlap_eliminator(input_object_1, input_object_2, delete_from='input_object_1', tolerance=3*a)



slab = []
slab.extend (result_a)


current_id = 1
group_size = 1 #polymer_size
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(slab, group_size, current_id, id_index)   
basis_object_3 = []
basis_object_3.extend( new_obj ) 


current_id = 1
group_size = 1
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_3, group_size, current_id, id_index)   
basis_object_4 = []
basis_object_4.extend(new_obj) 

t_vector =  [0.0, 0.0, 1.3*Nx*a]

basis_object_5 = translator (basis_object_4, t_vector)

slab = []
slab.extend (basis_object_5)

















basis_2 =  [[0.0000000, 0.000000,  0.00000, "p", 2, 2]]
polymer_size =  8

basis_object_1 = []
tvector = [1, 0, 0]
old_object  = []
old_object.extend(basis_2)
basis_object_1.extend(old_object)
for i in range(polymer_size-1):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_1.extend(old_object)
    

number_of_polymers  =  10
box  = [Nx*a, Nx*a, 1.2*Nx*a]


basis_object_2 =  []
for i in range(number_of_polymers):
    basis_object_2.extend(basis_object_1)
    
    

current_id = len(result_a) +1
group_size = 1 #polymer_size
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_2, group_size, current_id, id_index)   
basis_object_3 = []
basis_object_3.extend( new_obj ) 


current_id = len(result_a) +1
group_size = polymer_size
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_3, group_size, current_id, id_index)   
basis_object_4 = []
basis_object_4.extend( new_obj ) 



random_object =  randomize_positions (basis_object_4, idx  =  7,  box  = box,  seed=3840983, rotation =  False, periodic=False ,max_trials=10000)


id_body_index = 7
new = random_object #periodic_unwrapper (random_object, box, id_body_index)


polymers = []
polymers.extend(new)
#polymers.extend(basis_object_6)
















basis_3 =  [[0.0000000, 0.000000,  0.00000, "w", 3, 3]]

phi  =  0.38

Np  =  phi * box[0]*box[1]*box[2]/v
Np = int (Np - polymer_size*number_of_polymers)



basis_object_1 = []
tvector =  [0.0, 0.0, 0.0]
old_object  =  []
old_object.extend(basis_3)
basis_object_1.extend(old_object)
for i in range(Np-1):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_1.extend(old_object)


current_id = len(result_a) + len (polymers) +1
group_size = 1 #polymer_size
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_1, group_size, current_id, id_index)   
basis_object_3 = []
basis_object_3.extend( new_obj ) 


current_id = len(result_a) + number_of_polymers +1
group_size = 1
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_3, group_size, current_id, id_index)   
basis_object_4 = []
basis_object_4.extend( new_obj ) 



random_object =  randomize_positions (basis_object_4, idx  =  7,  box  = box,  seed=3840983, rotation =  False, periodic=False ,max_trials=10000)

id_body_index = 7

new = random_object #periodic_unwrapper (random_object, box, id_body_index)
basis_object_5 = []
basis_object_5.extend(new)







basis_4 =  [[0.0000000, 0.000000,  0.00000, "a", 4, 4]]

phi  =  0.38

Np  =  phi * box[0]*box[1]*box[2]/v
Np = int (Np - polymer_size*number_of_polymers)



basis_object_1 = []
tvector =  [0.0, 0.0, 0.0]
old_object  =  []
old_object.extend(basis_4)
basis_object_1.extend(old_object)
for i in range(Np-1):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_1.extend(old_object)


current_id = len(result_a) + len (polymers) +1 + len (basis_object_5)
group_size = 1 #polymer_size
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_1, group_size, current_id, id_index)   
basis_object_3 = []
basis_object_3.extend( new_obj ) 


current_id = len(result_a) + number_of_polymers + 1 +len (basis_object_5)
group_size = 1
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_3, group_size, current_id, id_index)   
basis_object_4 = []
basis_object_4.extend( new_obj ) 



random_object =  randomize_positions (basis_object_4, idx  =  7,  box  = box,  seed=3840983, rotation =  False,  periodic=False ,max_trials=10000)

id_body_index = 7

new = random_object #periodic_unwrapper (random_object, box, id_body_index)



t_vector =  [0.0, 0.0,   1.4*Nx*a + 1.2*Nz*a] 


basis_object_6  =  translator(new, t_vector)

fluid = []
fluid.extend(basis_object_5)
fluid.extend(basis_object_6)








# slab 2 for the particle's orientation


basis = [[0.0000000, 0.000000,  0.00000, "s", 1, 1]]


unit_cell = []
unit_cell.extend(basis)

old_object = []
old_object.extend(basis)

tvector =  [0.0, a/(2), a/(2)]
new_object_1  =  translator(old_object, tvector)

unit_cell.extend (new_object_1)

tvector =  [a/(2), 0.0, a/(2)]
new_object_2  =  translator(basis, tvector)
unit_cell.extend (new_object_2)

tvector =  [a/(2), a/(2), 0.0]
new_object_3  =  translator(basis, tvector)
unit_cell.extend (new_object_3)





object_1 =  unit_cell

Nx = 10
Ny = 10
Nz = 3



basis_object_1 = []
tvector =  [a, 0.0, 0.0]
old_object  = []
old_object.extend(object_1)
basis_object_1.extend(old_object)
for i in range(Nx-1):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_1.extend(old_object)
    

basis_object_2 = []
tvector =  [0.0, a, 0.0]
old_object  = []
old_object.extend(basis_object_1)
basis_object_2.extend(old_object)
for i in range(Ny-1):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_2.extend(old_object)


basis_object_3 = []
tvector =  [0.0, 0.0, a]
old_object  = []
old_object.extend(basis_object_2)
basis_object_3.extend(old_object)
for i in range(Nz):
    new_object  =  translator(old_object, tvector)
    old_object  =  new_object
    basis_object_3.extend(old_object)


input_object_1 = basis_object_3

slab2 = []
slab2.extend(input_object_1)

current_id = len(result_a) + len (polymers) +1 + len(basis_object_5) + len(basis_object_6)
group_size = 1 #polymer_size
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(slab, group_size, current_id, id_index)   
basis_object_3 = []
basis_object_3.extend( new_obj ) 


current_id = len(result_a) + number_of_polymers + 1 + len(basis_object_5) + len(basis_object_6)
group_size = 1
remove_existing_trailing_id=True
id_index = None
new_obj = assign_group_ids(basis_object_3, group_size, current_id, id_index)   
basis_object_4 = []
basis_object_4.extend(new_obj) 

t_vector =  [0.0, 0.0, 1.4*Nx*a + 1.2*Nz*a + 1.4*Nx*a]

basis_object_5 = translator (basis_object_4, t_vector)

slab.extend (basis_object_5)





























system  = []

system.extend (slab)
system.extend (polymers)
system.extend (fluid)




bond_length  = 1.0
tolerance  =  0.1

id_body_index = 7

input_object = []
input_object.extend(system)


         


box  = [Nx*a, Nx*a, 1.2*Nx*a +  1.4*Nx*a + 1.8*Nz*a]
whole_system = system #periodic_wrapper(system, box)





build_topology(whole_system, bond_length, tolerance, id_index=6,
                   coord_indices=(0, 1, 2), export_base="topology_check",
                   many_body=True, id_body_index=7)


system  = []

system.extend(whole_system)

        
        
        
input_object = []
input_object.extend(system)


particle_idx=  6
mol_idx  =  7


mol_type_idx = 5
particle_type_idx = 4


moving_mol_id  = []
for i in range(len(input_object)):
    if (input_object[i][mol_type_idx] != 1):
        moving_mol_id.append (input_object [i][mol_idx])
    
box  =  box


iter_max  =  10000000
sigma_matrix =  [[1.1, 1.1, 1.1,  1.1], [1.1, 1.1, 1.5,  1.1], [1.1, 1.5, 1.1,  1.5], [1.1, 1.1, 1.5,  1.1]]

cell_size =  1.15
translation_step  =  0.1
rotation_step  =  0.1
print (input_object[0])
print (input_object[-1])
print (box )

system_final = overlap_remover(input_object, mol_idx, particle_idx, mol_type_idx, particle_type_idx, sigma_matrix, moving_mol_id, box, cell_size, iter_max, translation_step, rotation_step, max_particles_per_cell=128,  grid_shifting_rate=100000)

unwrapped_system= periodic_unwrapper (system_final, box, id_body_index)



build_topology(unwrapped_system, bond_length, tolerance, id_index=6,
                   coord_indices=(0, 1, 2), export_base="topology",
                   many_body=True, id_body_index=7)


particle_vis(system_final, "system")
export_xyz (system_final, "system")


size  = get_object_size(system, coord_indices=[0,1,2])
print (size)


exit (0)
