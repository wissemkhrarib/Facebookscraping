from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from getsoup import get_soup
from post import Post
from time import sleep
from selenium import webdriver


class FacebookScraper:

    def __init__(self, username, password, pages):
        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        options.add_argument('--disable-notifications')  # disable notifications
        self.driver = webdriver.Chrome(options=options)
        self.username = username
        self.password = password
        self.pages = pages

    def login(self):
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

    def scroll(self, scroll_size):
        for i in range(1, scroll_size):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_posts(self, page):
        ancient_posts = []
        self.driver.get(page)
        sleep(1)
        # i --> nbr of posts wanted to be loaded
        i = 200
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
                print("**  **  new post **  **")
                print(post)
            ancient_posts = list(new_posts)
            i -= len(ancient_posts)
            print("_______  " + str(i) + "  -------------")

    def start_scraping(self):
        self.login()
        for page in self.pages:
            self.get_posts(page)
