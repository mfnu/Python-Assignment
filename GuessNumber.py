''' Author: Madhulika
     Program: Game to guess number.
     Input: Ask user to play yes/no and guess any number between 1 to 100.
     Output: Guessed number
     Date Created: 4/16/2015
     Version : 2
     Date Modified: 4/22/2015
'''

lower = 0
higher = 100
testval = (lower+ higher)//2
#print(testval)

name=input("Please enter your name: ")
Playmore=input("Hi "+name+" Would you like to play a game of guessing number? (Y/N) :")
while (Playmore=='Y'):
	print("Think of random number from 1 to 100, and I'll try to guess it!")
	isFound = False
	while(isFound == False):
		value=input("Is it bigger than " + str(testval)+" (Y/N) : ")
		if (value == 'Y'):
			lower = testval
			
		else:
			higher = testval
		testval = (lower+ higher)//2
		if(lower==testval):
			isFound=True
			testval=testval+1
			print("Got you your number is : "+str(testval))
	Playmore=input(" Would you like to play a game of guessing number? (Y/N) :")
		
else:
	print("Ok Tata! ")

