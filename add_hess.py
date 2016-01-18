#!/usr/bin/python
# Anna Tomberg
# 06/08/2014
# To add hess section to end of GAMEES-US input file


# importing modules
import sys
import os
import re

# display greating

print ("\n ~~~~ ADD HESSIAN ~~~~\n")
print ("\n >>> Enter INP file then DAT file\n")

# Verify input
if len(sys.argv) <= 2:
	path = raw_input(">>> Enter path to inp file: ")
else:
	path = sys.argv[1]
	dat_name = sys.argv[2]
	
	if not os.path.isfile(path):
		sys.exit(">>> This file does not exist.Bye!")


# Open corresponding dat file
if not os.path.isfile(dat_name):
	sys.exit(">>> Can't find .dat file. Bye!")
else:
	print (">>> Found .dat file.\n")


fo = open("hess_temp.txt", "w")

for line in reversed(open(dat_name).readlines()):
	if line.startswith(" $HESS"):
		fo.write(line)
		break
	else:
		fo.write(line)

fo.close()	

print ">>> Got the $HESS group from the .dat file.\n"
fo = open("hess.txt", "w")	

for line in reversed(open("hess_temp.txt").readlines()):
	print line
	fo.write(line)
	
fo.close()

#fo = open(path, "a")	
#fo.write(HESS_group)
#fo.close()
 
os.remove("hess_temp.txt") 
