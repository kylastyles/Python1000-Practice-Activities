""" 
File: PR11_PasswordEncoder.py
Requirements: PT11_PasswordEncoder.pdf
"""

# TODO: Your solution goes here!

#!usr/bin/env python3

# Problem Domain: Login / Security / Encryption
# Mission Summary: Create a "Password Encoder"


# HELPER FUNCTIONS

def make_string_of_ords(myString):
    ord_str = ""
    for char in myString:
        x = ord(char)
        ord_str += str(x)
    return ord_str


def encrypt(user_id, password):
    # Determine integral value of characters in strings
    ord_combo = ""

    id_index = 0
    pw_index = 0

    while pw_index < len(password):

        x = ord(user_id[id_index])
        y = ord(password[pw_index])
        ord_combo += str(x+y)

        id_index += 1
        if id_index == len(user_id):
            id_index = 0
        
        pw_index += 1
    
    return hex(int(ord_combo))



def decrypt(hex_pw, user_id):
    ord_id = make_string_of_ords(user_id)
    ord_pw = str(int(hex_pw, 16))
    password = ""

    for i in range(0, len(ord_pw), 3):
        x = chr(int(ord_pw[i:i+3]) - int(ord_id[i:i+3]))
        password += x 

    return password



# TEST CASES
user_id = "dog"
password = "cat"

test1 = encrypt(user_id, password)
#print(test1)
#print(int(test1, 16))
print(decrypt(test1, user_id))

# print(ord("a")) #97
# a = 9
# b = 7
# print(chr(int(str(a) + str(b))))



