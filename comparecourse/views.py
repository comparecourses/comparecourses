from comparecourse import app
from flask import render_template, url_for, request
@app.route('/')
def index():
    return render_template('pehlapanna.html')

@app.route('/search',methods = ['POST'])
def search():
	return ('chalo yahan tak to pahunch gaye ab aage bhi chale jaayenge.'+request.form['query'])
