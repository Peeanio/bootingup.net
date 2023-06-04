#!/usr/bin/python

'''
Author: Max Russell, max@theguards.net
tool to work with openlibary api
goal is to generate a html file formatted to look nice from a list of ISBN's
for use on a web server or other viewer
'''
import requests
import json
import argparse
import re
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from unidecode import unidecode
import os
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--isbn", metavar="ISBN", dest="isbn_str", \
help="the ISBN number to use")
args= parser.parse_args()

#isbn_str = "055329461X"

class Book():
    #load up a book with data from the API
    def __init__(self, isbn):
        self.isbn = isbn
        self.get_book_info()
        self.title = self.general_json["title"]
        self.url = self.general_json["url"]
        try:
            self.pages = self.general_json["number_of_pages"]
        except:
            try:
                self.pages = self.general_json["pagination"]
            except:
                self.pages = ""
        try:
            self.year = self.general_json["publish_date"]
        except:
            self.year = ""
        authors_json = self.general_json["authors"]
        authors_list = []
        for value in authors_json:
            authors_list.append(value["name"])
        if len(authors_list) == 1:
            self.authors = authors_list[0]
        else:
            self.authors = ", ".join(authors_list)
        self.get_book_description()

    def get_book_info(self):
        payload = {'bibkeys': 'ISBN:' + self.isbn, 'format': 'json', 'jscmd': 'data'}
        r = requests.get('https://openlibrary.org/api/books', params=payload)
        y = r.json()
        self.general_json = y['ISBN:' + args.isbn_str]

    def get_book_description(self):
        '''uses the info_url to find the web page, parse it out to get the
        description
        '''
        book_url = self.general_json["url"]
        book_webpage = requests.get(book_url)
        webpage_content = book_webpage.text
        content = BeautifulSoup(webpage_content, 'lxml')
        description = content.find_all('div', attrs={'class':'book-description-content restricted-view'})
        html = BeautifulSoup(str(description), 'lxml')
        text = html.find_all('p')
        desc_list = []
        for count, paragraph in enumerate(text):
            black_list = ["<p>", "</p>", "\n"]
            if count == 0:
                pass
            else:
                for black in black_list:
                    paragraph = str(paragraph).replace(black, '')
                desc_list.append(unidecode(paragraph))
        self.description = ''.join(desc_list)

    def render_template(self):
        '''uses a book object and template to create a post file'''
        now = datetime.now()
        now_formatted = now.strftime("%Y-%m-%d %H:%M:%S -0700")
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("book.j2")
        filename = self.isbn + "_post.markdown"
        rendered = template.render(title=self.title, 
                                    date=now_formatted,
                                    isbn=self.isbn,
                                    authors=self.authors,
                                    year=self.year,
                                    pages=self.pages,
                                    description=self.description,
                                    url=self.url)
        with open(filename, mode="w", encoding="utf-8") as post:
            post.write(rendered)
    

def main():
    #main script starts here
    if os.path.isfile(args.isbn_str + "_post.markdown"):
        print("exists, skipping ", args.isbn_str)
    else:
        thebook = Book(args.isbn_str)
        print(thebook.title)
        print(thebook.isbn)
        print(thebook.authors)
        print(thebook.year)
        print(str(thebook.pages) + " pages")
        thebook.render_template()

try:
    args.isbn_str
except:
    parser.print_help()

main()
