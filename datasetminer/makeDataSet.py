#! /usr/local/bin/python
import random

'''
	checks if a string contains numbers
	used to filter out measurements
'''
def contains_digit(string):
	return any(char.isdigit() for char in string)

def getCuisine(line):
	if 'Australian-and-New-Zealander' in line:
		return EAST
	elif'Latin-American:' in line:
		return WEST
	elif 'Asian:' in line:
		return EAST
	elif 'African:' in line:
		return WEST
	elif 'European' in line:
		return WEST
	elif'Middle-Eastern' in line:
		return EAST
	elif 'Canadian' in line:
		return WEST


#open files
input_file = open("masteroutMASTER.txt","r")
output_file = open("Holdout3.txt", "w")
east_file = open("Data/East/East.txt", "w")
west_file = open("Data/West/West.txt", "w")

ingredients=[]
skip_line = False

EAST = 0
WEST = 1

n = 2#random.randint(1, 4)
east_count = 0
west_count = 0

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
			#if eastern recipe
			if int(ingredients[0]) == EAST:
				#increment eastern recipe count
				east_count += 1
				#if right time, put in East file
				if east_count%n != 0:
					east_file.write(ingredients_str)
				#otherwise, just pool it in w/ the rest
				else:
					output_file.write(ingredients_str);

			#if western recipe
			if int(ingredients[0]) == WEST:
				#increment western recipe count
				west_count += 1
				#if right time, put in West file
				if west_count%n != 0:
					west_file.write(ingredients_str)
				#otherwise, just pool it in w/ the rest
				else:
					output_file.write(ingredients_str);

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
east_file.close()
west_file.close()