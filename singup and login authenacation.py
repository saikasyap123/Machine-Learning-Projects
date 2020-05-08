 
my_dict = {}
def signup():
    user = input("enter the username: ")
    pas = input("enter the password: ")
    my_dict[user]=pas
    print("registered succesfully")

def login():
    user = input("enter the username: ")
    if user  in my_dict.keys():
        pas = input("enter the password: ")
        if pas==my_dict[user]:
            print('logined succesfully')
        else:
            print('wrong password,try again')
            login()
    else:
        print("username not found..try again")
        login()
def change():
    user = input("enter the username: ")
    if user in my_dict.keys():

        pas = input("enter the current password: ")
        if pas==my_dict[user]:
            pas1 = input("enter the new password: ")
            my_dict[user]=pas1
            print("password cahnged succesfully...")
        else:
            print("wrong password...try again")
            change()
    else:
        print("username not found...try again")
        change()
while True:
    num = int(input("press 1 for login, 0 for signup, 2 for change password and -1 for exit..."))
    if num==1:
        login()
    elif num==0:
        signup()
    elif num==2:
        change()
    else:
        print("thankyou...")
        break


    



    
