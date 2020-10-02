  
def pwd_check():
    
    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        attempt = attempt +1
        pwd = input("Enter password:")
        return_value = "Password Valid"

        if not 8 < len(pwd) < 20:
            print("Password length should be between 8-20 characters.")
            return_value = "Password Invalid"

        if not any(char.isupper() for char in pwd):
            print("Password must contain atleast 1 uppercase character.")
            return_value = "Password Invalid"

        if not any(char.isdigit() for char in pwd):
            print("Password must contain atleast 1 number.")
            return_value = "Password Invalid"

        if not any(char.islower() for char in pwd):
            print("Password must contain atleast 1 lowerpercase character.")
            return_value = "Password Invalid"

        SpecialCharacter = ['!','@','#','$','%','*','&']
        if not any(char in SpecialCharacter for char in pwd):
            print("Password must contain atleast 1 special character.")
            return_value = "Password Invalid"

        if return_value == "Password Valid":
            print("Password is valid")
            break
        
        if attempt == 3 and return_value == "Password Invalid":
            print("Max attempts reached. Please contact administrator to reset password.")

pwd_check()