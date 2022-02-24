#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests

DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "Peter's Starter Template for a Flask Web App",
    "description":  "A basic Flask app using bootstrap for layout",
    "author":       "Peter Simeth",
    "html_title":   "Peter's Starter Template for a Flask Web App",
    "project_name": "Starter Template",
    "keywords":     "flask, webapp, template, basic"
}


@app.route('/')
def index():
    #get data from url
    ona_data = requests.get('https://api.ona.io/api/v1/data/650907', auth=('kipngetich33', 'Empharse333'))
    return render_template('index.html', app_data=ona_data.json())


@app.route('/ona_data',methods=["GET","POST"])
def ona_dat_view():
    print("*"*80)
    print("ona view")
    #get data from url
    ona_data = requests.get('https://api.ona.io/api/v1/data/650907', auth=('kipngetich33', 'Empharse333'))
    return {'data': ona_data.json()}
   

@app.route('/about')
def about():
    return render_template('about.html', app_data=app_data)


@app.route('/service')
def service():
    return render_template('service.html', app_data=app_data)


@app.route('/contact')
def contact():
    return render_template('contact.html', app_data=app_data)


if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)