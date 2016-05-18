#!/usr/bin/python
# To easily insert ECP and rest of basis set of a GAMESS .nip file


# importing modules
import sys
import os
import re

# display menu

print ("\n ~~~~ WELCOME TO GAMESS Basis Set CUSTOMIZER ~~~~\n")

message = ("To Run: python script-name.py file_name.inp\n")
print message

# Verify input
if len(sys.argv) <= 1:
	path = raw_input("Enter path to log file: ")
else:
	path = sys.argv[1]
	if not os.path.isfile(path):
		sys.exit("This file does not exist.Bye!")

# Basis set Coefficients:
"""!  LANL2DZ ECP  EMSL  Basis Set Exchange Library   5/18/16 4:50 AM
! Elements                             References
! --------                             ----------
! H  - Ne: T. H. Dunning Jr. and P. J. Hay, in Methods of Electronic Structure
! Theory, Vol. 2, H. F. Schaefer III, ed., PLENUM PRESS (1977)
! Na - Hg: P. J. Hay and W. R. Wadt, J. Chem. Phys. 82, 270 (1985).
! P. J. Hay and W. R. Wadt, J. Chem. Phys. 82, 284 (1985).
! P. J. Hay and W. R. Wadt, J. Chem. Phys. 82, 299 (1985).
! """

Zn = """ S   2
  1      0.7997000             -0.6486112        
  2      0.1752000              1.3138291        
 S   1
  1      0.0556000              1.0000000        
 P   1
  1      0.1202000              1.0000000        
 P   1
  1      0.0351000              1.0000000        
 D   4
  1     68.8500000              0.0258532        
  2     18.3200000              0.1651195        
  3      5.9220000              0.4468212        
  4      1.9270000              0.5831080        
 D   1
  1      0.5528000              1.0000000   
  
"""
Zn_ECP = """   
ZN-ECP GEN     18     3
  5      ----- f-ul potential     -----
    -18.0000000        1    386.7379660        
   -124.3527403        2     72.8587359        
    -30.6601822        2     15.9066170        
    -10.6358989        2      4.3502340        
     -0.7683623        2      1.2842199        
  5      ----- s-ul potential     -----
      3.0000000        0     19.0867858        
     22.5234225        1      5.0231080        
     48.4465942        2      1.2701744        
    -44.5560119        2      1.0671287        
     12.9983958        2      0.9264190        
  5      ----- p-ul potential     -----
      5.0000000        0     43.4927750        
     20.7435589        1     20.8692669        
     90.3027158        2     21.7118378        
     74.6610316        2      6.3616915        
      9.8894424        2      1.2291195        
  3      ----- d-ul potential     -----
     -4.8490359        2     13.5851800        
      3.6913379        2      9.8373050        
     -0.5037319        2      0.8373113 
	 
"""

"""
!  6-31+G*  EMSL  Basis Set Exchange Library   5/18/16 5:06 AM
! Elements                             References
! --------                             ----------
! H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca:  .
! 6-31+G* Split Valence + Polarization Basis
!                     ------------------------------------------
! Elements      Contraction                       References
!  H     : (4s)        -> [2s]       P.C. Hariharan and J.A. Pople, Theoret.
! He     : (4s)        -> [2s]       Chimica Acta 28, 213 (1973).
! Li - Ne: (11s,5p,1d) -> [4s,3p,1d]
! Na - Ar: (16s,10p,1d)-> [4s,3p,1d] M.M. Francl, W.J. Petro, W.J. Hehre, J.S.
!                                    Binkley, M.S. Gordon, D.J. DeFrees and J.A.
!                                    Pople, J. Chem. Phys. 77, 3654 (1982)
!                                    Note: He and Ne are unpublished basis sets
!                                          taken from the Gaussian program.
! Diffuse exponents: T. Clark, J. Chandrasekhar, P.v.R. Schleyer, J. Comp. Chem.
!                    4, 294 (1983).  R. Krishnam, J.S. Binkley, R. Seeger, J.A.
!                    Pople, J. Chem. Phys. 72, 650 (1980).  P.M.W. Gill, B.G.
!                    Johnson, J.A. Pople and M.J. Frisch, Chem. Phys. Lett.
!                    197, 499 (1992).
"""
C = """ S   6
  1   3047.5249000              0.0018347        
  2    457.3695100              0.0140373        
  3    103.9486900              0.0688426        
  4     29.2101550              0.2321844        
  5      9.2866630              0.4679413        
  6      3.1639270              0.3623120        
 L   3
  1      7.8682724             -0.1193324              0.0689991        
  2      1.8812885             -0.1608542              0.3164240        
  3      0.5442493              1.1434564              0.7443083        
 L   1
  1      0.1687144              1.0000000              1.0000000        
 L   1
  1      0.0438000              1.0000000              1.0000000        
 D   1
  1      0.8000000              1.0000000       
  
"""
H = """ S   3
  1     18.7311370              0.03349460       
  2      2.8253937              0.23472695       
  3      0.6401217              0.81375733       
 S   1
  1      0.1612778              1.0000000  

"""  
N = """ S   6
  1   4173.5110000              0.0018348        
  2    627.4579000              0.0139950        
  3    142.9021000              0.0685870        
  4     40.2343300              0.2322410        
  5     12.8202100              0.4690700        
  6      4.3904370              0.3604550        
 L   3
  1     11.6263580             -0.1149610              0.0675800        
  2      2.7162800             -0.1691180              0.3239070        
  3      0.7722180              1.1458520              0.7408950        
 L   1
  1      0.2120313              1.0000000              1.0000000        
 L   1
  1      0.0639000              1.0000000              1.0000000        
 D   1
  1      0.8000000              1.0000000

"""  
O = """ S   6
  1   5484.6717000              0.0018311        
  2    825.2349500              0.0139501        
  3    188.0469600              0.0684451        
  4     52.9645000              0.2327143        
  5     16.8975700              0.4701930        
  6      5.7996353              0.3585209        
 L   3
  1     15.5396160             -0.1107775              0.0708743        
  2      3.5999336             -0.1480263              0.3397528        
  3      1.0137618              1.1307670              0.7271586        
 L   1
  1      0.2700058              1.0000000              1.0000000        
 L   1
  1      0.0845000              1.0000000              1.0000000        
 D   1
  1      0.8000000              1.0000000       

"""
 
 
# BASIS SET DICTIONARY:
 
customA2 ={"Zn":Zn, "C ":C, "H ":H, "N ": N, "O ": O}
#Zn = ECP
#C  = 6-31+G*
#H  = 6-31+G* 
#N  = 6-31+G*
#O  = 6-31+G*

 
# Get file
fo = open(path, "r")	
lines =  fo.readlines()
fo.close()
	
# in file.inp: 
#	1) Erase $BASIS	.* $END\n line
#	2) For each line in the $DATA (skipping the first 2):
#		- get first letter
#		- go to list of elements
#		- if element exists: add corresponding BS
#		- else: print error message
# will need to read and write separately!

f = open(path,"w")
atoms = []

for line in lines:
	if line.startswith(" $BASIS"):
		print "\n...removing $BASIS ...  $END\n"
	
	elif re.match("(\w+)(\s+)(\d).*", line) is not None:	
		# found line with element and coordinates
		# C     6.0     5.36808    25.49591    20.49677
		element = line[0]+line[1]
		print element
		atoms.append(element)
		
		# write line, add BS after
		f.write(line)
		
		# find element in dictionary customA2
		if customA2.has_key(element):
			bs = customA2.get(element)
			f.write(bs)
		else:
			print "No such element in my Basis set: "+element

			
		
	else:
		f.write(line)
		
# add $ECP section at end of file:



"""
! Elements                             References
! --------                             ----------
! Na - Hg: P. J. Hay and W. R. Wadt, J. Chem. Phys. 82, 270 (1985).
! P. J. Hay and W. R. Wadt, J. Chem. Phys. 82, 284 (1985).
! P. J. Hay and W. R. Wadt, J. Chem. Phys. 82, 299 (1985).
! 
"""
f.write("\n $ECP\n")

for element in atoms:
	if element == "Zn":
		f.write(Zn_ECP)
		
	else:
		f.write(element +"- ECP NONE\n")
f.write(" $END")		
f.close()

print "I'm done. Please make sure I did no mistake!"




 