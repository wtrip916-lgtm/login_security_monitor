import time
credentials = {
    "saksham": 976873,
    "gpt": 672345,
    "john": 138751
}
remaining_attempts = {
    "saksham": 4,
    "gpt": 4,
    "john": 4
}
blocked_users = []
print(" #       #######  #####  ### #     #     #####  #######  #####  #     # ######  ### ####### #     #    #     # ####### #     # ### ####### ####### ######  ")
print(" #       #     # #     #  #  ##    #    #     # #       #     # #     # #     #  #     #     #   #     ##   ## #     # ##    #  #     #    #       #     # ")
print(" #       #     # #        #  # #   #    #       #       #       #     # #     #  #     #      # #      # # # # #     # # #   #  #     #    #       #     # ")
print(" #       #     # #  ####  #  #  #  #     #####  #####   #       #     # ######   #     #       #       #  #  # #     # #  #  #  #     #    #####   ######  ")
print(" #       #     # #     #  #  #   # #          # #       #       #     # #   #    #     #       #       #     # #     # #   # #  #     #    #       #   #   ")
print(" #       #     # #     #  #  #    ##    #     # #       #     # #     # #    #   #     #       #       #     # #     # #    ##  #     #    #       #    #  ")
print(" ####### #######  #####  ### #     #     #####  #######  #####   #####  #     # ###    #       #       #     # ####### #     # ###    #    ####### #     # ")
while True:
    ask = input("select (login / remaining / exit): ").lower().strip()
    if ask == "login":
        username = input("enter your username: ").strip().lower()
        if username in blocked_users:
            print("You are blocked because of anonymous activity from your account")
            continue
        while True:
            try:
                password = int(input("enter your password: "))
                break
            except ValueError:
                print("Invalid input! Please enter your password using digits only.")
        if username in credentials and credentials[username] == password:
            print("Login successfull you can access your account")
        else:
            print("Enter a valid username and password")
            if username in credentials:
                remaining_attempts[username] -= 1
                if remaining_attempts[username] == 2:
                    print("WARNING! two attempts left!")
                if remaining_attempts[username] == 1:
                    print("🚨ANONYMOUS ACTIVITY DETECTED! pleasw wait for 10 seconds to proceed")
                    time.sleep(10)
                if remaining_attempts[username] == 0:
                    print("Because of many attempts we have to block your account")
                    blocked_users.append(username)
        print("remain attempts: " , remaining_attempts[username])
    elif ask == "remaining":
        take = input("enter username: ")
        if take in remaining_attempts:
            print(remaining_attempts[take])
        else:
            print("Invailid username entered")
    elif ask == "exit":
        print("Thanks for using! bye")
        break
    else:
        print("Invaild option is select. Entera vaild option")