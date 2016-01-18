#!/usr/bin/python
# Anna Tomberg
# split mol2 file with multiple structures into seperate files

# Last modified: 2015-04-14


#-------------------------------------------------#
#				IMPORTING MODULES				  #
#-------------------------------------------------#
import sys
import os
import re

#-------------------------------------------------#
#				DISPLAY WELCOME MSG				  #
#-------------------------------------------------#
welcome_msg = """
\n ~~~~ SPLITTING MOL2 INTO MULTIPLE FILES ~~~~
>>> To Run: supply .mol2 file as argument1.\n"""

print welcome_msg

#-------------------------------------------------#
#			FIND FILE GIVEN AS ARGUMENT			  #
#-------------------------------------------------#

inp_file = sys.argv[1]  #Get file name
if not os.path.isfile(inp_file):
	sys.exit(">>> This file does not exist. Bye!\n")
		
name = inp_file.split('.')[0]
extension = inp_file.split('.')[1]
	
filelist = []		
f = open(inp_file, "r")	
counter = 0


for line in f.readlines():
	if line.startswith("#\n"):
		counter += 1
		fx = open(name+str(counter)+"."+extension, "w")
		fx.write (line)
		filelist.append(fx)
	else:
		fx.write (line)
		
for fx in filelist:
	fx.close()

f.close()
	
print ("\n>>> DONE.\n")		

#-------------------------------------------------#
#					END OF PROGRAM				  #
#-------------------------------------------------#	
