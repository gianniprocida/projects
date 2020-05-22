



import ase, ase.io, ase.build
from ase.build import surface
from ase import Atoms
import os,sys



atoms=ase.io.read(sys.argv[1], format='vasp')

xyz=atoms.get_scaled_positions()

cell_parameters=atoms.get_cell_lengths_and_angles()

   
# Define the bulk structure

Si8=Atoms('Si8',scaled_positions=xyz,cell=cell_parameters,pbc=True)


import pdb;pdb.set_trace()

# Define slab

# We cut along 100 because , it doesn't change the structure

slab100=surface(Si8,(0,0,1),3)
 
slab100.center(vacuum=9,axis=2)

ase.io.write('POSCAR_001',slab100)


