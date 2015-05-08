''' Author: Madhulika
     Program: Section4-securityscanner.py
     Input: Ask user to enter the name of file to search.
     Output: 
	1. Finds the path of the file and display to user.
	2. Reads the file, checks if "password" is present in the file, displays where "password" is present, and reports if file is secure or not.
     Date Created: 5/7/2015
     Version : 1
'''

import os
#---------------------------Function definition------------------------------------------------
def traverse_file(filename):
	foundFile=False
	hasPassword=False
	for root,dirs,files in os.walk(".",topdown=False):
		for name in files:
			searched = []
			searched = os.path.join(root,name)
			if searched.endswith(filename):
				print("File found at: "+str(searched))
				foundFile=True
				readfile=open(searched,"r")
				for line in readfile:
					if "password" in line:
						print("File is NOT SECURE, file has password at line: "+str(line))
						hasPassword=True
				
				if hasPassword==False:
					print("File is secure, it does not have password information")
	if foundFile==False:
		print("Sorry could not find the file :-(")
	
#---------------------------End of Function definition------------------------------------------------

#-------------------------Function call---------------------------------------------------------
filename = input("Please enter the name of file to be searched: ")
traverse_file(filename)
#-------------------------End of Function call---------------------------------------------------------

'''
O/P:

C:\Python34\Assignments>python Section4-securityscanner.py
Please enter the name of file to be searched: Section4-Filefinder-Filetosearch.txt
File found at: .\Section4-Filefinder-Filetosearch.txt
File is NOT SECURE, file has password at line: password = helloProfessor
'''