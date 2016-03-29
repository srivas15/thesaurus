myText = "Hello i am trying to test this stupid code"

print myText

words = myText.split()

print words

urlStart = 'http://thesaurus.com/browse/'
urlEnd = '?s=t'

for word in words:
	url = urlStart+word+urlEnd
	print url
