from app import app
from flask import render_template
from app.forms import LoginForm
# there are two decorators, which associate the URLs / and /index to this function
# this means that when a web browser requests either of these two URLs,Flask is
# going to invoke this function and pass the return value of it back to the 
# browser as a response.
@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Wei Song'}
	# the render_template function invokes the Jinja2 template engine that
	# comes bundled with the Flask framework.Jinja2 substitutes {{ ... }}
	# blocks with the corresponding values, given by the arguments provided
	# in the render_template() all
	return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)