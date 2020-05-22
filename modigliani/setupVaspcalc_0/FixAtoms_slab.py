



import ase, ase.io, ase.build
from ase.constraints import FixAtoms
from ase import Atom
import os,sys


# Fix atoms for slab relaxation 


# e.g python3 FixAtoms_slab vaspfile 6. -> It's going to fix all  non-hydrogen atoms below 6 Angstrom


#6 is the upper_limit_z. It is expressed in cartesian coordinates and represents the maximum limit where the method FixAtoms is 
# going to fix non-H atoms i.e. above upper_limit_z atoms will be free to relax. In addition also H atoms at the bottom will be free to relax.  


       
atoms=ase.io.read(sys.argv[1], format='vasp')


upper_limit_z=float(sys.argv[2])
   
indx_nonH=set([atom.index for atom in atoms if not atom.symbol=='H'])   # it detects all non-H indexes as a set, 

indx_Si=set([atom.index for atom in atoms if atom.symbol=='Si' and atom.z > upper_limit_z])    #it detects all Si indexes having certain z > upper_limit value as a set


   
indx_O=set([atom.index for atom in atoms if atom.symbol=='O' and atom.z > upper_limit_z])   #it detect all O indexes having certain z > upper_limit value as a set 




temp=indx_nonH-indx_Si          # Non-H atoms - Si_with_z > u.l. where u.l. is upper limit



indx_to_fix=list(temp-indx_O)     # Non-H atoms - O_with_z > u.l 


indexes = FixAtoms(indices=indx_to_fix)    # indx_to_fix= Non-H atoms with z< u.l. 





atoms.set_constraint(indexes)
ase.io.write("POSCAR", atoms)
