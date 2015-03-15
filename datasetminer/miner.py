import urllib2
from bs4 import BeautifulSoup
import time

URLS = {"http://allrecipes.com/Recipes/World-Cuisine/European/Main.aspx","http://allrecipes.com/Recipes/World-Cuisine/Asian/Main.aspx",
		"http://allrecipes.com/Recipes/World-Cuisine/Latin-American/Main.aspx","http://allrecipes.com/Recipes/World-Cuisine/Canadian/Main.aspx",
		"http://allrecipes.com/Recipes/World-Cuisine/Australian-and-New-Zealander/Main.aspx","http://allrecipes.com/Recipes/World-Cuisine/Middle-Eastern/Main.aspx",
		"http://allrecipes.com/Recipes/World-Cuisine/African/Main.aspx"}
NAMES = {"European","Asian","Latin-American","Canadian","Australian-and-New-Zealander","Middle-Eastern","African"}
BaseURL = "http://allrecipes.com/"

def parseLinkInfo(appendLink,url,name):
	parseUrl = url+appendLink
	
	print name+":"
	parseHtml = urllib2.urlopen(parseUrl).read()
	pSoup = BeautifulSoup(parseHtml)
	print pSoup.find(id="itemTitle").get_text()
	print ""

	ingredients = pSoup.find_all("li",{"id":"liIngredient"})
	for ing in ingredients:
		amount = ing.find(id="lblIngAmount")
		name = ing.find(id="lblIngName")
		if(amount is not None and name is not None):
			print amount.get_text()
			print name.get_text()
	for i in range(3):
		print ""

for url,name in map(None,URLS,NAMES):
	time.sleep(.1);
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	collectionlist = soup.find_all("div",id="divGridItemWrapper")

	for anchor in collectionlist:
		all_links = anchor.find_all("a",class_="img-link")
		for link in all_links:
			parseLinkInfo(link.get("href"), BaseURL, name)
