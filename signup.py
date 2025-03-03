def signup():
    print("\nSign-Up Page")
    newUser = input("Please enter your Username: ")
    newPass = input("Please enter your Password: ")
    checkPass = input("Enter again your Password: ")

    if newPass != checkPass:
        print("Passwords do not match. Try again.")
        signup()
    else:
        choice = input("\nAccount created successfully! Proceed to Log-In? (y/n): ")
        if choice == 'y':
            print("\nWelcome back! Please enter your Account")
            tries = 5
            loggedIn = False
            while tries > 0:
                username = input("Please enter your Username: ")
                password = input("Please enter your Password: ")
                if username == newUser and password == newPass:
                    print(f"\nHello again, {username}! You are now Logged In.")
                    loggedIn = True
                    break
                else:
                    tries -= 1
                    print(f"Invalid credentials. {tries} attempt/s left.\n")
            if not loggedIn:
                print("\nYou ran out of attempts. Try again later.")
        elif choice == 'n':
            print("See you around!")
        else:
            print("Invalid choice. Try again later.")
