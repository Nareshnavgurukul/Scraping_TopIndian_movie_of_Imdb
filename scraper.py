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
	eachMovie={"Position":"","name":0,"year_of_release":0,"Rating":0}
	index=0
	for tr in trs:
		index+=1	
		name_enter = tr.find("td",class_="titleColumn")
		year_enter = tr.find("td",class_="titleColumn")
		rating_td = tr.find("td",class_="imdbRating")
		rating = tr.find("strong").get_text()
		rating=float(rating)
		name = name_enter.find("a").get_text()
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
		# name = fmm["name"]
		year = fmm["year_of_release"]
		for keyyear in dec_years:
			if keyyear == year:
				dec_years[keyyear].append(fmm)

	moviename = open("Group_by_year.txt","w+")
	dicname={}
	for i in dec_years:
		count = 0
		# print(i,"\n")
		moviename.write(str(i)+"\n")

		for j in dec_years[i]:
			count+=1
			# print(j)
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
	