import re
import zipfile

#Regular Unzip: unzip + filename
#Other Unzip(with descirtion): unzip -l + filename

#According to re.. to find number(\d)
findnothing = re.compile(r'Next nothing is (\d+)').match
comments = []
z = zipfile.ZipFile("channel.zip",'r')
seed = '90052'
while True:
	fname = seed + '.txt'
	comments.append(z.getinfo(fname).comment)
	guts = z.read(fname)
	#text = open(fname,'r').read()
	m = findnothing(guts)
	if m:
		seed = m.group(1)#first match group
	else:
		#print text
		break

print "".join(comments)


