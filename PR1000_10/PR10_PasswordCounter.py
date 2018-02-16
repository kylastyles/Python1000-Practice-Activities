""" 
File: PR10_PasswordCounter.py
Requirements: PT10_PasswordCounter.pdf
"""

# TODO: Your solution goes here!

#!usr/bin/env python3

# Problem Domain: Login
# Mission Summary: Create a "Login Loop"


def Login(num): 

    # Hard-coded encapsulated user data
    user_id = "SuperGirl"
    password = "superfly"

    attempts = 0
    max_attempts = num

    # USER_LOOP
    while True:
        user_input1 = input("Please enter your name: ")
        print("Hello, " + user_input1)

        user_input2 = input("Please enter your password: ")

        # PASSWORD_LOOP
        while user_input1 == user_id:
            if user_input2 != password:
                attempts += 1

                if attempts == max_attempts:
                    print("Too Many Unsuccessful Attempts")
                    print("Program Termination")
                    exit()
                else:
                    print("Incorrect password. Strike " + str(attempts))
                    user_input2 = input("Please enter your password: ")
                    continue
            else:
                print("Login Success")
                print("Welcome, " + user_input1)
                return user_input1
        
        print("Incorrect username: " + user_input1)
        continue
        
Login(3)


