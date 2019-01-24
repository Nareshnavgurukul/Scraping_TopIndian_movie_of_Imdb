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

# import requests
# import json
# import os
# import random
# import pprint
# from bs4 import BeautifulSoup




# #Task 1 scrape_top_list
# def scrape_top_list():
# 	url = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
# 	html = requests.get(url)
# 	Obj_soup = BeautifulSoup(html.text,"html.parser")

# 	contain_data = Obj_soup.find("div",class_="lister")
# 	contain_var2 = contain_data.find("tbody",class_="lister-list")
# 	trs = contain_var2.find_all('tr')
# 	movies=[]
# 	eachMovie={"Position":"","name":0,"year_of_release":0,"Rating":0,"url":""}

# 	index=0
# 	for tr in trs:
# 		index+=1	
# 		name_enter = tr.find("td",class_="titleColumn")
# 		year_enter = tr.find("td",class_="titleColumn")
# 		rating_td = tr.find("td",class_="imdbRating")
# 		rating = tr.find("strong").get_text()
# 		rating=float(rating)
# 		name = name_enter.find("a").get_text()
# 		URL = name_enter.find("a")
# 		eachMovie["url"]="https://www.imdb.com"+URL["href"]

# 		Year = year_enter.find("span",class_="secondaryInfo").get_text()
# 		Year=Year[1:len(Year)-1]
# 		Year=int(Year)

# 		#every time our key value will change.
# 		eachMovie["name"]=name
# 		eachMovie["year_of_release"]=Year
# 		eachMovie["Position"]=index
# 		eachMovie["Rating"]=rating

# 		#here dec____ will append in the list.
# 		movies.append(eachMovie.copy())
# 		# eachMovie={"Position":"","name":0,"year_of_release":0,"Rating":0}# another way of movies.append(eachMovie.copy())
# 	store_data = open("information_of_movies.txt","w+")

# 	for i in movies:
# 		data = ''
# 		for j in i:	
# 			data = data+ str(i[j])+" "
# 		store_data.write(data + '\n\n')
# 	store_data.close()
# 	return(movies)
# Movies = scrape_top_list()

# #Task 2 group_by_year
# def group_by_year(movies):
# 	year_group=[]#it is using to store years
# 	list_of_year_movie=[]
# 	dec_years={}
# 	for year_movie in movies:
# 		YYY = year_movie["year_of_release"]
# 		if YYY not in year_group:
# 			year_group.append(YYY)

# 	for YY_year in year_group:
# 		dec_years[YY_year]=[]#here it is creating key name of year like Dic = {1971:[]}======>
# 	for fmm in movies:
# 		year = fmm["year_of_release"]
# 		for keyyear in dec_years:
# 			if keyyear == year:
# 				dec_years[keyyear].append(fmm)

# 	moviename = open("Group_by_year.txt","w+")
# 	dicname={}
# 	for i in dec_years:
# 		count = 0
# 		moviename.write(str(i)+"\n")
# 		for j in dec_years[i]:
# 			count+=1
# 			dicname=j
# 			data=str(count)+"."+dicname["name"]
# 			moviename.write(data+"\n")
# 	moviename.close()
# 	return(dec_years)# Movies name of all the same year==========
# dec_arg = group_by_year(Movies)

# # Task 3 group_by_decade
# def group_by_decade(movies):
# 	moviedec = {}
# 	list1 = []
# 	for index in movies:#years
# 		Mod = index%10
# 		decate = index-Mod
# 		if decate not in list1:
# 			list1.append(decate)#it is creating list of decates
# 	list1.sort()
# 	for i in list1:
# 		moviedec[i]=[]

# 	for i in moviedec:
# 		dec10 = i + 9
# 		for x in movies:
# 			if x <= dec10 and x>=i:
# 				for v in movies[x]:	
# 					moviedec[i].append(v)
# 	return(moviedec)					
# group_by_decade(dec_arg)



# # creating url of all top 250 movies task 4
# def get_all_urls():
# 	link = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
# 	html = requests.get(link)
# 	Obj_soup = BeautifulSoup(html.text,"html.parser")
# 	title = Obj_soup.title.get_text()
	
# 	Object = Obj_soup.find_all("td",class_="titleColumn")
# 	linklist = []
# 	for i in Object:
# 		newurl = (i).a["href"]
# 		link = "https://www.imdb.com"+newurl#every time url change
# 		linklist.append(link)
# 	return linklist
# url_list = get_all_urls()[:20]
# Top_250_URls = get_all_urls()#this variable for task 9


# # Task 4,8 and 9
# def extract_movie_details(movie_url):
# 	import time
# 	#creating ID.json file 135 to 141 till
# 	ID = ""
# 	for x in movie_url[27:]:
# 		if x != "/":
# 			ID+=x
# 		else:
# 			break
# 	#Task-8
# 	fileName = ID +".json"
# 	if os.path.exists("/home/naresh/Desktop/IMDB/DataIMDB_20/"+fileName):# if you are runimg this code so u have to change path of file
# 		Read = open("/home/naresh/Desktop/IMDB/DataIMDB_20/"+fileName)
# 		scraper = Read.read()
# 		return(scraper)
# 	scraper = None
# 	if scraper is None:# scraper = /home/naresh/Desktop/IMDB/DataIMDB_20/"+fileName
# 		#Task 9
# 		ran_time = random.randint(1,3)
# 		time.sleep(ran_time)
# 		#Task-4 
# 		html = requests.get(movie_url)
# 		Obj_soup = BeautifulSoup(html.text,"html.parser")
# 		dic_to_store_moviedeta = {"Name of movie":"","Director":"","Bio of the Movie":"","Runtime":"","URL of Poster":"","genre":"","Country":"","Language":""}
# 		genrelist=[]
# 		listdir = []
# 		moviedetail = []
# 		name = Obj_soup.find("div",class_="title_wrapper")
# 		Name = name.find("h1").get_text()
# 		Namemovie = Name.split()
# 		dic_to_store_moviedeta["Name of movie"] = "".join(Namemovie[:-1])
# 		poster = Obj_soup.find("div",class_="poster")#it have contain a tag with img src
# 		imgtag = (poster.find("img"))
# 		Subtext = Obj_soup.find("div",class_="subtext")#.a.get_text()
# 		subtext=Subtext.find_all("a")
			
# 		#below I have list of all anker tag 
# 		Subtext = Obj_soup.find("div",class_="subtext").time.get_text()
# 		Time = Subtext.strip().split()
# 		if len(Time) == 2:
# 			Timeh = Time[0][:-1]
# 			TimeM = Time[1][:-3]
# 			time = (int(Timeh)*60)+int(TimeM)
# 			dic_to_store_moviedeta["Runtime"]=str(time)+""+"min"

# 		if len(Time) == 1:
# 			Timeh = Time[0][:-1]
# 			time = int(Timeh)*60	
# 			dic_to_store_moviedeta["Runtime"]=str(time)+""+"min"

# 		dic_to_store_moviedeta["URL of Poster"] = imgtag["src"] #this is the url of poster

# 		direct = Obj_soup.find("div",class_="credit_summary_item")
# 		Alldirect = direct.find_all("a")

# 		for Namedir in Alldirect:
# 			listdir.append(Namedir.get_text())
# 		dic_to_store_moviedeta["Director"]=listdir
# 		listdir = []

# 		Bio = Obj_soup.find("div",class_="summary_text")
# 		dic_to_store_moviedeta["Bio of the Movie"]=Bio.get_text().strip()
# 		find_drc = Obj_soup.find("div",class_="subtext")
# 		listOfa = find_drc.find_all("a")#list of a tag
		
# 		for i in range(len(listOfa)-1):
# 			genrelist.append(listOfa[i].get_text())
# 		dic_to_store_moviedeta["genre"]=genrelist
	
# 		genrelist=[]
# 		country = Obj_soup.find_all("div",class_="txt-block")
# 		for count in country:
# 			h=count.find_all("h4")
# 			for m in h:
# 				if (m.get_text() == "Country:"):
# 					dic_to_store_moviedeta["Country"]=count.find("a").get_text()
# 					break
# 				if (m.get_text() == "Language:"):
# 					languages = count.find_all("a")
# 					lang = []
# 					for lan in languages:
# 						lang.append(lan.get_text())
# 					dic_to_store_moviedeta["Language"] = lang

# 					#Task-8 storing data into json file 
# 					fileName = ID +".json"
# 					file = open("/home/naresh/Desktop/IMDB/DataIMDB_20/"+fileName,"w+")# if you are runimg this code so u have to change path of file
# 					convert = json.dumps(dic_to_store_moviedeta)	
# 					file.write(convert)
# 					file.close()
# 	return(dic_to_store_moviedeta)# To scrape all 20 movie details you have to use print in place of return 
# extract_movie_details(url_list[0])#will scrape movie detail fron 1 to 20 only of each movie

# # Task 5
# movie = []
# def get_movie_list_details(movies_list):
# 	for url in movies_list:
# 		movie.append(extract_movie_details(url))
# 	return(movie)
# analyse = get_movie_list_details(url_list)

# # Task 6
# def analyse_movies_language(movies):
# 	lang_list = []
# 	languages = []
# 	landetail = {}
# 	for i in movies:
# 		dic = json.loads(i)
# 		for lang in dic["Language"]:
# 			lang_list.append(lang)
# 			if lang not in languages:
# 				languages.append(lang)

# 	for index in languages:
# 		count = 0
# 		landetail[index]=0
# 		for check in lang_list:
# 			if index == check:
# 				count+=1
# 				landetail[index]=count
# 	return(landetail)	
# analyse_movies_language(analyse)

# # Task 7 analyse_movies_directors
# def analyse_movies_directors(movies):
# 	Dirlist = []
# 	Directors = []
# 	Dirdetail = {}
# 	for i in movies:
# 		dic = json.loads(i)
# 		for k in (dic["Director"]):
# 			Dirlist.append(k)
# 			if k not in Directors:
# 				Directors.append(k)

# 	for index in Directors:
# 		count=0
# 		Dirdetail[index]=0
# 		for check in Dirlist:
# 			if check == index:
# 				count+=1
# 				Dirdetail[index] = count
# 	return(Dirdetail)
# analyse_movies_directors(analyse)

# # Task 9 it will scrape data from cache memory
# movie = []
# def get_movie_list_detailsimport requests
# from bs4 import BeautifulSoup

# def scrape_top_list():
# 	url = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
# 	html = requests.get(url)
# 	Obj_soup = BeautifulSoup(html.text,"html.parser")

# 	title = Obj_soup.title.get_text()#here it will assign   title value

# 	contain_data = Obj_soup.find("div",class_="lister")
# 	contain_var2 = contain_data.find("tbody",class_="lister-list")
# 	trs = contain_var2.find_all('tr')

# 	movies=[]
# 	eachMovie={"Position":"","name":0,"year_of_release":0,"Rating":0,"url":""}

# 	index=0
# 	for tr in trs:
# 		index+=1	
# 		name_enter = tr.find("td",class_="titleColumn")
# 		year_enter = tr.find("td",class_="titleColumn")
# 		rating_td = tr.find("td",class_="imdbRating")
# 		rating = tr.find("strong").get_text()
# 		rating=float(rating)
# 		name = name_enter.find("a").get_text()
# 		URL = name_enter.find("a")
# 		eachMovie["url"]="https://www.imdb.com"+URL["href"]

# 		Year = year_enter.find("span",class_="secondaryInfo").get_text()
# 		Year=Year[1:len(Year)-1]
# 		Year=int(Year)

# 		#every time our key value will change.
# 		eachMovie["name"]=name
# 		eachMovie["year_of_release"]=Year
# 		eachMovie["Position"]=index
# 		eachMovie["Rating"]=rating

# 		#here dec____ will append in the list.
# 		movies.append(eachMovie.copy())
# 		# eachMovie={"Position":"","name":0,"year_of_release":0,"Rating":0}# another way of movies.append(eachMovie.copy())

# 	store_data = open("information_of_movies.txt","w+")

# 	for i in movies:
# 		data = ''
# 		for j in i:	
# 			data = data+ str(i[j])+" "
# 		store_data.write(data + '\n\n')
# 	store_data.close()

# 	return(movies)
# scrape_top_list()#scraped all data
# Movies = scrape_top_list()


# def group_by_year(movies):
# 	year_group=[]#it is using to store years
# 	list_of_year_movie=[]
# 	dec_years={}
# 	for year_movie in movies:
# 		YYY = year_movie["year_of_release"]
# 		if YYY not in year_group:
# 			year_group.append(YYY)

# 	for YY_year in year_group:
# 		dec_years[YY_year]=[]#here it is creating key name of year like Dic = {1971:[]}======>

# 	for fmm in movies:
# 		year = fmm["year_of_release"]
# 		for keyyear in dec_years:
# 			if keyyear == year:
# 				dec_years[keyyear].append(fmm)

# 	moviename = open("Group_by_year.txt","w+")
# 	dicname={}
# 	for i in dec_years:
# 		count = 0
# 		moviename.write(str(i)+"\n")

# 		for j in dec_years[i]:
# 			count+=1
# 			(movies_list):
# 	import time
# 	for url in movies_list:
# 		ran_time = random.randint(1,3)
# 		movie.append(extract_movie_details(url))#using task 4 and 8
# 		time.sleep(ran_time)
# 	return(movie)
# analyse_movies = get_movie_list_details(Top_250_URls)
# # pprint.pprint(analyse_movies)

# #   Task 10
#  def  analyse_language_and_directors(movies_list):
#  	directors_dic = {}
#  	for movi in movies_list:
#  		movie = json.loads(movi)
#  		for director in movie['Director']:
#  			directors_dic[director] = {}

#  	for list_dic in movies_list:
#  		dic = json.loads(list_dic)
#  		for director in directors_dic:
#  			if director in dic['Director']:
#  				for language in dic['Language']:
#  					directors_dic[director][language] = 0

#  	for i in movies_list:#[{},{}]
#  		dic = json.loads(i)#converting into {}
#  		for director in directors_dic:#main {jveni{language:9}}
#  			if director in dic['Director']:
#  				for language in dic['Language']:
#  					directors_dic[director][language] += 1
#  	return directors_dic
#  director_by_language = analyse_language_and_directors(analyse_movies)
# #  pprint.pprint(directors_dic) 

# # Task 11
# def analyse_movies_genre(movies_list):
# 	Genres = {}
# 	M_list = []
# 	for i in movies_list:
# 		Dict = json.loads(i)
# 		M_list.append(Dict)
# 	for dic in M_list:
# 		for genre in dic["genre"]:
# 			if genre not in Genres:
# 				Genres[genre] = 0
# 	for g in Genres:
# 		for i in M_list:
# 			for a in i["genre"]:
# 				if g == a:
# 					Genres[g]+=1
# 	return(Genres)
# movies_genre = analyse_movies_genre(analyse_movies)
# # pprint.pprint(movies_genre)

