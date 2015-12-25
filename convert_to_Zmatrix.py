#!/usr/bin/python
# Anna Tomberg
# convert Avogadro's compact zMatrix to ORCA format


import re
import sys
	
fo = open(sys.argv[1] , "r")
line_counter = 1

lines = fo.readlines()
fo.close()

for line in lines:
	
	if line.startswith("* int"):	
		break
	line_counter += 1


new_coords = []

for x in range(line_counter, len(lines)):
	
	temp = lines[x].split()

	if temp[0] == '*':
		break
			
	else:
		new_line = [0]
		m = re.search('([a-zA-Z]+)([0-9]+)', temp[0])
		
		new_line[0]=(m.group(1)) # atoms in molecule
		atoms = []
		values = []
		
		for i in range(1,len(temp)):
			#print i, temp[i]
			
			if (i%2):			# atom columns
				m = re.search('([a-zA-Z]+)([0-9]+)', temp[i])
				atoms.append(m.group(2))

			else:				# value comlumns
				values.append(temp[i])
				
		
		atoms = atoms + [0] * (3 - len(atoms))
		values = values + ['0.0000'] * (3 - len(values))
		new_coords.append(new_line + atoms + values)

fo = open(sys.argv[1] , "a")
fo.write('\n')
		
for line in (new_coords):
	
	print " ".join(str(x) for x in line)
	fo.write(" ".join(str(x) for x in line)+'\n')

fo.close()
