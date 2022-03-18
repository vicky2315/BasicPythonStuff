import re


def message():
    print("Welcome to the Login and Registration System")
    print("Please enter the number corresponding to the operation you want to perform")
    print("1) Registration")
    print("2) Login")
    print("3) Exit")


def registration(n):
    print("Welcome to the Registration Portal")
    b = re.compile('[1234567890@_!#$%^&*()<>?/\|}{~:]')
    c = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    a = 1

    username = input("Enter your username or email ID : ")
    while a != 0:
        if b.search(username[0]) is None:
            a = 0
            break
        else:
            username = input("Invalid username, please do not use numbers or special characters in the beginning : ")

    if username.count("@") > 0:
        if username.index('.') - username.index('@') == 1:
            username = input("Invalid email ID, please enter a valid website in your email ID : ")
    a = 1
    password = input("Enter a password with min of 5 characters and max of 12 characters. Please use a strong password for better security : ")
    while a != 0:
        if len(password) < 5 or len(password) > 16:
            password = input("Please enter a password within the specified limits : ")
        elif b.search(password) is None or c.search(password) is None:
            password = input("Please enter a password containing at least one number or special character : ")
        elif password.isupper() is True or password.islower() is True:
            password = input("Please enter a password with at least one upper and lower case: ")
        else:
            a = 0
    storeinfile(username,password)
    print("You have successfully registered with our system!")
    n = int(input("Please enter the next step you would like to do : "))
    return n


def storeinfile(uname,pword):
    with open('geek.txt', 'a+') as f:
        f.write(uname + " " + pword + "\n")


def login(n):
    print("Welcome to the Login Portal")
    useruname = input("Enter your username : ")
    userpwd = input("Enter your password : ")
    with open('geek.txt','a+') as f1:
        f1.seek(0)
        content = f1.read()
        contents = content.split()
    if useruname not in contents:
        print("You are not registered with our system, please register first")
    else:
        if userpwd not in contents:
            a = input("Have you forgotten your password? If yes enter y, or no then enter n: ")
            if a == 'y':
                useruname = input("Please enter the right username to retrieve your password : ")
                print(contents[contents.index(useruname)+1])
            else:
                print("You are not registered with our system, please register first")
        else:
            print('You have successfully logged in to our system')
    n = int(input("Enter the next step you would like to do : "))
    return n

message()
n = int(input())
while n != 0:
    if n == 1:
        n = registration(n)
    elif n == 2:
        n = login(n)
    elif n == 3:
        print('Thank you for using our portal!')
        break
    else:
        print('Please enter a number given within the range')
        n = int(input())




