''' Author: Madhulika
     Program: Section4-PicleUnpickleUserData.py
     Input: Enter name, age and country.
     Output: Creates a text file and stores the input information in form of list,
             and then reads it back.
     Date Created: 5/7/2015
     Version : 1
'''
import pickle
f = open("picklesUserData.txt","bw")
name = input("Please enter your name: ")
age = input("Please enter your age: ")
country = input("Please enter your country of origin: ")

myList=[name,age,country]
pickle.dump(myList,f)
f.close()


#--------------------------Function Definition-----------------------------------
'''
Function name: unpickleAndRead
Description: This function unpickles and reads the pickled file.
Input Parameters: None.
'''
def unpickleAndRead(filename):
   print("Printing the read data from picklesUserData.txt file: ")
   f = open(filename,"br")
   myList = pickle.load(f)
   print(myList)
   f.close()
#--------------------------------------------------------------------------------

#Calling unpickleAndRead function:
unpickleAndRead("picklesUserData.txt")

'''
O/P:
C:\Python34\Assignments>python Section4-PickleUnpickleUserData.py
Please enter your name: Suresh
Please enter your age: 34
Please enter your country of origin: India
Printing the read data from picklesUserData.txt file:
['Suresh', '34', 'India']
'''