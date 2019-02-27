#!/usr/bin/env python3
import json
import quotes
import os
from flask import (Flask, render_template, redirect, 
                    url_for, make_response, flash, request)
from histogram_dictionary import *
from markov_chain import markov_chain

app = Flask(__name__)

app.secret_key = 'ldfasndohsdnafasngoherqowr'

@app.route('/')
def home():
    likes = 0
    sentence1 = markov_chain(word_list('Frankenstein.txt'), 15)
    sentence2 = markov_chain(word_list('Frankenstein.txt'), 15)
    
    quotes.Quote.create(
            quote_one = sentence1,
            quote_two = sentence2,
            likes = likes,
        )
    return render_template("index.html", sentence1 = sentence1, sentence2 = sentence2, likes=str(likes))

@app.route('/index')  
def index():
    init = quotes.initialize()
    menu = quotes.menu_loop()
    likes = 0
    add_quote = quotes.add_quote()

    sentence1 = markov_chain(word_list('Frankenstein.txt'), 15)
    sentence2 = markov_chain(word_list('Frankenstein.txt'),15)
    return render_template("index.html", sentence1 = sentence1, sentence2 = sentence2, likes=str(likes), saves=get_saved_data())

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)