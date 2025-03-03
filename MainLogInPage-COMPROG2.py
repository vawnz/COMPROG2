print("Basic Log-In System \n 1. Create an Account \n 2. Already have an Account")
choice = int(input("Choice: "))

if choice == 1:
    from signup import signup  
    signup()

elif choice == 2:
    from login import login 
    login()
else:
    print("Invalid choice. Try again later.")