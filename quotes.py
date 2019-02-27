
from collections import OrderedDict
import datetime
import sys
import os

from peewee import *

db = SqliteDatabase('quotes.db')

class Quote(Model):
    quote_one = TextField()
    quote_two = TextField()
    likes = IntegerField(default=0)
    timestamp = TimestampField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """ Create the database and the table if they don't exist"""
    db.connect()
    db.create_tables([Quote], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """ Show the menu """
    choice = 'q'
    
    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

def add_quote():
    if data:
        Quote.create(
        quote_one = quote_one,
        quote_two = quote_two,
        likes = likes,   
        )
        print('Saved successfully!')

def view_quote(search_query=None):
    """View previous quotes """
    quotes = Quote.select().order_by(Quote.timestamp.desc())

    if search_query:
        quotes = quotes.where(
            Quote.quote_one.contains(search_query),
            Quote.quote_two.contains(search_query)
        )
    for quote in quotes:
        timestamp = quote.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(quote.content)
        print('\n\n'+'='*len(timestamp))
        print('n) next entry')
        print('d) delete quote')
        print('q) return to main menu')

        nex_action = input('Action: [Ndq] ').lower().strip()
        if nex_action == 'q':
            break
        elif nex_action == 'd':
            delete_quote(quote)
        
def search_quote():
    """Search quote for string"""
    view_quote(input('Search query: '))

def delete_quote(quote):
    """ Delete quote"""
    if input("Are you sure? [yN] ").lower() == 'y':
        quote.delete_instance()
        print("Quote Deleted")

menu = OrderedDict([
    ('v', view_quote),
    ('s', search_quote)
])

if __name__ == '__main__':
    initialize()
    menu_loop()