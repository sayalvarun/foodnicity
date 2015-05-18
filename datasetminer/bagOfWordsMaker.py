import collections,re

f = open("masteroutMASTER.txt","r")

east = ""
west = ""

countryLine = True
isEast = True
spaceSeen = False

def isEastCountry(line):
	if 'Australian-and-New-Zealander' in line:
		return True
	elif'Latin-American:' in line:
		return False
	elif 'Asian:' in line:
		return True
	elif 'African:' in line:
		return False
	elif 'European' in line:
		return True
	elif'Middle-Eastern' in line:
		return True
	elif 'Canadian' in line:
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


#bagOfWords = collections.Counter(re.findall(r'\w+', txt))
#print bagOfWords
