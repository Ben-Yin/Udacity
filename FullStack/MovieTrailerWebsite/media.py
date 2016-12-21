# class name: 
# 	Movie
# attribute:
# 	title
# 	poster_image_url
# 	trailer_youtube_url

class Movie:
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def get_title(self):
		return self.title

	def get_poster_image_url(self):
		return self.poster_image_url

	def get_trailer_youtube_url(self):
		return self.trailer_youtube_url

	def set_title(self, title):
		self.title = title
	
	def set_poster_image_url(self, poster_image_url):
		self.poster_image_url = poster_image_url

	def set_trailer_youtube_url(self, trailer_youtube_url):
		self.trailer_youtube_url = trailer_youtube_url
