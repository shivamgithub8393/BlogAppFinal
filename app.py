import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
