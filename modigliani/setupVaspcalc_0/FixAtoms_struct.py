

# 

import ase, ase.io, ase.build
from ase.constraints import FixAtoms
from ase import Atom
import os,sys



# FixAtoms_struct freeze atoms for slab relaxation.

# e.g python3 FixAtoms_struct vaspfile 6. ->  It's going to fix all atoms below 6 Angstrom

#6 is the upper_limit_z. It is expressed in cartesian coordinates and represents the maximum limit where the method FixAtoms is 
# going to fix atoms i.e. above upper_limit_z atoms will be free to relax. The only difference between FixAtoms_slab is that 
# H atoms at the bottom are kept fix here. 





       
atoms=ase.io.read(sys.argv[1], format='vasp')
   
upper_limit_z=float(sys.argv[2])





indexes_to_fix= FixAtoms(indices=[atom.index for atom in atoms if atom.z<upper_limit_z])

atoms.set_constraint(indexes_to_fix)

ase.io.write("POSCAR", atoms)
