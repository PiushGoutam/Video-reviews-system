from app import MakeMovie
from scraper import ScrapeReviews
import os

movie_name = input('Enter the movie name you want reviews for:')
print(" Launching scraper for {}".format(movie_name))
Reviews = ScrapeReviews("https://www.imdb.com/find?q={}".format(movie_name.replace(' ','+')))
print("The url is {}".format(Reviews.response))
print("Begin downloading Images..")
Reviews.navigate_to_reviews()       
print("Begin making video...")
Movie = MakeMovie(movie_name)
Movie.pre_cast_text()
Movie.review_screenshots()
Movie.post_cast_text()
Movie.finalize(movie_name)

print('Deleting all downloaded images..')

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.png'):
        os.remove(filename)
