def signup():
    print("\nSign-Up Page")
    newUser = input("Please enter your Username: ")
    newPass = input("Please enter your Password: ")
    checkPass = input("Enter again your Password: ")

    if newPass != checkPass:
        print("Passwords does not match. Try again.")
        signup()
    else:
        choice = input("Account created successfully! Proceed to Log-In? (y/n): ")
        if choice == 'y':
            print("\nWelcome back! Please enter your Account")
            username = input("Please enter your Username: ")
            password = input("Please enter your Password: ")
            
            tries = 5
            while tries > 0:
                if username != newUser and password != newPass:
                    tries -= 1
                print(f"Invalid credentials. Please Try Again. {tries} attempt/s left.")
            else:
                print(f"Hello again, {username}! You are now Logged In.")
                if tries == 0:
                    print("You ran out of attempts. Try again later.")
        elif choice == 'n':
            print("See you around!")
        else:
            print("Invalid choice. Try again later.")
