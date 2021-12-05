import tools.helpers as lh
from secret_santa.message_generator import messageGen as msgGen
import os
import shutil

def gen_file(santa, dest):
    message = msgGen(santa,dest)
    file = open("save/"+santa+".txt","x")
    file.close()
    file = open("save/"+santa+".txt","w")
    file.write(message)
    file.close()


def check_dir():
    if os.path.isdir("save"):
        shutil.rmtree("save")
    os.mkdir("save")

def save_to_file(result):
    print("Saving to files ...")
    check_dir()
    spinner = lh.spinning_cursor()
    for santa in result:
        print(f'\r\033[1;36m         saving...  {next(spinner)}\033[0m', end = "\r")
        gen_file(santa, result[santa])
    print("saving files finished ! \n")


if __name__ == "__main__":
    print("file creator")