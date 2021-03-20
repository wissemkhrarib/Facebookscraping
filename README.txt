to start the scraping:
1- enter the e-mail, password, the pages urls, the db_name, the collection name and the cookies if you want to login with them in secrets.py
2- run the startscraping.py file

The code was executed on linux. To execute it on windows,
replace "self.driver = webdriver.Chrome(options=options)" with
"browser = webdriver.Chrome(executable_path=r"PATH_TO\chromedriver.exe", options=option)"
in the constructor in the facebookscraper.py file.

the output will be shown in the console.

the code performs the following things:
    1- get the number of likes
    2- get the number of shares
    3- get the number of comments
    4- detect the post was shared or not
    5- get the video url if there is a video
    6- get the images urls if there are images (only the first 4 images)
    7- get the name of the page
    8- get the posting date and change it from a string to datetime object
    9- get the post text.
    10- possibility to login using cookies
    11- save the data in a MongoDB collection

the pages urls should be in this form: "https://m.facebook.com/PAGE_NAME/"
it works only for pages, not yet for groups.

For the facebook account:
    1- Disable translation for the most used languages used in posts (Arabic, French, English)
    2- set the language used to English



