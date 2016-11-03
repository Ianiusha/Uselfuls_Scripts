# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:09:11 2016

@author: ania
"""


import sys
#import re
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# ------------- GET INPUT FILE ------------- #	
if len(sys.argv) <= 1:
	name = raw_input("Enter path to input: ")
else:
	name = sys.argv[1] 
	
fo = open(name, "r")
data = fo.readlines()
fo.close()

# ------------------------------------------ #

counter = -1
Energy = []
atoms = -10
where_xyz = []

# -------------- EXTRACT INFO -------------- #	

for line in data:
        counter += 1
        
        if line.startswith("FINAL SINGLE POINT ENERGY"):	#ENERGY (1)
		Energy.append(line.split()[4])
  
        if line.startswith("Number of atoms                         ...."):	#ATOMS
		atoms = int(line.split()[4]) 
  
        if line.startswith("CARTESIAN COORDINATES (ANGSTROEM)"):	#XYZ
		where_xyz.append(counter +2)

xyz_name = (name.split(".")[0])+".xyz"
print ">> Making ", xyz_name

fw = open(xyz_name, "w")
for x in range(len(where_xyz)-1):
    fw.write(str(atoms) + "\n")
    fw.write("Coordinates from ORCA-job " + name + " E " + Energy[x] + "\n")
    fw.writelines(data[(where_xyz[x]) : (where_xyz[x]+atoms)])

fw.close()


# -------------- PLOT ENERGY GRAPH -------------- #	
# energy as function of step number
"""
try:
    plt.figure()
    
    ax = plt.subplot(111)
    #plt.title(name + ": Energy by step")  
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax.plot(list(range(1, len(Energy)+1)), Energy, 'r-')
    
    plt.show()

except:
    print ">> Something went wrong with Energy plot."
"""



# ------------------------------------------ #

print ">>COMPLETE."