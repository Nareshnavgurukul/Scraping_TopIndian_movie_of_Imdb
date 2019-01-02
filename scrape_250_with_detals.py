from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_all_urls():
	link = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
	html = urlopen(link)
	Obj_soup = BeautifulSoup(html,"lxml")
	
	Object = Obj_soup.find_all("td",class_="titleColumn")
	linklist = []
	for i in Object:
		newurl = (i).a["href"]
		link = "https://www.imdb.com"+newurl#every time url change
		linklist.append(link)
	return(linklist)
get_all_urls()
url_list = get_all_urls()

def extract_movie_details(movie_url):
	index = 0
	for i in movie_url:
		index+=1
		html = urlopen(i)
		Obj_soup = BeautifulSoup(html,"lxml")
	
		dic_to_store_moviedeta = {"Name of movie":"","Director":"","Bio of the Movie":"","Runtime":"","URL of Poster":"","genre":"","Country":"","Language":""}
		genrelist=[]
		listdir = []
		moviedetail = []

		name = Obj_soup.find("div",class_="title_wrapper")
		Name = name.find("h1").get_text()
		Namemovie = Name.split()
		
		dic_to_store_moviedeta["Name of movie"] = Namemovie[0]

		poster = Obj_soup.find("div",class_="poster")#it have contain a tag with img src
		imgtag = (poster.find("img"))

		Subtext = Obj_soup.find("div",class_="subtext")#.a.get_text()
		subtext=Subtext.find_all("a")
			
			#below I have list of all anker tag 
		Subtext = Obj_soup.find("div",class_="subtext").time.get_text()
		Time = Subtext.strip().split()
		if len(Time) == 2:
			Timeh = Time[0][:-1]
			TimeM = Time[1][:-3]
			time = (int(Timeh)*60)+int(TimeM)
			dic_to_store_moviedeta["Runtime"]=str(time)+""+"min"

		if len(Time) == 1:
			Timeh = Time[0][:-1]
			time = int(Timeh)*60	
			dic_to_store_moviedeta["Runtime"]=str(time)+""+"min"

		
		dic_to_store_moviedeta["URL of Poster"] = imgtag["src"] #this is the url of poster

		direct = Obj_soup.find("div",class_="credit_summary_item")
		Alldirect = direct.find_all("a")

		for Namedir in Alldirect:
			listdir.append(Namedir.get_text())
		dic_to_store_moviedeta["Director"]=listdir
		listdir = []

		Bio = Obj_soup.find("div",class_="summary_text")
		dic_to_store_moviedeta["Bio of the Movie"]=Bio.get_text().strip()
		find_drc = Obj_soup.find("div",class_="subtext")
		listOfa = find_drc.find_all("a")#list of a tag
		
		for i in range(len(listOfa)-1):
			genrelist.append(listOfa[i].get_text())

		dic_to_store_moviedeta["genre"]=genrelist
			
		genrelist=[]

		country = Obj_soup.find_all("div",class_="txt-block")
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
		return(dic_to_store_moviedeta)
extract_movie_details(url_list)	




