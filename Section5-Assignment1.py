'''
     Author: Madhulika
     Program: Section5-Assignment1
     Input: None
     Output: Crawls through all pages of University of New Haven link and displays the "href links" it visited.
     Date Created: 5/15/2015

'''
import urllib.request
from urllib.error import  URLError
import re


def visit_url(url, domain):
	global crawler_backlog
	if(len(crawler_backlog)>100):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_keyhref = re.compile('<link href="(asset.*.css)" rel="stylesheet" />')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)

			if result:
				title = result.group("title")
				print(title)

			result = regexp_keyhref.search(content_string, re.IGNORECASE)

			if result:
				keywords = result.group("keywords")
				print(keywords)

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain)
	except URLError as e:
		print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")

'''
O/P
Processing: http://www.newhaven.edu/academics/resources/bursars/750041/
University of New Haven : Bursar Forms
Processing: http://www.newhaven.edu/academics/resources/
University of New Haven : Academic Resources
Processing: http://www.newhaven.edu/academics/resources/registrar/
University of New Haven : Office of the University Registrar
Processing: http://www.newhaven.edu/academics/resources/registrar/regulations/
University of New Haven : Academic Regulations
Processing: http://www.newhaven.edu/academics/resources/registrar/degree
error
Processing: http://www.newhaven.edu/academics/resources/registrar/diploma
error
Processing: http://www.newhaven.edu/academics/resources/registrar/FERPA/
University of New Haven : FERPA Policy
Processing: http://www.newhaven.edu/academics/resources/registrar/FERPA/directo
y/
University of New Haven : Directory Information
Processing: http://www.newhaven.edu/academics/resources/registrar/FERPA/release
error
Processing: http://www.newhaven.edu/academics/resources/registrar/forms/
University of New Haven : Registrar Forms
Processing: http://www.newhaven.edu/831482
University of New Haven : Academic Program Change Request - Grad
Processing: http://www.newhaven.edu/291891/
University of New Haven : All Resource Collections
Processing: http://www.newhaven.edu/291891
University of New Haven : All Resource Collections
Processing: http://www.newhaven.edu/292038/
University of New Haven : Academics
Processing: http://www.newhaven.edu/292038
University of New Haven : Academics
Processing: http://www.newhaven.edu/301001/
University of New Haven : Registrar
Processing: http://www.newhaven.edu/301001
University of New Haven : Registrar
Processing: http://www.newhaven.edu/301103
University of New Haven : Academic Program Change Request - Undergrad
Processing: http://www.newhaven.edu/academics/resources/registrar/grading/
University of New Haven : Grading Systems
Processing: http://www.newhaven.edu/academics/resources/registrar/graduation
error
Processing: http://www.newhaven.edu/academics/resources/registrar/staff/
University of New Haven : Registrar's Office Staff
Processing: http://www.newhaven.edu/academics/resources/registrar/registration
error
Processing: http://www.newhaven.edu/academics/resources/registrar/transcript
error
Processing: http://www.newhaven.edu/academics/resources/registrar/veterans/
University of New Haven : Veterans Affairs
Processing: http://www.newhaven.edu/academics/resources/registrar/veterans/mili
ary
error
Processing: http://www.newhaven.edu/about/institutional
error
'''