'''
     Author: Madhulika
     Program: Section5-Assignment1
     Input: Ask user to enter the country code.
     Output: Display following information:
	     Country Name.
	     Capital of the Country.
     Date Created: 5/13/2015

'''
countryInformation = {"name":"Colombia","capital":"Bogota","altSpellings":["CO","Republic of Colombia","Republica de Colombia"],"relevance":"0","region":"Americas","subregion":"South America","translations":{"de":"Kolumbien","es":"Colombia","fr":"Colombie","ja":"Japan","it":"Colombia"},"population":47907800,"latlng":[4.0,-72.0],"demonym":"Colombian","area":1141748.0,"gini":55.9,"timezones":["UTC-05:00"],"borders":["BRA","ECU","PAN","PER","VEN"],"nativeName":"Colombia","callingCodes":["57"],"topLevelDomain":[".co"],"alpha2Code":"CO","alpha3Code":"COL","currencies":["COP"],"languages":["es"]}
countryCode = input("Please enter country code: ")
altspellings=countryInformation["altSpellings"]
found = False
for i,quote in enumerate(altspellings):
	found_at=quote.find(countryCode)
	if(found_at>=0):
		print("Country code found, country name is = ", countryInformation["name"])
		print("Capital of the country is = ", countryInformation["capital"])
		found=True
if(found!=True):
	print("Sorry the code you entered does not exists")


'''
O/P:
C:\Python34\Assignments>python Section5-Assignment1.py
Please enter country code: CO
Country code found, country name is =  Colombia
Capital of the country is =  Bogota

'''

