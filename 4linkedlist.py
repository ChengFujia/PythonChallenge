#-*- coding:utf-8 -*-
import urllib
import urllib2

data = {}#key-value pairs
number = '12345'

def shiyanlou_solution(number):
	#Recycle 400 times
	for i in range(400):
		data["nothing"] = number
		url_values = urllib.urlencode(data)
		url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
		full_url = url+'?'+url_values

		foo = urllib2.urlopen(full_url)
		foo = foo.read()
		print foo
		foo = foo.split(" ")
		new_lastone = foo[len(foo)-1]
		if "html" in new_lastone:
                        print "FINISHED"
                        break
		elif new_lastone.isdigit():
			number = new_lastone
		else:
			number = str(int(number)/2)

import re
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = "12345"

search = re.compile("(\d+)$")
search_html = re.compile("\.html$")

def std_solution(nothing):
	for i in xrange(400):
		print "%s: "%nothing
		line = urllib.urlopen("%s%s"%(url,nothing)).read()
		print line
		if search_html.findall(line):
                        print "FINISHED"
			break
		match = search.findall(line)
		if match:
			nothing =match[0]
		else:
			nothing = str(int(nothing)/2)
	
if __name__ == "__main__":
	#shiyanlou_solution(number)
	std_solution(nothing)

