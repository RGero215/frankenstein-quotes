#!/usr/bin/env python3
import json
import quotes
from flask import (Flask, render_template, redirect, 
                    url_for, make_response, flash, request)
from histogram_dictionary import *

app = Flask(__name__)

app.secret_key = 'ldfasndohsdnafasngoherqowr'

@app.route('/')
def home():
    init = quotes.initialize()
    menu = quotes.menu_loop()
    sentence1 = []
    sentence2 = []
    likes = 0
    for i in range(5, 20):
        sentence1.append(sample(histogram('Frankenstein.txt')))
        sentence2.append(weighted_random(histogram('Frankenstein.txt')))
    return render_template("index.html", sentence1 = ' '.join(sentence1), sentence2 = ' '.join(sentence2), likes=str(likes), saves=get_saved_data())

@app.route('/index')  
def index():
    init = quotes.initialize()
    menu = quotes.menu_loop()
    sentence1 = []
    sentence2 = []
    likes = 0
    add_quote = quotes.add_quote()
    for i in range(5, 20):
        sentence1.append(sample(histogram('Frankenstein.txt')))
        sentence2.append(weighted_random(histogram('Frankenstein.txt')))
    return render_template("index.html", sentence1 = ' '.join(sentence1), sentence2 = ' '.join(sentence2), likes=str(likes), saves=get_saved_data())


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('quotes'))
    except TypeError:
        data = {}
    return data

@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('quotes', json.dumps(data))
    return response

app.run(debug=True)