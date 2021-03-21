import datetime
import re


class CustomParser:

    # get date from string
    def parse_date(self, date_str):
        word_list = date_str.split(" ")
        if len(word_list) == 6:
            date = datetime.datetime.strptime(date_str, "%B %d, %Y at %I:%M %p")
        elif len(word_list) == 5:
            new_date_str = word_list[0] + " " + word_list[1] + ", 2021 " + word_list[2] + " " + word_list[3] + " " + \
                           word_list[4]
            date = datetime.datetime.strptime(new_date_str, "%B %d, %Y at %I:%M %p")
        else:
            date = datetime.datetime.now()
        return date

    # get int from string
    def int_parser(self, string):
        if 'K' in string:
            try:
                return int(float(re.search(r'\d+.\d+', string).group()) * 1000)
            except:
                return int(float(re.search(r'\d+', string).group().replace(',', '.')) * 1000)
        return int(re.search(r'\d+', string).group())
