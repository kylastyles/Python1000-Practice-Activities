#!usr/bin/env python3

from PR20_DataArray import load_data
import random

def parse_data(data):
    quote = random.choice(list(data))
    quote_list = quote.split("|")
    quote_dict = {"Quote Key" : quote_list[1], "Author Key" : quote_list[0]}
    
    return quote_dict

def show_stars(num):
    return num * "*"

def make_spaces(num):
    return num * " "

def present_quote(quote_dict):
    text_box = "\n" + show_stars(40) + "\n* "
    word_list = quote_dict["Quote Key"].split(" ")
    word_count = 0
    while word_count < len(word_list):
        char_count = 2
        for word in word_list:
            if char_count + (len(word) + 2) < 40:
                text_box += word + " "
                char_count += (len(word) + 1)
            else:
                text_box += make_spaces(39 - char_count) + "*\n* " + word + " "
                char_count = 3 + len(word)
            word_count += 1
        text_box += make_spaces(39 - char_count) + "*"
    text_box += "\n* --- " + quote_dict["Author Key"] + make_spaces(39 - (len(quote_dict["Author Key"]) + 6)) + "*\n" + show_stars(40) + "\n"
    return text_box

def run_program():
    print(present_quote(parse_data(load_data())))

run_program()