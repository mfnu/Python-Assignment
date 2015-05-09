''' Author: Madhulika
     Program: Section4-DictionaryOrShelveFaster.py
     Input: Create a dictionary d.
     Output: Prints the dictionary, also prints the time within which transaction completed.
     Date Created: 5/7/2015
     Version : 1
'''
from datetime import datetime
dt1 = datetime.now()
print("Time before starting Dictionary transaction: "+str(dt1))
d={"Suresh":7,"Madhu":8}
#print("Value of d is: "+d)
print (d)

dt1 = datetime.now()
print("Transaction in Dictionary completed in: "+str(dt1))
print("Dictionary is faster")

'''
O/P:
C:\Python34\Assignments>python Section4-CheckDictionaryFaster.py
Time before starting Dictionary transaction: 2015-05-08 23:12:45.504147
{'Madhu': 8, 'Suresh': 7}
Transaction in Dictionary completed in: 2015-05-08 23:12:45.504147
Dictionary is faster
'''