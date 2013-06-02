from comparecourse import app
from flask import render_template, url_for, request
from comparecourse.schema import *

@app.route('/')
def index():
    return render_template('pehlapanna.html')

@app.route('/search',methods = ['GET'])
def search():
	return (find_courses(request.args.get('query', '')))

def find_courses(s):
	for course in Course.select():
		if (s == course.name):
			return "match found"+":"+s
		else:
			return "no match found"
	
