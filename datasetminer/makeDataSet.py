#! /usr/local/bin/python
import random

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
east_file = open("East.txt", "w")
west_file = open("West.txt", "w")

ingredients=[]
skip_line = False

EAST = 0
WEST = 1

n = random.randint(5, 10)
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

			print ingredients[0],EAST,WEST
			#if eastern recipe
			if int(ingredients[0]) == EAST:
				print "east"
				#increment eastern recipe count
				east_count += 1
				#if right time, put in East file
				if east_count%n == 0:
					east_file.write(ingredients_str)
				#otherwise, just pool it in w/ the rest
				else:
					output_file.write(ingredients_str);

			#if western recipe
			if int(ingredients[0]) == WEST:
				print "west"
				#increment western recipe count
				west_count += 1
				#if right time, put in West file
				if west_count%n == 0:
					west_file.write(ingredients_str)
				#otherwise, just pool it in w/ the rest
				else:
					output_file.write(ingredients_str);

		#clear the list for the prev. recipe
		del ingredients[:]

		#give the region
		if isEastCountry(line):
			line = str(EAST)
		else:
			line = str(WEST)
		
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

print str(east_count)+"vs"+str(west_count)

#close files
input_file.close()
output_file.close()
east_file.close()
west_file.close()