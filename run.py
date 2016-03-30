import sys
from bs4 import BeautifulSoup
import requests
import urllib2

#myText = "Hello i am trying to test this stupid code"

if(len(sys.argv) != 2):
	print "Please check the argument again. For more help visit : https://github.com/srivas15/thesaurus"
file = open(str(sys.argv[1]), 'r')
myText = file.read()
print myText

words = myText.split()

print words

urlStart = 'http://thesaurus.com/browse/'
urlEnd = '?s=t'

finalText = ""

dontReplace = ['what', 'why', 'who', 'when', 'where', 'was']

for word in words:
	word = word.replace(".", "")
	word = word.replace("'", "")
	word = word.replace(",", "")
	if(len(word) < 3 or word in dontReplace):
		thesaurus = word
	else:
		url = urlStart+word+urlEnd
		print url
		
		var = requests.get(url)
		html = urllib2.urlopen(var.url).read()
		soup = BeautifulSoup(html, "html.parser")
		
		content = (soup.find("div", {"class" : "relevancy-list"})).find("ul")
		#print content
		thesaurus = (content.find("li")).getText()
		thesaurus = thesaurus[:-4]
		#print thesaurus
		#break
	finalText = finalText + " " + thesaurus

finalText = finalText[1:]
print finalText
