from urllib.request import urlopen
from bs4 import BeautifulSoup

#step 1
# In the first step it have contain all the details of movie
#{'name': 'Anand', 'year_of_release': 1971, 'position': 1, 'rating': 8.7} , {}, {}, {}, {}]
# 1. year_of_release should be an integer.
# 2. positon should be an integer.
# 3. rating should be a float.
# 4. name should be a string. 
#
#Step 2
#{
# 1956: [
#   {'name': 'Koi movie ka naam', 'year_of_release': 1956, 'position': 1, 'rating': 8.7},
#   {'name': 'Kuch aur naam', 'year_of_release': 1956, 'position': 4, 'rating': 8.7}],
# 1959: [
# {'name': 'Koi movie ka naam 2', 'year_of_release': 1959, 'position':34, 'rating': 8.7}]}

# step 3
# 1.1960 se 1969 tak ke beech ke saare saal 1960s ke decade mein aate hain.
# 2. 1970 se 1979 tak ke beech ke saare saal 1970s ke decade mein aate hain.
# 3. 1980 se 1989 tak ke beech ke saare saal 1980s ke decade mein aate hain.
# 4. 2000 se 2009 tak ke beech ke saare saal 2000s ke decade mein aate hain.
# 

def scrape_top_list():
	url = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
	html = urlopen(url)
	Obj_soup = BeautifulSoup(html,"lxml")

	title = Obj_soup.title.get_text()#here it will assign   title value

	contain_data = Obj_soup.find("div",class_="lister")
	contain_var2 = contain_data.find("tbody",class_="lister-list")
	trs = contain_var2.find_all('tr')

	movies=[]
	eachMovie={"Position":"","name":0,"year_of_release":0,"Rating":0,"url":""}

	index=0
	for tr in trs:
		index+=1	
		name_enter = tr.find("td",class_="titleColumn")
		year_enter = tr.find("td",class_="titleColumn")
		rating_td = tr.find("td",class_="imdbRating")
		rating = tr.find("strong").get_text()
		rating=float(rating)
		name = name_enter.find("a").get_text()
		URL = name_enter.find("a")
		eachMovie["url"]="https://www.imdb.com"+URL["href"]

		Year = year_enter.find("span",class_="secondaryInfo").get_text()
		Year=Year[1:len(Year)-1]
		Year=int(Year)

		#every time our key value will change.
		eachMovie["name"]=name
		eachMovie["year_of_release"]=Year
		eachMovie["Position"]=index
		eachMovie["Rating"]=rating

		#here dec____ will append in the list.
		movies.append(eachMovie.copy())
		# eachMovie={"Position":"","name":0,"year_of_release":0,"Rating":0}# another way of movies.append(eachMovie.copy())

	store_data = open("information_of_movies.txt","w+")

	for i in movies:
		data = ''
		for j in i:	
			data = data+ str(i[j])+" "
		store_data.write(data + '\n\n')
	store_data.close()

	return(movies)
print(scrape_top_list())#scraped all data
print("\n")

def group_by_year(movies):
	year_group=[]#it is using to store years
	list_of_year_movie=[]
	dec_years={}
	for year_movie in movies:
		YYY = year_movie["year_of_release"]
		if YYY not in year_group:
			year_group.append(YYY)
	for YY_year in year_group:
		dec_years[YY_year]=[]#here it is creating key name of year like Dic = {1971:[]}======>

	for fmm in movies:
		year = fmm["year_of_release"]
		for keyyear in dec_years:
			if keyyear == year:
				dec_years[keyyear].append(fmm)
	moviename = open("Group_by_year.txt","w+")
	dicname={}
	for i in dec_years:
		count = 0
		moviename.write(str(i)+"\n")
		for j in dec_years[i]:
			count+=1
			dicname=j
			data=str(count)+"."+dicname["name"]
			moviename.write(data+"\n")
	moviename.close()
	return(dec_years)# Movies name of all the same year==========
movies = scrape_top_list()
print(group_by_year(movies))
print("\n")

def group_by_decade(movies):
	movies_by_year = group_by_year(movies)
	moviedec = {}
	list1 = []
	for index in movies_by_year:#years
		Mod = index%10
		decate = index-Mod
		if decate not in list1:
			list1.append(decate)#it is creating list of decates
	for i in list1:
		moviedec[i]=[]
	for i in moviedec:
		dec10 = i + 9
		for x in movies_by_year:
			if x <= dec10 and x>=i:
				for v in movies_by_year[x]:	
					moviedec[i].append(v)
	return(moviedec)					
print(group_by_decade(movies))


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

url_list = get_all_urls()[:20]


def extract_movie_details(movie_url):
	index = 0
	index+=1
	i = movie_url
	html = urlopen(i)
	Obj_soup = BeautifulSoup(html,"lxml")
	dic_to_store_moviedeta = {"Name of movie":"","Director":"","Bio of the Movie":"","Runtime":"","URL of Poster":"","genre":"","Country":"","Language":""}
	genrelist=[]
	listdir = []
	moviedetail = []
	name = Obj_soup.find("div",class_="title_wrapper")
	Name = name.find("h1").get_text()
	Namemovie = Name.split()

	dic_to_store_moviedeta["Name of movie"] = "".join(Namemovie[:-1])
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

list1 = []
def get_movie_list_details(movies):
	for i in movies:
		list1.append(extract_movie_details(i))
	return(list1)
get_movie_list_details(url_list)
analyse = get_movie_list_details(url_list)

def analyse_movies_language(movies):
	lang_list = []
	languages = []
	landetail = {}
	for i in movies:
		for i in(i["Language"]):
			lang_list.append(i)
			if i not in languages:
				languages.append(i)

	for index in languages:
		count = 0
		landetail[index]=0
		for check in lang_list:
			if index == check:
				count+=1
				landetail[index]=count
	print(landetail)
analyse_movies_language(analyse)

def analyse_movies_directors(movies):
	Dirlist = []
	Directors = []
	Dirdetail = {}
	for i in movies:
		for k in (i["Director"]):
			Dirlist.append(k)
			if k not in Directors:
				Directors.append(k)

	for index in Directors:
		count=0
		Dirdetail[index]=0
		for check in Dirlist:
			if index == check:
				count+=1
				Dirdetail[index] = count
	print(Dirdetail)
analyse_movies_directors(analyse)

