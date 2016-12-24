# class name: 
# 	Movie
# attribute:
# 	title
# 	poster_image_url
# 	trailer_youtube_url
# 	storyline
class Movie:
	"""
	The Movie class store movie related information
	"""
	def __init__(self, title, poster_image_url, trailer_youtube_url, storyline):
		"""
		the input arguments of init is the title of movie, 
		URL of poster image and URl of trailer video on youtube
		"""
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.storyline = storyline

	# getter and setter
	def get_title(self):
		return self.title

	def get_poster_image_url(self):
		return self.poster_image_url

	def get_trailer_youtube_url(self):
		return self.trailer_youtube_url

	def get_storyline(self):
		return self.storyline

	def set_title(self, title):
		self.title = title
	
	def set_poster_image_url(self, poster_image_url):
		self.poster_image_url = poster_image_url

	def set_trailer_youtube_url(self, trailer_youtube_url):
		self.trailer_youtube_url = trailer_youtube_url

	def set_storyline(self, storyline):
		self.storyline = storyline