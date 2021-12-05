from secret_santa import dispSecretSantaList
from secret_santa import secretSantaAuto
import os
import helpers as lh
from smtp_mail_server import usemail
from smtp_mail_server import configserver
from message_generator import messageGen
import file_saver as fs

try:    
    from mail_credentials import s_mail, s_password
    no_credentials = False
    server_password = s_password
    server_mail = s_mail
except:
    no_credentials = True
    server_password = ""
    server_mail = ""    


clear = lambda: os.system("clear")

yes = ["yes","y"]
no = ["no","n"]

couples = {}
mails = {}


def saveResult(result):
    pass

def sendResult(result,mails):
    print("sending mails ... ")
    try:
        server = configserver(server_mail,server_password)
        for x in mails:
            print("generating mail for "+x)
            message = messageGen(x,result[x])
            print("sending mail for "+x)
            usemail(server,server_mail,mails[x],message,x + " you are the secret santa of ...")
    except Exception as e:
        print(e)
    finally:
        server.close()
        clear()
        print("finished sending mails, happy secret santa !")

def display(dict_list):
    dispSecretSantaList(dict_list)

def runAll(dict_list,mails):
    clear()
    while input("Press enter to generate secrete santa list ! (press Enter)") != "":
        pass
    results = secretSantaAuto(dict_list)
    #display(results)
    if(mails != {}):
        res = lh.correctInput(["mail","file"],"Do you want to save results to files or send them by mail ? (mail or file)")
        if res == "mail":
            sendResult(results,mails)
        elif res == "file":
            saveResult(results)
    else:
        saveResult(results)

if __name__ == "__main__":
    print("Welcome to secret santa !")
    if no_credentials:
        print("enter the server mail :")
        server_mail = lh.correctEmailInput() 
        server_password = lh.notEmptyInput("Please enter the server mail password : ")
    res = lh.correctInput(yes+no,"do you want to enter your own participants' list ? ('y'es or 'n'o)")
    if res in yes:
        clear()
        couples, mails = lh.inputCouples()
    elif res in no:
        try:
            import test_couples_mails
            couples = test_couples_mails.couples
            mails = test_couples_mails.mails
        except:
            print("No default couples and mails, you have to input your list")
            clear()
            couples, mails = lh.inputCouples()
    try:
        runAll(couples,mails)
    except Exception as e:
        print(e)