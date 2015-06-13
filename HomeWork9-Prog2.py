'''-------------------------------------------------------------------------------------------------------
Author: Madhulika
Program: HW 9 -2 : Enter data in UI and save in sqliteDB
Input: Animal name and Count in UI.
Output: sqlite db saving the contents entered in UI.
Version: 1
-------------------------------------------------------------------------------------------------------'''
from wsgiref.simple_server import make_server
import sqlite3

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form_vals

def hello_world_app(environ, start_response):
	#print("ENVIRON:", environ)
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<br>Your data has been recorded:"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
		for item in form_vals.keys():
			message += "<br/>"+item + " = " + form_vals[item]

		conn=sqlite3.connect("zoo.sqlite")
		cursor=conn.cursor()
		cursor.execute("Insert into zoo(animal,count) values(?,?)",(form_vals['animal'],form_vals['count']))
		conn.commit()
		conn.close()

	message += "<h1>Welcome to the Zoo</h1>"
	message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()