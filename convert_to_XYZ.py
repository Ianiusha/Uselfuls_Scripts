#!/usr/bin/python
# Anna Tomberg
#


# Last updated : 04-12-2015


import re
import sys
import os

msg="""
------------------------------------------------------
This script convert GAMESS-US log file into xyz format.
Options:
	-h		print help
	-i		inverse tranjectory
	[ ]		default
------------------------------------------------------
"""

inverse_trajectory = False

if sys.argv[1] == '-h':
	sys.exit(msg)
elif sys.argv[1] == '-i':
	inverse_trajectory = True
	file_name = sys.argv[2]
else:
	file_name = sys.argv[1]

	
fo = open(file_name , "r")
lines = fo.readlines()
fo.close()


gamess_output = False


if lines[0].startswith("----- GAMESS execution script 'rungms' -----"):	
	gamess_output = True
	print(">>> Reading a GAMESS output.")

	
if gamess_output:

	line_counter = -1
	total_atoms = 0
	IRC_step = []
	IRC_energy = 0

	xyz_name = file_name.replace('.log', '.')
		
	for line in lines:
		line_counter += 1
		
		if line.startswith(" TOTAL NUMBER OF ATOMS"):
			total_atoms = int(line.split()[-1])
			print("TOTAL NUMBER OF ATOMS:"),total_atoms
			
				
		elif re.search("ON THE REACTION PATH",line):
		
			IRC_step.append(line.split()[2])
			IRC_energy = (lines[line_counter+3].split()[3])
			
			ft = open(xyz_name+IRC_step[-1], "w")
			ft.write(str(total_atoms)+'\n')
			ft.write('Coordinates from GAMESS job ' +file_name+ ' E ' + IRC_energy+'\n')

			for n in range(total_atoms):			
				temp = lines[line_counter + 9 + n].split()
				ft.write('\t'+temp[0]+'\t'+temp[2]+'\t'+temp[3]+'\t'+temp[4]+'\n')

			ft.close()

	if inverse_trajectory:
		fo = open(xyz_name+'xyz', "w")
		for x in reversed(range(len(IRC_step))):
			ft = open(xyz_name+IRC_step[x], "r")
			fo.writelines(ft.readlines())
			ft.close()
			os.remove(xyz_name+IRC_step[x])

	else:
		fo = open(xyz_name+'xyz', "w")
		for x in reversed(range(len(IRC_step))):
			ft = open(xyz_name+IRC_step[x], "r")
			fo.writelines(ft.readlines())
			ft.close()
			os.remove(xyz_name+IRC_step[x])

	fo.close()
