from random import shuffle
from time import sleep
import os
import re   
  
regex = '[^@]+@[^@]+\.[^@]+'#'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

yes = ["yes","y"]
no = ["no","n"]

clear = lambda: os.system("clear")

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def shuffleList(list_to):
    shuffle(list_to)
    return list_to
    
def correctInput(inputs,msg):
    while True:
        res = input(msg) 
        if res not in inputs:
            pass
        else:
            break
    return res

def notEmptyInput(message):
    while True: 
        name = input(message)
        if name == "":
            print("Enter text ...")
            pass
        else:
            break
    return name

def correctEmailInput():
    while True: 
        mail = input("Enter a valid email address : ")
        if not re.search(regex,mail):
            print("Enter a valid email ...")
            pass
        else:
            break
    return mail

def waiter(message,timer):
    i = 0
    spinner = spinning_cursor()
    while i < timer:
        print(f'\r\033[1;36m '+ message + f'  {next(spinner)}\033[0m', end = "\r")
        i+=1
        sleep(0.1)

def inputPerson():
    name = notEmptyInput("Enter your firstname and lastname : (then press enter) ")
    mail = correctEmailInput()
    return name, mail

def inputLoop():
    dic_to_fill = {}
    while True: 
        print(dic_to_fill)
        name, mail = inputPerson()
        dic_to_fill[name] = mail
        nxt = correctInput(yes+no,"Add another user ? ('y'es or 'n'o) : ")
        if nxt in yes:
            clear()
            pass
        else:
            break
    if len(list(dic_to_fill.keys())) <= 3:
        raise ValueError("You need to have at least four persons for the shuffling to work")
    return dic_to_fill

def couplesLoop(users):
    couples = {}
    temp = users
    while temp != []:
        current_user = temp[0]
        print("You are : "+current_user)
        couples[current_user] = correctInput(temp,"Enter the name of your partner (enter your name if you're single) : ")
        partner = couples[current_user]
        couples[partner]=current_user
        temp = [x for x in temp if x != current_user and x != partner]
    return couples

def inputCouples():
    waiter("prepare to input names and emails of the participants",20)
    mailing = inputLoop()
    waiter("prepare to input names of your partners",20)
    users = list(mailing.keys())
    couples = couplesLoop(users)
    return couples,mailing

if __name__ == "__main__":
    print("helper functions concerning lists and dictionaries")