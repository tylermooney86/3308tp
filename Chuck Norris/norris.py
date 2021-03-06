"""this file pulls a random chuck norris joke off of the internet and writes it to a file."""

import urllib
import json
from pprint import pprint
from BeautifulSoup import BeautifulSoup


def generateJoke():

	file = open("norris.txt", 'r+')

	file.truncate()

	link = "http://api.icndb.com/jokes/random"
	f = urllib.urlopen(link)

	j = json.load(urllib.urlopen(link))

	joke = j['value']['joke']

	decode = str(BeautifulSoup(joke, convertEntities=BeautifulSoup.HTML_ENTITIES))

	file.write(decode)

	file.close
