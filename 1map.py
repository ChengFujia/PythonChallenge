#-*- coding:utf-8 -*-

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
tips = "now apply on the url"

def shiyanlou_solution(text):
	new_text = ''
	for each in text:
		if each >='a' and each<='z':
			new_text+= chr((ord(each)+2-ord('a'))%26+ord('a'))
		else:
			new_text+=each
	print new_text

import string
def std_solution(text):
	table = string.maketrans(string.ascii_lowercase,
				string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
	print string.translate(text,table)

if __name__=="__main__":
	#shiyanlou_solution(text)
	#shiyanlou_solution("map")
	std_solution(text)
	std_solution("map")
		
