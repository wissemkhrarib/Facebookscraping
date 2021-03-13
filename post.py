import re

from customparser import CustomParser
from getsoup import get_soup
import datetime


class Post:
    def __init__(self, post_html):
        self.text = ""
        self.nbr_likes = 0
        self.nbr_shares = 0
        self.post_date = None
        self.images_urls = []
        self.other_urls = []
        self.scraping_date = datetime.datetime.now()
        self.soup = get_soup(str(post_html))
        self.parser = CustomParser()

    def get_date(self):
        post_date = self.soup.find('abbr').text
        return self.parser.parse_date(post_date)

    # no likes -->  fixed
    def get_nbr_likes(self):
        nbr_likes = self.soup.find("div", class_="_1g06")
        if nbr_likes != None:
            return self.parser.int_parser(nbr_likes.text)
        return 0

    # no shares #no comments --> fixed
    def get_nbr_shares(self):
        spans = self.soup.find_all("span", class_="_1j-c")
        if spans != None:
            for span in spans:
                if 'Share' in span.text:
                    return self.parser.int_parser(span.text)
        return 0

    # bug --> no text --> fixed
    def get_post_text(self):
        p_elts = self.soup.find('article').find_all("p")
        post_text = ""
        if p_elts != None:
            for elt in p_elts:
                post_text += "\n" + elt.text
        post_text = post_text.replace('…', '').replace('More', '')
        return post_text

    def get_images_urls(self):
        pass

    def get_other_urls(self):
        pass

    def get_post_data(self):
        self.post_date = self.get_date()
        self.nbr_likes = self.get_nbr_likes()
        self.nbr_shares = self.get_nbr_shares()
        self.text = self.get_post_text()

    def __str__(self):
        return "Date: " + str(self.post_date) + " Likes: " + str(self.nbr_likes) + " share: " + str(
            self.nbr_shares) + " scraping date: " + str(self.scraping_date) + " text: " + self.text
