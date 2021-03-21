from getsoup import get_soup, get_singelton_webdriver
from post import Post
from time import sleep
from selenium import webdriver

from Facebookscraping.db import MongoDB


class FacebookScraper:

    def __init__(self, username, password, pages, db_name, col_name, cookies=None):
        self.driver = get_singelton_webdriver()
        self.username = username
        self.password = password
        self.cookies = cookies
        self.pages = pages
        self.db_object = MongoDB(db_name, col_name)

    def login(self):
        if self.cookies is not None:
            return
        self.driver.get("https://www.facebook.com/login")
        sleep(2)
        email_in = self.driver.find_element_by_id("email")
        email_in.send_keys(self.username)
        sleep(1)
        password_in = self.driver.find_element_by_name("pass")
        password_in.send_keys(self.password)
        login_btn = self.driver.find_element_by_id('loginbutton')
        login_btn.click()
        sleep(2)

    def login_with_cookies(self):
        if self.cookies is None:
            return
        for c in self.cookies:
            self.driver.add_cookie(c)
        return self.driver.refresh()
        sleep(2)

    def scroll(self, scroll_size):
        for i in range(1, scroll_size):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_posts_text_and_save(self, posts):
        posts_objects_dict = []
        for post in posts:
            post.get_post_text()
            posts_objects_dict.append(post.__dict__())
            print(post.__dict__())
            sleep(3)
        self.db_object.insert_data_list(posts_objects_dict)

    def get_posts(self, page):
        ancient_posts = []
        posts_objects = []
        self.driver.get(page)
        self.login_with_cookies()
        sleep(1)
        # i --> nbr of posts wanted to be loaded
        i = 50
        while i > 0:
            # j --> used to scroll multiple times to load more posts
            j = 4
            while j > 0:
                self.scroll(2)
                sleep(2)
                j -= 1
            page_content = self.driver.page_source
            soup = get_soup(page_content)
            posts = soup.find_all("article")
            # to get only the new loaded posts
            new_posts = list(set(posts) - set(ancient_posts))
            for post_html in new_posts:
                post = Post(post_html)
                post.get_post_data()
                posts_objects.append(post)
                # print("**  **  new post **  **")
                # print(post)
            ancient_posts += list(new_posts)
            i -= len(new_posts)
        self.get_posts_text_and_save(posts_objects)


    def start_scraping(self):
        self.login()
        for page in self.pages:
            self.get_posts(page)
