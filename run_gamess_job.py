#!/usr/bin/python
# Anna Tomberg
# run GAMESS-US job like a normal person

# Last updated : 15-09-2016
import sys
import os

from subprocess import call

# HERE GIVE THE FULL PATH TO GAMESS FOLDER:
path_to_gamess = "C:\gamess.64" #DEFAULT

# HERE GIVE THE VERSION OF GAMESS YOU HAVE:
version = "13-64.pgi.linux.blas" 


if len(sys.argv) <= 1:
	input_file = raw_input("Enter path to input: ")
else:
	input_file = sys.argv[1] 
	
try:
	number_of_processors = sys.argv[2] 
except:
	number_of_processors = 1
	

name = input_file.split(".inp")[0]
output_name = name+".log"

input_directory = os.getcwd()	
call(["copy", input_file, path_to_gamess], shell=True)

os.chdir(path_to_gamess)

# CHECKING THAT THERE ARE NO OLD RESIDUAL FILES
try:
	call(["del", path_to_gamess+"\\tmp\\"+name+".*"], shell=True)
	call(["del", path_to_gamess+"\\scr\\"+name+".*"], shell=True)
except:
	print(">> No residual files found.")
	
# RUNNING GAMESS JOB
call(["rungms.bat", input_file, version, number_of_processors, "0", output_name], shell=True)
call(["copy", output_name, input_directory], shell=True)

print( ">> COMPLETE.")
