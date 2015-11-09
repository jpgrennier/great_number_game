from flask import Flask, session, request, redirect, render_template
import random
app = Flask(__name__)
app.secret_key = 'WordsAndStuffAndThings'

@app.route('/')
def index():
	try:
		session['number']
	except:
		session['number'] = random.randrange(0,101)
	return render_template('index.html')
@app.route('/guess', methods = ['POST'])
def guess():
	if int(request.form['guess']) < session['number']:
		session['message'] = 'Too Low!'
	elif int(request.form['guess']) > session['number']:
		session['message'] = 'Too High!'
	elif int(request.form['guess']) == session['number']:
		session['message'] = 'Perfect!'
	return redirect ('/')
@app.route('/reset', methods = ['POST'])
def reset():
	session.pop('number')
	session.pop('message')
	return redirect('/')

app.run(debug=True) 