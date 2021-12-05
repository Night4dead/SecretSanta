from typing import OrderedDict
import tools.helpers as lh
from time import sleep

test_dict = {"one":"three","two":"five","three":"one","four":"four","five":"two"}

def dispSecretSantaCouple(santa,secret):
    print("\033[0;31m"+santa+"\033[0m is the secret santa of \033[1;32m"+secret+"\033[0m")

def dispSecretSantaList(def_list):
    for x in def_list:
        dispSecretSantaCouple(x,def_list[x])

def checkFullShuffle(couples,santas):
    for x in couples:
        if (x,couples[x]) in santas.items():
            return False
        if santas[x] == x: 
            return False
    return True

def secretSantaAuto(couples):
    spinner = lh.spinning_cursor()
    print("\n\033[1;34m     generating secret santas ...\033[0m")
    while True:
        santas = list(couples.keys())
        santas = lh.shuffleList(santas)
        secret_santas_dict = dict(OrderedDict(zip(santas,list(couples.values()))))
        if checkFullShuffle(couples, secret_santas_dict):
            break
        print(f'\r\033[1;36m         rechecking  {next(spinner)}\033[0m', end = "\r")
        sleep(0.1)
    print("\033[1;34m     Finished generation\033[0m \n")
    return secret_santas_dict

""" def secretSanta(participant_list,couples):
    print("Welcome to the Secret Santa app !")
    user = getUser(participant_list)
    participant_list = lh.removeFromList(participant_list,user)
    temp_couples = lh.removePairFromDict(user,couples)
    secret = returnRandomItem(lh.getInputList(temp_couples))
    couples = lh.removeFromDict(secret,couples)
    displayCouple(user,secret)
    while input("Press enter to continue ... ") != "":
        pass
    return participant_list """

if __name__ == "__main__":
    dispSecretSantaList(secretSantaAuto(test_dict))