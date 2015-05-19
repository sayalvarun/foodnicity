#! /usr/local/bin/python
import random

'''
	checks if a string contains numbers
	used to filter out measurements
'''
def contains_digit(string):
	return any(char.isdigit() for char in string)

def getCuisine(line):
	if 'African' in line:
		return AFRICAN
	elif 'Asian' in line:
		return ASIAN
	elif 'Australian-and-New-Zealander' in line:
		return AUSSIE
	elif 'Canadian' in line:
		return CANADIAN
	elif 'European' in line:
		return EUROPEAN
	elif'Latin-American' in line:
		return LATINO
	elif'Middle-Eastern' in line:
		return BROWN


#open files
input_file = open("masteroutMASTER.txt","r")
output_file = open("Holdout3.txt", "w")
afr_file = open("Data/African/African.txt", "w")
asn_file = open("Data/Asian/Asian.txt", "w")
aus_file = open("Data/Australian-and-New-Zealander/Australian-and-New-Zealander.txt", "w")
can_file = open("Data/Canadian/Canadian.txt", "w")
eur_file = open("Data/European/European.txt", "w")
lat_file = open("Data/Latin-American/Latin-American.txt", "w")
bwn_file = open("Data/Middle-Eastern/Middle-Eastern.txt", "w")

ingredients=[]
skip_line = False

AFRICAN = 0
ASIAN = 1
AUSSIE = 2
CANADIAN = 3
EUROPEAN = 4
LATINO = 5
BROWN = 6

n = 2#random.randint(1, 4)
counts = [0] * (BROWN+1)

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
			ingredients_str = ",".join(ingredients)+"\n"
			print ingredients

			counts[int(ingredients[0])] += 1
			if (counts[int(ingredients[0])]) % n == 0:
				output_file.write(ingredients_str);
			else:
				ingredients_str = ingredients_str.split(",", 1)[1]
				#if african recipe, write to african file
				if int(ingredients[0]) == AFRICAN:
					afr_file.write(ingredients_str)

				#if asian recipe, write to asian file
				if int(ingredients[0]) == ASIAN:
					asn_file.write(ingredients_str)

				#if aussie recipe, write to aussie file
				if int(ingredients[0]) == AUSSIE:
					aus_file.write(ingredients_str)

				#if canadian recipe, write to canadian file
				if int(ingredients[0]) == CANADIAN:
					can_file.write(ingredients_str)

				#if european recipe, write to european file
				if int(ingredients[0]) == EUROPEAN:
					eur_file.write(ingredients_str)

				#if latino recipe, write to latino file
				if int(ingredients[0]) == LATINO:
					lat_file.write(ingredients_str)

				#if brown recipe, write to brown file
				if int(ingredients[0]) == BROWN:
					bwn_file.write(ingredients_str)

		#clear the list for the prev. recipe
		del ingredients[:]

		#give the region
		line = str(getCuisine(line))
		
		ingredients.append(line)
		#skip the line; next line is recipe name
		skip_line = True
		continue

	#if there is a comma, only things before the first comma is an ingredient
	line = line.split(",", 1)[0]

	#add line to ingredients list if it's not blank and isnt a measurement
	if line != "" and not contains_digit(line):
		ingredients.append(line);

output_file.write(",".join(ingredients))

#close files
input_file.close()
output_file.close()
afr_file.close()
asn_file.close()
can_file.close()
eur_file.close()
lat_file.close()
bwn_file.close()