#-*- coding:utf-8 -*-
import string
text = open("mess.txt").read()

def shiyanlou_solution(text):
	s = filter(lambda x:x in string.letters,text)
	print s

def std_solution(text):
	s =''.join([line.rstrip() for line in text])
	occ = {}
	for c in s:
		occ[c] = occ.get(c,0) + 1
	/*average frequence number*/
	avg = len(s)//len(occ)
	print ''.join([c for c in s if occ[c] < avg])

if __name__ == "__main__":
	#shiyanlou_solution(text)
	std_solution(text)


