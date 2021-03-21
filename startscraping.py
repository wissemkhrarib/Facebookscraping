from facebookscraper import FacebookScraper
from secrets import username, password, cookies, pages, db_name, col_name
sc = FacebookScraper(username, password, pages, db_name, col_name, cookies)
sc.start_scraping()



























# sc.driver.get("https://m.facebook.com/Presidencedugouvernementtunisien/")
# sc.scroll(4)
# sleep(2)
# sc.scroll(4)
# sleep(2)
# sc.scroll(4)
#
# page = sc.driver.page_source
# print(len(sc.get_posts(page)))
# for post in sc.get_posts(page):
#     print("--------------------------------------------" + "nbr_like : "+ sc.get_nbr_likes(post) + " nbr partage : " + sc.get_nbr_shares(post)["shares"])
#     print("--------------posted date : "+sc.date_posted(post))
#     print(sc.get_post_text(post))
#     #print(post)

