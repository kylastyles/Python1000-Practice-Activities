#!usr/bin/env python3

# Problem Domain: Integral Conversion
# Mission Summary: Convert String / Integral Formats

user_string = input("Please enter a string to encode in hexadecimal notation: ")


def hex_writer(user_string):
    hex_string = ""

    if user_string == "":
        return None

    for char in user_string:
        hex_num = hex(ord(char))
        hex_string += hex_num

    return hex_string


def hex_reader(encoded_string):

    if encoded_string:
        hex_list = encoded_string.split("0x")
        char_list = [chr(int(i, 16)) for i in hex_list if i != '']
        glue = ""
        decoded_string = glue.join(char_list) 
        return decoded_string
    
    return None


def main(user_string):

    encoded_string = hex_writer(user_string)
    print("\nYour hex-encoded string is:")
    print(encoded_string)

    decoded_string = hex_reader(encoded_string)
    print("\nYour decoded string is:")
    print(decoded_string)


main(user_string)