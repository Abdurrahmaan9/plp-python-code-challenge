# importing all the necesary modules
import random
import string

print('---Welcome to my password generator---')
# the function that will do all the proccesses
def generate_password():
    password = string.ascii_letters + string.digits + string.punctuation
    len = int(input("Enter the length of the password: "))
    # making sure users selects a password long than 8 char
    if len < 8:
        len = 8
        print('your password must be atleast 8 charecters')
        return generate_password()
    # making sure users selects a password less than 90 char
    elif len > 90:
        print("Password length must be less than 90 characters.")
        return generate_password()
    else:
        # joining the password and the length  so they much
        generate_password = ''.join(random.choice(password) for i in range(len))
        print('the password: ',generate_password)
generate_password()

