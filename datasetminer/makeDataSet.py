#! /usr/local/bin/python

#############################################################################################################
# This file is used to split up the masteroutMaster file into 3 disjoint									#
# sections: east training data, west training data, and holdout test data 								   	#
#############################################################################################################

import random

'''
	checks if a string contains numbers
	used to filter out measurements
'''
def contains_digit(string):
	return any(char.isdigit() for char in string)

def getCuisine(line):
	if 'African' in line:
		return WEST
	elif 'Asian' in line:
		return EAST
	elif 'Australian-and-New-Zealander' in line:
		return EAST
	elif 'Canadian' in line:
		return WEST
	elif 'European' in line:
		return EAST
	elif'Latin-American' in line:
		return WEST
	elif'Middle-Eastern' in line:
		return EAST


#open files
input_file = open("masteroutMASTER.txt","r")
output_file = open("Holdout.txt", "w")
e_file = open("2CatData/East/East.txt", "w")
w_file = open("2CatData/West/West.txt", "w")

ingredients=[]
skip_line = False

EAST = 0
WEST = 1

n = 3#random.randint(1, 4)
counts = [0] * (WEST+1)

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
				if int(ingredients[0]) == EAST:
					e_file.write(ingredients_str)

				#if asian recipe, write to asian file
				if int(ingredients[0]) == WEST:
					w_file.write(ingredients_str)

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
e_file.close()
w_file.close()