#50+25 =75+13=88+6=94+3=97+2=99+1=100
''' Author: Madhulika
     Program: Game to guess number.
     Input: Ask user to play yes/no and guess any number between 1 to 100.
     Output: Guessed number
     Date: 4/16/2015
'''

name=input("Please enter your name: ")
Playmore=input("Hi "+name+" Would you like to play a game of guessing number? (Y/N) :")
while(Playmore=='Y'):
	print("Think of random number from 1 to 100, and I'll try to guess it!")
	value=input("Is it 50? (Y/N) : ")
	if(value=='Y'):
		print("Ha ha got you in first shot")
		Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")	
	else:
		value= input("Is it greater than 50? (Y/N): ")
		if(value=='Y'):
			if(value=='Y'):
				value = input("Is it 75? (Y/N): ")
			if(value =='Y'):
				print("Ha ha got you in second shot")
				Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
			else:
				value = input("Is it greater than 75? (Y/N): ")
				if(value =='Y'):
					value = input("Is it 88? (Y/N): ")
					if(value=='Y'):
						print("Ha ha got you in Third shot")
						Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
					else:
						value = input("Is it greater than 88? (Y/N) :")
						if(value=='Y'):
							value = input("Is it 94?(Y/N):")
							if(value=='Y'):
								print("Ha ha got you guessed 94")
								Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
							else:
								value = input("Is it greater than 94? (Y/N): ")
								if(value=='Y'):
									value = input("Is it 97? (Y/N): ")
									if(value=='Y'):
										print("Ha ha got you, you guessed 97")
										Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
									else:
										value = input("Is it greater than 97? (Y/N): ")
										if(value=='Y'):
											value = input("Is it 99? (Y/N) : ")
											if(value=='Y'):
												print("Ha ha got you, you guessed 99")
												Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
											else:
												value = input("Is it 100? (Y/N) : ")
												if(value=='Y'):
													print("Ha ha got you, you guessed 100")
													Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
												else:
													print("You guessed invalid number")
													Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")

		elif(value=='N'):
			value=input("Is it 25 ? (Y/N) : ")
			if(value=='Y'):
				print("Ha ha, you guessed 25")
				Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
			else:
				value= input("Is it less than 25? (Y/N) : ")
				if(value=='Y'):
					value=input("Is it 12? (Y/N): ")
					if(value=='Y'):
						print("Ha ha, you guessed 12")
						Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
					else:
						value=input("Is it less than 12? (Y/N) : ")
						if(value=='Y'):
							value=input("Is it 6? (Y/N) : ")
							if(value=='Y'):
								print("Ha ha, you guessed 6")
								Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
							else:
								value=input("Is it less than 6? (Y/N): ")
								if(value=='Y'):
									value=input("Is it 3? (Y/N) : ")
									if(value=='Y'):
										print("Ha ha, you guessed 3")
										Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
									else:
										value=input("Is it 2? (Y/N)")
										if(value=='Y'):
											print("Ha ha, You guessed 2")
										else:
											print("It should be 1, else you guessed invalid value")
											Playmore=input("Hi "+name+" Would you like to play more? (Y/N) :")
else:
	print("Ok Tata! ")

