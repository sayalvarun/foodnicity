import collections,re

f = open("masteroutMaster.txt","r")

east = ""
west = ""

countryLine = True
isEast = True
spaceSeen = False

def isEastCountry(line):
	if line == 'Australian-and-New-Zealander:\n':
		return True
	elif line == 'Latin-American:\n':
		return False
	elif line == 'Asian:\n':
		return True
	elif line == 'African:\n':
		return False
	elif line == 'European:\n':
		return True
	elif line == 'Middle-Eastern:\n':
		return True
	elif line == 'Canadian:\n':
		return False


for line in f:
	if(countryLine):
		print "line is: "+line
		if(isEastCountry(line)):
			print "This is an eastern"
			isEast = True
		else:
			print "This is western"
			isEast = False

		countryLine = False
		spaceSeen = False
	elif(line.isspace()):
		if(spaceSeen):
			countryLine = True
			spaceSeen = False
		else:
			spaceSeen = True
	else:
		if(isEast):
			east+=line
		else:
			west+=line

		spaceSeen = False


bagOfWords = collections.Counter(re.findall(r'\w+', txt)

