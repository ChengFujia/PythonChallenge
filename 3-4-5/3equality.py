#-*- coding:utf-8 -*-

import string
text = open("character.txt").read().rstrip()

def my_solution(text):
	equality = ''
	for i in range(len(text)-8):
		#NOTICE: there is a EXACTLY in tips
		if text[i] in string.lowercase and text[i+1] in string.uppercase and text[i+2] in string.uppercase and\
		 text[i+3] in string.uppercase and text[i+4] in string.lowercase and text[i+5] in string.uppercase and\
		 text[i+6] in string.uppercase and text[i+7] in string.uppercase and text[i+8] in string.lowercase:
			equality += text[i+4]
	print equality

import re
def shiyanlou_solution(text):
	print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text))

if __name__ == "__main__":
	#my_solution(text)
	shiyanlou_solution(text)
