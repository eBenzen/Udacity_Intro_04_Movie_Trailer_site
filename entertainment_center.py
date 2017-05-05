import media
import fresh_tomatoes

#Create a list for each variable in the class
#Source - https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films
#movie_title, poster_image, trailer_youtube, rotten_tomato_score, gross_revenue, budget

titles = ["Iron Man", "The Incredible Hulk", "Iron Man 2", "Thor", "Captain America: The First Avenger", "Marvel's The Avengers", "Iron Man 3", "Thor: The Dark World", "Captain America: The Winter Soldier", "Guardians of the Galaxy", "Avengers: Age of Ultron", "Ant-Man", "Captain America: Civil War", "Doctor Strange"]

year = [2008,2008,2010,2011,2011,2012,2013,2013,2014,2014,2015,2015,2016,2016]

#source - http://marvelcinematicuniverse.wikia.com/
poster_link = ["https://vignette1.wikia.nocookie.net/marvelcinematicuniverse/images/1/1e/Iron_Man_Official_Poster.jpg/revision/latest?cb=20120115035645", "https://vignette3.wikia.nocookie.net/marvelcinematicuniverse/images/1/1b/The_Incredible_Hulk.jpg/revision/latest?cb=20121221015327", "https://vignette4.wikia.nocookie.net/marvelcinematicuniverse/images/c/cb/Iron_Man_2_Official_Poster.jpg/revision/latest?cb=20120702233904", "https://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/5/5a/Thor_Official_Poster.jpg/revision/latest?cb=20121220212004", "https://vignette1.wikia.nocookie.net/marvelcinematicuniverse/images/8/81/CaptainAmericaTheFirstAvengerComicConPoster.jpg/revision/latest?cb=20120122235032", "https://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/d/d0/Theavengersnewposter.jpg/revision/latest?cb=20140224212619", "https://vignette4.wikia.nocookie.net/marvelcinematicuniverse/images/5/55/Iron_Man_3_IMAX_poster.jpg/revision/latest?cb=20130319165854", "https://vignette1.wikia.nocookie.net/marvelcinematicuniverse/images/f/fc/Thor-_The_Dark_World_poster.jpg/revision/latest?cb=20131115001851", "https://vignette3.wikia.nocookie.net/marvelcinematicuniverse/images/c/c0/Captain_America_The_Winter_Soldier_main_poster.jpg/revision/latest?cb=20160617182910", "https://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/f/f8/GuardiansoftheGalaxyTheatricalPoster.jpg/revision/latest?cb=20140516163015", "https://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/c/c7/Avengers_Age_Of_Ultron-poster1.jpg/revision/latest?cb=20150224202250", "https://vignette3.wikia.nocookie.net/marvelcinematicuniverse/images/b/bb/Ant-Man_Poster.png/revision/latest?cb=20150506130539", "https://vignette1.wikia.nocookie.net/marvelcinematicuniverse/images/5/5c/Civil_War_Final_Poster.jpg/revision/latest?cb=20160310172110", "https://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/8/8b/DrStrangePoster2.jpg/revision/latest?cb=20160724020506" ]

trailer_link = ["https://www.youtube.com/watch?v=8OCJRbzdzaU", "https://www.youtube.com/watch?v=5OPDu0hp7A8", "https://www.youtube.com/watch?v=LXBbCeKNn9Y", "https://www.youtube.com/watch?v=1dYBtiqet1k", "https://www.youtube.com/watch?v=R9xgkBlrEn0", "https://www.youtube.com/watch?v=W9ZnpIGvZUo", "https://www.youtube.com/watch?v=IA7b28MBBXo", "https://www.youtube.com/watch?v=5V8qm-V7JuY", "https://www.youtube.com/watch?v=FNv6pxZyRL4", "https://www.youtube.com/watch?v=maIEaTm5gBE", "https://www.youtube.com/watch?v=M2ciY79mlQw", "https://www.youtube.com/watch?v=IkrfpsjTJzo", "https://www.youtube.com/watch?v=efBgXjbd2uQ", "https://www.youtube.com/watch?v=Bme-XHo-AA4"]

release_date = ["May 2, 2008", "June 13, 2008", "May 7, 2010", "May 6, 2011", "July 22, 2011", "May 4, 2012", "May 3, 2013", "November 8, 2013", "April 4, 2014", "August 1, 2014", "May 1, 2015", "July 17, 2015", "May 6, 2016", "November 4, 2016"]

fresh_score = [94,67,72,77,80,92,79,66,89,91,75,81,90,90,86]

gross_revenue = [590, 270, 630, 450, 380, 1520, 1220, 650, 720, 780, 1410, 520, 1160, 680]

budget = [140, 150, 200, 150, 140, 220, 200, 170, 170, 232, 316, 130, 250, 165]

#Use a loop to create a class for each movie.  To add a movie, simple add one element to each list, loop runs based on the lengths
movies = []
index = 0

while index < len(titles):
	movies.append(media.Movie(titles[index],year[index],poster_link[index], trailer_link[index], release_date[index],fresh_score[index], gross_revenue[index],budget[index]))
	index += 1

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)


