from urllib.request import urlopen
from bs4 import BeautifulSoup

link = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
def get_movie_details(movie_url):
	html = urlopen(movie_url)
	Obj_soup = BeautifulSoup(html,"lxml")
	title = Obj_soup.title.get_text()
	
	Object = Obj_soup.find_all("td",class_="titleColumn")
	
	
	dic_to_store_moviedeta = {"Name of movie":"","Director":"","Bio of the Movie":"","Runtime":"","URL of Poster":"","genre":"","Country":"","Language":""}
	genrelist=[]
	listdir = []
	index = 0
	for i in Object:
		index+=1
		name = i.a.get_text()

		dic_to_store_moviedeta["Name of movie"] = name
		newurl = (i).a["href"]
		link = "https://www.imdb.com"+newurl#every time url change

		obj_html = urlopen(link)
		obj_on_work = BeautifulSoup(obj_html,"lxml")

		poster = obj_on_work.find("div",class_="poster")#it have contain a tag with img src
		imgtag = (poster.find("img"))

		Subtext = obj_on_work.find("div",class_="subtext")#.a.get_text()
		subtext=Subtext.find_all("a")
		
		#below I have list of all anker tag 
		Subtext = obj_on_work.find("div",class_="subtext").time.get_text()
		dic_to_store_moviedeta["Runtime"] = Subtext.strip()
		dic_to_store_moviedeta["URL of Poster"] = imgtag["src"] #this is the url of poster

		direct = obj_on_work.find("div",class_="credit_summary_item")
		Alldirect = direct.find_all("a")

		for Namedir in Alldirect:
			listdir.append(Namedir.get_text())
		dic_to_store_moviedeta["Director"]=listdir
		listdir = []


		Bio = obj_on_work.find("div",class_="summary_text")
		dic_to_store_moviedeta["Bio of the Movie"]=Bio.get_text().strip()

		find_drc = obj_on_work.find("div",class_="subtext")
		listOfa = find_drc.find_all("a")#list of a tag
	
		for i in range(len(listOfa)-1):
			genrelist.append(listOfa[i].get_text())

		dic_to_store_moviedeta["genre"]=genrelist
		
		genrelist=[]

		country = obj_on_work.find_all("div",class_="txt-block")
		for count in country:
			h=count.find_all("h4")
			for m in h:
				if (m.get_text() == "Country:"):
					dic_to_store_moviedeta["Country"]=count.find("a").get_text()
					break
				if (m.get_text() == "Language:"):
					languages = count.find_all("a")
					lang = []
					for lan in languages:
						lang.append(lan.get_text())
					dic_to_store_moviedeta["Language"] = lang

		print(dic_to_store_moviedeta,"\n")
get_movie_details(link)

