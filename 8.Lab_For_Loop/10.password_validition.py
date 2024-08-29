# 10. Python program to check the validity of password input by users:

def password_validation(password):
    if len(password) < 8:                                            # Check if the password has at least 8 characters
        return "Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):                 # Check if the password contains at least one uppercase letter
        return "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):                 # Check if the password contains at least one lowercase letter
        return "Password must contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):                 # Check if the password contains at least one number
        return "Password must contain at least one number."
    
    special_characters = "@#$%^&*"                                   # Check if the password contains at least one special character
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character (@, #, $, %, ^, &, *)."
    
    return "Password is valid."                                      # if all the previous statements correct 

password = input("Enter a password: ")   #taking password from the user
print(password_validation(password))     # Checking and printing the result