import json
from customparser import CustomParser
from getsoup import get_soup, get_singelton_webdriver
import datetime


class Post(object):
    def __init__(self, post_html):
        self.post_url = ""
        self.nbr_likes = 0
        self.nbr_shares = 0
        self.nbr_comments = 0
        self.text = ""
        self.post_date = None
        self.images_urls = []
        self.video_url = ""
        self.source_name = ""
        self.is_shared = False
        self.scraping_date = datetime.datetime.now()
        self.soup = get_soup(str(post_html))
        self.parser = CustomParser()
        self.driver = get_singelton_webdriver()

    def get_post_url(self):
        a_tag = self.soup.find("abbr").find_parent("a")
        link = a_tag.attrs["href"]
        return "https://m.facebook.com" + link

    def get_post_source_name(self):
        a = self.soup.find('a')
        return a.i.attrs["aria-label"].replace(', profile picture', '')

    def get_date(self):
        post_date = self.soup.find('abbr').text
        return self.parser.parse_date(post_date)

    def is_the_post_shared(self):
        post_dates = self.soup.find_all('abbr')
        return len(post_dates) == 2

    # no likes -->  fixed
    def get_nbr_likes(self):
        nbr_likes = self.soup.find("div", class_="_1g06")
        if nbr_likes != None:
            return self.parser.int_parser(nbr_likes.text)
        return 0

    # no shares #no comments --> fixed
    def get_nbr_shares(self):
        data = {'shares': 0, 'comments': 0}
        spans = self.soup.find_all("span", class_="_1j-c")
        if spans != None:
            for span in spans:
                if 'Share' in span.text:
                    data['shares'] = self.parser.int_parser(span.text)
                elif 'Comment' in span.text:
                    data['comments'] = self.parser.int_parser(span.text)

        return data

    # bug --> no text --> fixed
    def get_post_text(self):
        post_text = ""
        self.driver.get(self.post_url)
        page_content = self.driver.page_source
        soup = get_soup(page_content)
        p_elts = soup.find_all('p')
        if p_elts != None:
            for elt in p_elts:
                post_text += " " + elt.text
        self.text = post_text

    def get_images_urls(self):
        images_urls = []
        image_links_container = self.soup.find("div", class_="_26ii _-_b")
        if image_links_container != None:
            images_links = image_links_container.find_all('a')
            for link in images_links:
                images_urls.append("https://m.facebook.com" + link.attrs["href"])
        return images_urls

    def get_video_url(self):
        video_div = self.soup.find('div', class_="_53mw")
        if video_div != None:
            src = json.loads(video_div.attrs['data-store'])['src']
            return src

    def get_post_data(self):
        self.post_date = self.get_date()
        self.nbr_likes = self.get_nbr_likes()
        self.nbr_comments = self.get_nbr_shares()['comments']
        self.nbr_shares = self.get_nbr_shares()['shares']
        self.post_url = self.get_post_url()
        self.images_urls = self.get_images_urls()
        self.source_name = self.get_post_source_name()
        self.video_url = self.get_video_url()
        self.is_shared = self.is_the_post_shared()

    def __str__(self):
        return "Date: " + str(self.post_date) + " Likes: " + str(self.nbr_likes) + " shares: " + str(
            self.nbr_shares) + " comments: " + str(self.nbr_comments) + " scraping date: " + str(
            self.scraping_date) + " post url : " + self.post_url + "post text:\n" + self.text

    def __dict__(self):
        post_dict = {'post_url': self.post_url, 'nbr_likes': self.nbr_likes, 'nbr_shares': self.nbr_shares, 'nbr_comments': self.nbr_comments, 'is_shared': self.is_shared, 'text': self.text, 'post_date': self.post_date,
                     'images_urls': self.images_urls, 'video_url': self.video_url, 'source_name': self.source_name, 'scraping_date': self.scraping_date}
        return post_dict
