import psycopg
#Login file for Monty Hall

def login():
    with psycopg.connect(conninfo="postgresql://postgres:angjaya08102005@127.0.0.1:5432/montyhall") as connection:
        with connection.cursor() as cursors:
            #Login menu
            print("Welcome to the Monty Hall Game")
            print("Before we start, please sign in or sign up or you can playing as guest")
            while True:
                ask_user = input("1. Sign In\n2. Sign Up\n3. Guest\nAnswer with number: ")
                if int(ask_user) == 1 or ask_user.lower == "sign in":
                    #Ask for username, password and do checks etc
                    ask_username = input("Input username : ")
                    try:
                        cursors.execute("SELECT username FROM montyhall where username LIKE '%s';"%(ask_username))
                    except:
                        print("Username is wrong! Try again")
                        continue
                    ask_password = input("Input password : ")
                    try:
                        cursors.execute("SELECT password FROM montyhall WHERE password LIKE '%s';"%(ask_password))
                    except:
                        print("Password is wrong! Try again")
                        continue
                    cursors.execute("SELECT * FROM montyhall;")
                    user_confirmed = cursors.fetchone()
                    return user_confirmed[1], user_confirmed[3], user_confirmed[4]
                if int(ask_user) == 2 or ask_user.lower == "sign up":
                    #Input new username, new password, reinput new password and insert to db
                    while True:
                        new_user = input("Input your new account username : ")
                        new_pass = input("Input your new account password : ")
                        new_confirm_pass = input("Please re-input your new password to make sure : ")
                        if new_confirm_pass != new_pass:
                            continue
                        confirm_all = input("Your username : %s\nYour password : %s\nIs this correct? (Yes / No) : "%(new_user, new_pass))
                        if confirm_all.lower() == "yes" or confirm_all.lower() == "y":
                            cursors.execute("INSERT INTO montyhall(username, password) values('%s', '%s')"%(new_user, new_pass))
                            cursors.execute("SELECT user_attempt, user_won FROM montyhall WHERE username LIKE '%s';"%(new_user))
                            take_info_new_user = cursors.fetchone()
                            return new_user, take_info_new_user[0], take_info_new_user[1]
                        else:
                            continue
                if int(ask_user) == 3 or ask_user.lower == "guest":
                    guest_name = input("Input your guest name : ")
                    user_attempt = 0
                    user_won = 0
                    return guest_name, user_attempt, user_won 