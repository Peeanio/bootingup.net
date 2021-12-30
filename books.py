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


class Book():
	#load up a book with data from the API
	def __init__(self, isbn):
		self.isbn = isbn
		self.title = detail_json["title"]
		self.numOfPages = detail_json["number_of_pages"]
		self.publishDate = detail_json["publish_date"]
		
		
def main():
	#main script starts here
	#print(z['authors'])
	get_book_info()
	print(str(general_json) + "\n" + "\n")
	print(detail_json)
	print('now for the show...' + '\n' + '\n')
	thebook = Book(args.isbn_str)
	print(thebook.publishDate)

try:
	args.isbn_str
except:
	parser.print_help()

main()
