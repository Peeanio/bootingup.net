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
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--isbn", metavar="ISBN", dest="isbn_str", \
help="the ISBN number to use")
args= parser.parse_args()

#isbn_str = "055329461X"

def get_book_info():
	#uses the ISBN to get information on book from openlibrary 
	#isbn = str(9781492051367)
	#get complete payload
	payload = {'bibkeys': 'ISBN:' + args.isbn_str, 'format': 'json', 'jscmd': 'details'}
	r = requests.get('https://openlibrary.org/api/books', params=payload)
	y = r.json()
	
	global general_json
	global detail_json
	general_json = y['ISBN:' + args.isbn_str]
	detail_json = general_json['details']

def get_book_description():
    '''uses the info_url to find the web page, parse it out to get the 
    description
    '''
    book_url = general_json["info_url"]
    #print(book_url)
    book_webpage = requests.get(book_url)
    #print(book_webpage)
    webpage_content = book_webpage.text
    #print(webpage_content)
    content = BeautifulSoup(webpage_content, 'lxml')
    #print(content)
    #description = content.find_all('div', attrs={'class':'workHelp'})
    description = content.find_all('p', attrs={'class':'workHelp'})
    #description = content.find_all('div', attrs={'class':'book-description-content restricted-view'})
    print(description)

class Book():
	#load up a book with data from the API
	def __init__(self, isbn):
		self.isbn = isbn
		self.title = detail_json["title"]
		self.numOfPages = detail_json["number_of_pages"]
		self.publishDate = detail_json["publish_date"]
		self.authors_json = detail_json["authors"]
		self.authors_first = self.authors_json[0]
		self.authors = self.authors_first["name"]
		
		
def main():
	#main script starts here
	#print(z['authors'])
	get_book_info()
	# print(str(general_json) + "\n" + "\n")
	# print(detail_json)
	# print('now for the show...' + '\n' + '\n')
	thebook = Book(args.isbn_str)
	print(thebook.title)
	print(thebook.isbn)
	print(thebook.authors)
	print(thebook.publishDate)
	print(str(thebook.numOfPages) + " pages")
	get_book_description()

try:
	args.isbn_str
except:
	parser.print_help()

main()
