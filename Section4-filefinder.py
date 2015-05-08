''' Author: Madhulika
     Program: Section4-filefinder.py
     Input: Ask user to enter the name of file to search.
     Output: find the path of the file and display to user
     Date Created: 5/7/2015
     Version : 1
'''

import os

#---------------------------Function definition------------------------------------------------
def traverse_file(filename):
	foundFile=False
	for root,dirs,files in os.walk(".",topdown=False):
		for name in files:
			searched = []
			searched = os.path.join(root,name)
			if searched.endswith(filename):
				print("File found at: "+str(searched))
				foundFile=True
	if foundFile==False:
		print("Sorry could not find the file :-(")
	
#---------------------------End of Function definition------------------------------------------------

#-------------------------Function call---------------------------------------------------------
filename = input("Please enter the name of file to be searched: ")
traverse_file(filename)
#-------------------------End of Function call---------------------------------------------------------

'''
O/P:

C:\Python34>python Section4-filefinder.py
Please enter the name of file to be searched: Section4-Filefinder-Filetosearch.txt
File found at: .\Assignments\Section4-Filefinder-Filetosearch.txt
File found at: .\Section4-Filefinder-Filetosearch.txt

C:\Python34>python Section4-filefinder.py
Please enter the name of file to be searched: abc.txt
Sorry could not find the file :-(
'''