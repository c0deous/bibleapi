#BibleApi by Jesse Wallace (c0deous) <jessewallaceblog.wordpress.com> <c0deous.net>
#You may run, modify, use commercially, and distribute this program freely.
#This comes with ABSOLOUTELY NO WARRANTY, to the extent permitted by applicable law.
from bottle import route, run
from xml.dom.minidom import parse, parseString

apiusage = '''API Usage

Single Verse: address:port/bookid/chapter/verse
2 verses from the same chapter and book: address:port/bookid/chapter/verse1/verse2
NOTE: The bookid is the index number of the bible book where genesis would be 1 and exodus would
NOTE: be 2, leviticus 3 and so on...

'''
print('Loading bible.xml... this may take a moment') #loading message
dom = parse('db/bible.xml') #open bible.xml
print('Done!')#finished loading
def bibleRef(bookid, chapter, verse): #define parameters
	try:
		element = dom.getElementsByTagName('BIBLEBOOK') #get all the books
		book = element[int(bookid) - 1] #single out requested book
		chapterelement = book.getElementsByTagName('CHAPTER') #get all of the chapters
		chpter = chapterelement[int(chapter) - 1] #single out requested chapter
		verseelement = chpter.getElementsByTagName('VERS') #get all verses
		vrse = verseelement[int(verse) - 1].firstChild.nodeValue #single out requested verse
	except IndexError: #if the verse, chapter, or book doesn't exist return a 'Not Found' message
		print('Not Found')
		return('Not Found')
	return(vrse) #If it doesn't get any errors then return the text of the verse


@route('/') #set route
def homepage():
	return 'KJV Bible API' #return a simple message

@route('/<bookid>/<chapter>/<verse>')#set route
def verselookup(bookid="1", chapter="1", verse="1"):
	return verse + " " + bibleRef(bookid, chapter, verse) #call the bibleRef function

@route('/<bookid>/<chapter>/<verse1>/<verse2>')#set route
def multiverselookup(bookid="1", chapter="1", verse1="1", verse2="2"):
	return verse1 + " " + bibleRef(bookid, chapter, verse1) + " " + verse2 + " " +  bibleRef(bookid, chapter, verse2)
	# call the bibleRef function twice and join the two verses with their corresponding number

@route('/info')
def info():
	info = dom.getElementsByTagName('INFORMATION')
	for node in info:
		return node.toxml()

print(' ')#empty space
print('Bible API by Jesse Wallace (c0deous) <jessewallaceblog.wordpress.com> <c0deous.net>') #attribution
print(' ')#empty space
run(host='0.0.0.0', port=5942, debug=False) #start server
print(' ')#empty space
print('Quitting...')# send a quitting message
