''' Author: Madhulika
     Program: Finding repeats in a list.
     Output: The program returns the number of times the element is repeated in the list.
     Date Created: 4/60/2015
     Version : 1
'''

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
def count_frequency(mylist):
	result = dict((i,mylist.count(i)) for i in mylist)
	return result

print(count_frequency(mylist))

'''
O/P:
C:\Python34\Assignments>python Functions-repeatsinlist.py
{'eleven': 3, 'seven': 1, 'one': 2, 'two': 2, 'three': 2}
'''