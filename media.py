# Class atributes - title, trailer, reviews, story line, poster image

#IMPORTS
import webbrowser



class Movie(object):
	"""This class Movie is a way to store movie info in one place."""# call this with media.Movie.__doc__
#Class Variables - 


		#1. Purpose - Initializes an object of the Movie class
		#2. Inputs - all of the listed atributes of a movie
		#3. Outputs - no active outputs, creating the object for later use is the goal.
	def __init__(self, movie_title, year, poster_image, trailer_youtube, release_date, rotten_tomato_score, gross_revenue, budget):
		#super(Movie, self).__init__()
		#self.arg = arg
		self.title = movie_title
		self.year = year
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = release_date
		self.rotten_tomato_score = rotten_tomato_score
		self.gross_revenue = gross_revenue
		self.budget = budget
		self.gross_profit = gross_revenue - budget
		self.roi = self.gross_profit *100 / budget


		#1. Purpose - Opens a new window, specifically to show the youtube trailer
		#2. Inputs - The object which includes the link to the trailer on youtube
		#3. Outputs - An open browser window the objects youtube trailer playing
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

'''
Defenitions
Class
Instances - instances of a class, when called it calles the..
Constructor  - __int__. the callss the class to creat and instance called..
self - 
Instance variables - self.variable
Instance methods - functions within the class'''