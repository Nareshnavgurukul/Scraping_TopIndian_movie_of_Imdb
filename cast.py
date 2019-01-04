from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_all_urls():
	link = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
	html = urlopen(link)
	Obj_soup = BeautifulSoup(html,"lxml")
	title = Obj_soup.title.get_text()
	
	Object = Obj_soup.find_all("td",class_="titleColumn")
	linklist = []
	for i in Object:
		newurl = (i).a["href"]
		link = "https://www.imdb.com"+newurl#every time url change
		linklist.append(link)
	return linklist
cast_url = get_all_urls()

def cats(movies):
	All_cast = []
	for i in movies:
		html = urlopen(i)
		Obj_soup = BeautifulSoup(html,"lxml")
		name = Obj_soup.find("div",class_="title_wrapper")
		Name = name.find("h1").get_text()
		Namemovie = Name.split()
		moviename = "".join(Namemovie[:-1])
		Dic_={}
		listOfcast = []
		castdiv = Obj_soup.find("table")
		cast = castdiv.find_all("img")
		for x in cast:
			listOfcast.append(x["alt"])
		Dic_[moviename]=listOfcast
		All_cast.append(Dic_)
	return(All_cast)
print(cats(cast_url))

