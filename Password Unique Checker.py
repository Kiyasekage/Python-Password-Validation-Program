print("Welcome to checking your password!")
print("Criteria :  \n1. >8 characters\n2. Must contain lowercase, uppercase, and digits\n3. password must not be the same with username ")
name = input("Username: ")
attempts = 3
for i in range(attempts):
    password = input("Password: ")
    has_lower = False
    has_upper = False
    has_number = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_number = True
    if(len(password)>8 and has_lower and has_upper and has_number and password != name):
        print(f"Hi {name}, your password has been confirmed")
        break
    else:
        remaining = attempts -i- 1
        print(f"Dear {name}, your password does not meet our criteria")
        if remaining>0:
            print(f"You have {remaining} attempt(s)")
        else:
            print("You have failed to create a valid password")
        