from application import app
from flask import render_template, request, redirect, url_for

@app.route('/') #@app.route is a decorator to tell Flask what URL should trigger our function
def index():
    return render_template('index.html', title = 'Home')

@app.route('/layout')
def layout():
    return render_template('layout.html')
