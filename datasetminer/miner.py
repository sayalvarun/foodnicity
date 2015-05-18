import urllib2
from bs4 import BeautifulSoup
import time

URLS = {"http://allrecipes.com/Recipes/World-Cuisine/European/Main.aspx","http://allrecipes.com/Recipes/World-Cuisine/Asian/Main.aspx",
		"http://allrecipes.com/Recipes/World-Cuisine/Latin-American/Main.aspx","http://allrecipes.com/Recipes/World-Cuisine/Canadian/Main.aspx",
		"http://allrecipes.com/Recipes/World-Cuisine/Australian-and-New-Zealander/Main.aspx","http://allrecipes.com/Recipes/World-Cuisine/Middle-Eastern/Main.aspx",
		"http://allrecipes.com/Recipes/World-Cuisine/African/Main.aspx"}
NAMES = {"European","Asian","Latin-American","Canadian","Australian-and-New-Zealander","Middle-Eastern","African"}
BaseURL = "http://allrecipes.com/"

outfile = open('masterout.txt','w')

def parseLinkInfo(appendLink,url,name):
	parseUrl = url+appendLink
	
	write(name+":")
	parseHtml = urllib2.urlopen(parseUrl).read()
	pSoup = BeautifulSoup(parseHtml)
	rTitle = pSoup.find(id="itemTitle").get_text()
	print rTitle
	write(rTitle)
	write("")

	ingredients = pSoup.find_all("li",{"id":"liIngredient"})
	for ing in ingredients:
		amount = ing.find(id="lblIngAmount")
		name = ing.find(id="lblIngName")
		if(amount is not None and name is not None):
			write(amount.get_text())
			write(name.get_text())
	for i in range(2):
		write("")

def write(string):
	outfile.write(string.encode('utf8'))
	outfile.write("\n")


for url,name in map(None,URLS,NAMES):
	time.sleep(.1);
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)

	pageNum = 2 #Start looking for the next page at page 2, since page 1 is the default linked page
	nextLink = ["thing"] #Initialze the next link

	while nextLink:

		collectionlist = soup.find_all("div",id="divGridItemWrapper")

		for anchor in collectionlist:
			all_links = anchor.find_all("a",class_="img-link")
			for link in all_links:
				parseLinkInfo(link.get("href"), BaseURL, name)
		
		nextPageUrl = url+"?Page="+str(pageNum)+"#recipes"
		nextLink = soup.find_all("a",href=nextPageUrl)

		html = urllib2.urlopen(nextPageUrl).read()
		soup = BeautifulSoup(html)
		print nextLink
		print nextPageUrl
		pageNum = pageNum + 1

outfile.close()
