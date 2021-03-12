to start the scraping:
1- enter the e-mail, password and the pages links in secrets.py
2- run the startscraping.py file

the output will be shown in the console.
the code performs the following things:
    1- get the number of likes
    2- get the number of shares
    3- get the posting date and change it from a string to datetime object
    4- get the post text but it doesn't work perfectly because clicking the more link is no fixed
    and it takes the original text and its corresponding translation.
the pages links should be in this form: "https://m.facebook.com/PAGE_NAME/"


