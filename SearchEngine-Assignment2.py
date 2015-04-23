''' Author: Madhulika
     Program: SearchEngine-Assignment2.
     Input: Ask user to search (Ex: for flower/sheep/flower or sheep/flower and sheep)
     Output: When OR is provided the result returns the value found anywhere in the arraylist; but if AND is input exact match is returned.
     Date: 4/22/2015
'''
data_list=["And now here is my secret, a very simple secret: It is only with the heart that one can see rightly; what is essential is invisible to the eye.",
"All grown-ups were once children... but only few of them remember it.",
"People have forgotten this truth","flowers or sheeps","flowers and sheeps","flowers","sheeps","flowers sheeps","flowers are blue but sheeps are green"]

querylist = []
query=input("query:")
if not query.find("or")==-1:
	print("The query has 'or' in it")
	querylist=query.split(' or ')
	for each in querylist:
		print(querylist)
		for i,quote in enumerate(data_list):
			found_at = quote.find(each)
			if( found_at >= 0):
				print("Found at ", i, "..."+quote[found_at:found_at+50], "...")
				
	
else:

	for i,quote in enumerate(data_list):
		found_at = quote.find(query)
		if( found_at >= 0):
			print("Found at ", i, "..."+quote[found_at:found_at+50], "...")
	
