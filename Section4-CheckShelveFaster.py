''' Author: Madhulika
     Program: Section4-CheckShevleFaster.py
     Input: Creates new file shelvetest and creates dictionary items in the file.
     Output: Displays the dictionary items created in shelve and also the time within which transaction completed.
     Date Created: 5/7/2015
     Version : 1
'''
from datetime import datetime
dt1 = datetime.now()
print("Time before starting shelve transaction: "+str(dt1))
import shelve
s=shelve.open("shelvetest.txt")
d={"Suresh":7,"Madhu":8}
print(d)
dt1 = datetime.now()
print("Transaction in Shelve completed in: "+str(dt1))

'''
O/P:
C:\Python34\Assignments>python Section4-CheckShelveFaster.py
Time before starting shelve transaction: 2015-05-08 23:19:31.700234
{'Suresh': 7, 'Madhu': 8}
Transaction in Shelve completed in: 2015-05-08 23:19:31.793991

'''