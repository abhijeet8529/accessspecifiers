dict = {'abhi': 'oof',
        'loss': 'win',
        'on': 'down',
        'tmkoc': 'jethalal',
        'rick grimes': 'we are the ones who lives',
        'navratri': 'jai mata di',
        'pubg': 'm416'
        }
username = input("enter your username here :")
if username in dict:
    password = input("Enter your password here :")
    if dict[username] == password:
        print("welcome , you're logged in successfully")
    else:
        print("incorrect password or username,please try again")
