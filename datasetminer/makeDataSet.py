#! /usr/local/bin/python

'''
	checks if a string contains numbers
	used to filter out measurements
'''
def contains_digit(string):
	return any(char.isdigit() for char in string)

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

#open files
input_file = open("masteroutMASTER.txt","r")
output_file = open("dataset.txt", "w")

ingredients=[];
skip_line = False;

#read input file
for line in input_file:
	#don't bother w/ this line if told to skip
	if skip_line:
		skip_line = False
		continue

	#get rid of the trailing whitespace
	line = line.rstrip()

	#there's a colon in the line => country of orign
	if ":" in line:
		#only print if there are ingredients...
		if len(ingredients) != 0:
			output_file.write(",".join(ingredients)+"\n")

		#clear the list for the prev. recipe
		del ingredients[:]

		#give the region
		if isEastCountry(line):
			line = "east"
		else:
			line = "west"

		#skip the line; next line is recipe name
		skip_line = True

	#add line to ingredients list if it's not blank and isnt a measurement
	if line != "" and not contains_digit(line):
		ingredients.append(line);

output_file.write(",".join(ingredients))

#close files
input_file.close()
output_file.close()