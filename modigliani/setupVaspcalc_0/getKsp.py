
from pymatgen import Structure
import sys
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


# Tips on how perform convergence test for VAP

# 1)Loop over a set of kinetic energy cut-off values.

#These should be a simple static calculation. Make sure that each of the calculations finishes successfully, otherwise you will not be able to compare results and check convergence.

#2) KPOINTS : Once you have the ideal cutoff, you need to find out the number of kpoint at which the energy and the lattice
# parameters converge.
# Here since we need to do slab calculations, it's important to find out the KSPACING as well. 
# It's important to get KSPACING out of the 
# We assume that structure reaches convergence at 5x5x5 kpoints within a range of 0.001 Angstrom and
# the energy reaches convergence at 12x12x12 kpoints within a range 0f 0.0001 eV ( for quartz )
# 

# Return reciprocal lattice for the first and second structure (s0 and s1).


s0=Structure.from_file(sys.argv[1])                     

s1=Structure.from_file(sys.argv[2])



#Number of kpoints_along_i=max(1,|b_i|/KSPACING). where i might be x,y,z. b_i is the reprocal lattice vector along i in module.

recip_lat_s0=s0.lattice.reciprocal_lattice

k_sp_a=recip_lat_s0.abc[0]/5                    # k_sp_a -> KSPACING along a

k_sp_b=recip_lat_s0.abc[1]/5                     # k_sp_b -> KSPACING along b

k_sp_c=recip_lat_s0.abc[2]/5                     # k_sp_c -> KSPACING along c


print("Kspacing to relax the quartz along a,b,c: '%.8f %.8f %.8f'"%(k_sp_a,k_sp_b,k_sp_c))



recip_lat_s1=s1.lattice.reciprocal_lattice

kp_a=recip_lat_s1.abc[0]/k_sp_a


kp_b=recip_lat_s1.abc[1]/k_sp_b

#kp_c=recip_lat_s1.abc[1]/k_sp_b

kp_c=1                                     


print(" ")

print("k-points necessary to relax the slab supercell along a,b,c: '%.4f %.4f %i'"%(kp_a,kp_b,kp_c))


