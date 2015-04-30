'''
   Author: Madhulika
   Program: Finding total number of ears bunny has (even bunnies =3 ears; odd bunnies =2 ears).
   Input: Ask user to enter number of bunnies.
   Output: displays the total number of ears bunny will have.
   Date Created: 4/30/2015
   Logic:
     5 bunnies will have 12 ears.
     1=2
     2=3
     3=2
     4=3
     5=2
     ------
     12

'''
def fibonacci(bunnies):
	if bunnies == 0: return 0
	#if bunnies ==1: return 1
	return fibonacci(bunnies-1)+3-(bunnies%2)
NumberOfBunnies=input("Please enter number of bunnies: ")
NumberOfBunnies=int(NumberOfBunnies)
print("Total number of ears = "+str(fibonacci(NumberOfBunnies)))

'''
O/P:
C:\Python34\Assignments>python Functions-BunnyEars.py
Please enter number of bunnies: 5
Total number of ears = 12
'''

   