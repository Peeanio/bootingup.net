#!/usr/bin/python

'''
Author: Max Russell, max@theguards.net
tool to work with openlibary api 
'''
import requests
import json

def get_book_info():
	#uses the ISBN to get information on book from openlibrary 
	isbn = str(9781492051367)
	#get complete payload
	payload = {'bibkeys': 'ISBN:' + isbn, 'format': 'json', 'jscmd': 'details'}
	r = requests.get('https://openlibrary.org/api/books', params=payload)
	y = r.json()
	
	global general_json
	global detail_json
	general_json = y['ISBN:9781492051367']
	detail_json = general_json['details']
#print(z['authors'])
get_book_info()
print(detail_json)
class Book():
	#load up a book with data from the API
	def __init__(self, isbn):
		self.isbn = isbn
		self.numOfPages = detail_json["number_of_pages"]


print('now for the show..."'+ '\n' + '\n')

thebook = Book(str(9781492051367))
print(thebook.numOfPages)
