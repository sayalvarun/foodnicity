import collections,re
'''
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
'''

#open dataset file
data = open("dataset.txt", "r")
output = open("features.txt", "w")
ingredients_map = {}

NEUTRAL = -1
EAST = 0
WEST = 1

for line in data:
	line = line.split(',')
	for i in range(1, len(line)):
		#remove trailing whitespace
		line[i] = line[i].rstrip()

		#if the ingredient doesnt exist in the map yet, insert the entry
		if line[i] not in ingredients_map:
			ingredients_map[line[i]] = [0,0]

		#increment the count for the proper cuisine
		ingredients_map[line[i]][int(line[0])]+=1

#close file
data.close()

#go through all the ingredients
for key in ingredients_map:
	east = ingredients_map[key][EAST]
	half_east = east/2
	west = ingredients_map[key][WEST]
	half_west = west/2

	cuisine = NEUTRAL
	if half_east >= west:
		cuisine = EAST
	if half_west >= east:
		cuisine = WEST

	print key,ingredients_map[key],cuisine
	if cuisine != NEUTRAL:
		output.write(key+","+str(cuisine)+"\n")