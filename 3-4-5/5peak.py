import pickle

data = pickle.load(open("banner.p","rb"))
'''
#output directly
for each in data:
	print each
'''

#output decorated but not beautiful  (shiyanlou_solution)
for each in data:
	print "".join([i[0]*i[1] for i in each])

#output decroted to character picture  (std_solution)
import pprint
from PIL import Image,ImageDraw

im = Image.new("1",(95,24))
draw = ImageDraw.Draw(im)
line = 0

for i in data:
	xpos = 0
	for j in i:
		if j[0] == " ":
			draw.line([(xpos,line),(xpos+j[1],line)],255)
		xpos += j[1]
	line += 1
im.save("banner.bmp")
	

