def login():
    fixUser = "cvsu"
    fixPass = "1234"
    tries = 5
    
    while tries > 0:
        print("\nLog-In Page")
        username = input("Please enter your Username: ")  
        password = input("Please enter your Password: ")     
        
        if username != fixUser or password != fixPass: 
            tries -= 1
            print(f"Invalid credentials. {tries} attempt/s left.")
        else:
            print(f"Hello again, {username}! You are now Logged In.")
            break 
            
    if tries == 0:
        print("You ran out of attempts. Try again later.")