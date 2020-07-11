import requests
from bs4 import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

class ScrapeReviews:
    """ A wrapper class to do web scraper movie reviews from IMDB """
    def __init__(self,url):
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        self.url = url
        self.driver = webdriver.Chrome(os.getcwd()+'//chromedriver.exe',options=chrome_options)
        self.reviews_url = ''

    def get_to_the_main_page(self,soup):
        return soup.find('td',{'class':'result_text'}).find('a').get('href')

    @property
    def response(self):
        resp = requests.get(self.url)
        if resp.status_code == 200:
            main_url = "https://www.imdb.com/{}reviews".format(self.get_to_the_main_page(BeautifulSoup(resp.text,'lxml')))
            self.reviews_url = main_url
            return resp
        else:
            print("Sorry Invalid response") 
            return resp    

    def navigate_to_reviews(self):
        ctr = 0
        print(self.reviews_url)
        self.driver.get(self.reviews_url)
        self.driver.implicitly_wait(10)
        reviews = self.driver.find_elements_by_class_name("review-container")
        for review in reviews:
            review.screenshot('new_{}.png'.format(ctr))
            print("Saving new_{}.png".format(ctr))
            ctr+=1
        print(f"Downloaded {ctr} images of reviews..")


        
