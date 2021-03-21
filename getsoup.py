from bs4 import BeautifulSoup
from selenium import webdriver


def get_soup(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup


driver = None


def get_singelton_webdriver():
    global driver
    if driver == None:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')  # disable notifications
        driver = webdriver.Chrome(options=options)
    return driver
