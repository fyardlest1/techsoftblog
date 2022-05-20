from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__) # this is how we start a flask project

# Create a route decorator
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# localhost:5000/user/Fyard
@app.route('/user/<name>')
def user(name: str):
    return render_template('user.html', name=name)

# Create Custom Error Pages (404)
# For Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 

# For Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500