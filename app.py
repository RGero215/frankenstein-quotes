#!/usr/bin/env python3
import json
import quotes
from flask import (Flask, render_template, redirect, 
                    url_for, make_response, flash, request)
from histogram_dictionary import *
import markov_chain

app = Flask(__name__)

app.secret_key = 'ldfasndohsdnafasngoherqowr'

@app.route('/')
def home():
    sentence1 = []
    sentence2 = []
    likes = 0
    sentence1.append(markov_chain(histogram('Frankenstein.txt')))
    sentence2.append(markov_chain(histogram('Frankenstein.txt')))
    quotes.Quote.create(
            quote_one = ' '.join(sentence1),
            quote_two = ' '.join(sentence2),
            likes = likes,
        )
    return render_template("index.html", sentence1 = ' '.join(sentence1), sentence2 = ' '.join(sentence2), likes=str(likes))

@app.route('/index')  
def index():
    init = quotes.initialize()
    menu = quotes.menu_loop()
    sentence1 = []
    sentence2 = []
    likes = 0
    add_quote = quotes.add_quote()

    sentence1.append(markov_chain(histogram('Frankenstein.txt')))
    sentence2.append(markov_chain(histogram('Frankenstein.txt')))
    return render_template("index.html", sentence1 = ' '.join(sentence1), sentence2 = ' '.join(sentence2), likes=str(likes), saves=get_saved_data())

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)