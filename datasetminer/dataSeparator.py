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

master = open("masteroutMASTER.txt","r")

masterContents = master.read();

recipes = masterContents.split("\n\n\n")

for rec in recipes:
	recipeLines = rec.split("\n")
	


