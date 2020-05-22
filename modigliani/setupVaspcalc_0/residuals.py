from ase.build import bulk
import ase, ase.io, ase.build
from ase.build import surface
from ase import Atoms
import os,sys


Mobulk = bulk('Mo', 'bcc', a=3.16, cubic=True)
ase.io.write('POSCAR_bulk',Mobulk)
s2 = surface(Mobulk, (3, 2, 1), 9)
s2.center(vacuum=10, axis=2)


ase.io.write('POSCAR_321',s2)
