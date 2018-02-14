#!usr/bin/env python3

# Problem Domain: String & Number Practice
# Mission Summary: Convert String / Integral Formats

user_str = input("Please enter text to convert to hexadecimal notation: ")

def dump_hex(user_str):
    hex_table = ""
    counter = 0

    for char in user_str:
        num = hex(ord(char))

        if counter % 8 != 0:
            hex_table += str(num) + "\t"
        else:
            hex_table += "\n" + str(num) + "\t"
        
        counter += 1

    return hex_table

print(dump_hex(user_str))