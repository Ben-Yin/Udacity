from fresh_tomatoes import open_movies_page
from media import *

# some instances of movie class
movie_star_war = Movie(
	"Rogue One: A Star Wars Story", 
	"https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
	"https://www.youtube.com/watch?v=frdj1zb9sMY",
	"The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.")

movie_fantastic_beasts = Movie(
	"Fantastic Beasts and Where to Find Them",
	"https://upload.wikimedia.org/wikipedia/zh/9/94/Fantastic_Beasts_and_Where_to_Find_Them_Poster.jpg",
	"https://www.youtube.com/watch?v=Vso5o11LuGU",
	"The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.")

movie_moana = Movie(
	"Moana", 
	"https://upload.wikimedia.org/wikipedia/zh/d/d5/Moana-poster1.jpg",
	"https://www.youtube.com/watch?v=LKFuXETZUsI",
	"In Ancient Polynesia, when a terrible curse incurred by Maui reaches an impetuous Chieftain's daughter's island, she answers the Ocean's call to seek out the demigod to set things right.")


# a list of movies
movies = [
	movie_star_war,
	movie_fantastic_beasts,
	movie_moana,
]

# Uses list of movie instances as input to generate an HTML file
# and open it in the browser.
open_movies_page(movies)