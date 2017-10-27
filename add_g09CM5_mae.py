# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:02:54 2017

@author: Anna Tomberg

This script is used to add CM5 charges found in a .log file obtained from a 
gaussian calculation into an .mae file.
(In Gaussian : Pop=CM5)

How to use the script (provided you have python installed):
[user]$ python add_g09CM5_mae.py my_gaussian.log my_structure.mae

This will write the CM5 charges from the log into the mae file.
NOTE: it is important that the sequence of atoms in the log and the mae files 
are the same.
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:02:54 2017

@author: Anna Tomberg

This script is used to add CM5 charges found in a .log file obtained from a 
gaussian calculation into an .mae file.
(In Gaussian : Pop=CM5)

How to use the script (provided you have python installed):
[user]$ python add_g09CM5_mae.py my_gaussian.log my_structure.mae

This will write the CM5 charges from the log into the mae file.
NOTE: it is important that the sequence of atoms in the log and the mae files 
are the same.
"""

import sys

#----------------------#
# Get arguments
try:
    gaussian_log = sys.argv[1]
    mae_file = sys.argv[2]
except:
    print "I need a gaussian log and an .mae file to work."
    
#----------------------#
# Read gaussian log
fo = open(gaussian_log, "r")
data = fo.readlines()
fo.close()

counter = -1

for line in data:
    counter = counter +1
    
    if line.startswith(" Hirshfeld charges, spin densities, dipoles, and CM5 charges"):
        counter = counter + 2 #now we are at the line where 1st atom is
        break
    
CM5_charges = []
while not(data[counter].startswith("       Tot ")) and counter < len(data):
    temp = float((data[counter].split())[7])
    temp = round(temp, 5)    
    CM5_charges.append(str(temp)+" ") 
    counter = counter +1
    
if len(CM5_charges)<1:
    print "I couldn't find CM5 charges in this gaussian file. Closing."
    sys.exit()    
    
else:
    print "I have found CM5 charges for ", len(CM5_charges), " atoms."
    
#----------------------#


#----------------------#
# Open mae file and create new data
fo = open(mae_file, "r")
data = fo.readlines()
fo.close()

counter = -1


for line in data:
    counter = counter +1
    
    if line.startswith(" m_atom["):
        h = counter +8
        counter = counter + 11 #now we are at the line where 1st atom is
        
        break

header = "".join(data[:h] )
header = header + """  r_m_charge1\n"""
header = header + "".join(data[h:counter] )

atom_line = []
m = """"""
atom_counter = 0

while not(data[counter].startswith("  :::")) and counter < len(data) and atom_counter <len(CM5_charges):
    temp = (data[counter].split('"'))
    #print temp
    charge = CM5_charges[atom_counter]
    insert_temp = temp[2]+charge
    b = temp[:2] + [insert_temp] + temp[3:]  
    b = '"'.join(b)
    #print b
    
    m = m + b
    
    counter = counter +1
    atom_counter = atom_counter +1

print m

tail = "".join(data[counter:] )
#print tail
#----------------------#


#----------------------#
# Write new data to mae file
print "I'm writing the CM5 charges into the .mae file now."
fw = open(mae_file, "w")
fw.write(header)
fw.write(m)
fw.write(tail)
fw.close()

    
print "--- DONE ---"
