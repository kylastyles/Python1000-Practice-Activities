""" 
File: PR11_PasswordEncoder.py
Requirements: PT11_PasswordEncoder.pdf
"""

# TODO: Your solution goes here!

#!usr/bin/env python3

# Problem Domain: Login / Security / Encryption
# Mission Summary: Create a "Password Encoder"


# HELPER FUNCTION

def make_string_of_ords(myString):
    ord_str = ""
    for char in myString:
        x = ord(char)
        ord_str += str(x) + ";"
    return ord_str


# STEP 1: ENCRYPT PASSWORD

def encrypt(user_id, password):
    """
    Determine integral value of characters in strings, add them together (wrapping user_id if needed),
    and return as a hex representation.
    """
    if user_id == "" or password == "":
        return None
        
    encrypted_str = ""
    id_index = 0
    for c in password:
        if id_index >= len(user_id):
            id_index = 0
        combined_char = hex(ord(c) + ord(user_id[id_index]))
        encrypted_str += combined_char + ";"
        id_index += 1
    
    return encrypted_str


# STEP 2: DECRYPT PASSWORD

def decrypt(hex_pw, user_id):
    """
    Translate from hex back to ordinal value of characters, subtract user_id (wrapped if necessary) values from sum,
    return original password.
    """
    
    # Prepare user_id to work as key:
    ord_id = make_string_of_ords(user_id)
    # Turn user_id and password strings into lists, deleting the erroneous ' ' at the end.
    id_list = ord_id.split(";")
    del id_list[-1]
    pw_list = hex_pw.split(";")
    del pw_list[-1]

    password = ""

    # Iterate through password list, wrapping and subtracting user_id char
    id_index = 0
    for i in pw_list:
        if id_index >= len(id_list):
            id_index = 0
        char = int(i, 16) - int(id_list[id_index])
        password += chr(char)
        id_index += 1 

    return password


# TEST CASES
user_id = "doggy"
password = "kittycat"

test1 = encrypt(user_id, password)
print(test1)
print(decrypt(test1, user_id))






