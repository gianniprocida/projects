
from pymatgen import Structure
import sys
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

# Detect space group of some structure. Usage: python3 check_sym CONTCAR (or POSCAR)

space_group=SpacegroupAnalyzer(Structure.from_file(sys.argv[1]),symprec=0.10,angle_tolerance=5).get_space_group_symbol()

crystal_system=SpacegroupAnalyzer(Structure.from_file(sys.argv[1])).get_crystal_system()

print(space_group,crystal_system)
