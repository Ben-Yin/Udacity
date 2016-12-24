from fresh_tomatoes import open_movies_page
from media import *

# some instances of movie class
movie_star_war = Movie(
	"Rogue One: A Star Wars Story", 
	"https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
	"https://www.youtube.com/watch?v=frdj1zb9sMY")

movie_your_name = Movie(
	"Your Name", 
	"https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
	"https://www.youtube.com/watch?v=s0wTdCQoc2k")

movie_fantastic_beasts = Movie(
	"Fantastic Beasts and Where to Find Them",
	"https://upload.wikimedia.org/wikipedia/zh/9/94/Fantastic_Beasts_and_Where_to_Find_Them_Poster.jpg",
	"https://www.youtube.com/watch?v=Vso5o11LuGU")

movie_moana = Movie(
	"Moana", 
	"https://upload.wikimedia.org/wikipedia/zh/d/d5/Moana-poster1.jpg",
	"https://www.youtube.com/watch?v=LKFuXETZUsI")

# a list of movies
movies = [
	movie_star_war,
	# movie_your_name,
	movie_fantastic_beasts,
	movie_moana,
]

# Uses list of movie instances as input to generate an HTML file
# and open it in the browser.
open_movies_page(movies)