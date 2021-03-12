from bs4 import BeautifulSoup


def get_soup(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup
