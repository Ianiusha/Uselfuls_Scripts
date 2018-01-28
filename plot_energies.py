#!/usr/bin/python
# Anna Tomberg
# Plot info from orca run using *.out file

# Last updated : 02-12-2015

import sys
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# ------------- GET INPUT FILE ------------- #	
if len(sys.argv) <= 1:
	name = raw_input("Enter path to input: ")
else:
	name = sys.argv[1] 
	
fo = open(name, "r")
lines = fo.readlines()
fo.close()
# ------------------------------------------ #


# -------------- EXTRACT INFO -------------- #	
print lines[2]	

if re.search(" O   R   C   A ", lines[2]):
	print 'this is an orca output'
	we_continue = True
else :
	print 'dunno this output format!'
	we_continue = False
	
	
if we_continue:
        flagD3 = False
        spattern = "Total Energy       :     "
        pos = 3
        Energy = []
        for line in lines:
                if re.search(spattern, line):
                        temp = line.split()[pos]
                        Energy.append(temp)
                if re.search("DFTD3", line):
                        if flagD3 == False:
                                flagD3 = True
                                spattern = "FINAL SINGLE POINT ENERGY"
                                pos = 4
                                Energy = []
# convert string to float
        Energy=[(lambda x: float(x))(x) for x in Energy]

# ------------- PLOTTING STUFF ------------- #			
# If only SCF cycle, plot OPTION 1.
# If got passed 1st SCF cycle, plot OPTION 2.
# ------------------------------------------ #	

# OPTION 1:
if Energy != []:

	
	plt.figure()
	
	ax = plt.subplot(111)	
	plt.title("Energy")
	ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
	ax.plot(list(range(1, len(Energy)+1)), Energy, 'r-')
	


plt.show()
