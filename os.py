import subprocess
import os
import shutil

def rm_recursive(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        input(f"Error: {path} does not exist.")
    except PermissionError:
        input(f"Error: Permission denied for {path}.")
    except Exception as e:
        input(f"Error: {e}")

def vim(filename):
    os.system(f'vim {filename}')

def nano(filename):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()

        print("Nano-like editor. Type X to save and exit.")
        for line in lines:
            print(line.rstrip('\n'))

        while True:
            line = input()
            if line == 'X':
                break
            file.write(line + '\n')

        file.close()

def ls():
    process = subprocess.Popen("dir", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode().strip()

def rm(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        os.rmdir(path)
    else:
        input(f"Error: {path} does not exist or is not a valid file or directory.")

while True:
    os.system("cls")
    print(os.getcwd())
    command = input("Enter Linux Command: ")
    if "ls" in command:
        ls_output = ls()
        os.system("cls")
        input(ls_output)
    elif "cd" in command:
        path = command.replace("cd ", "")
        os.chdir(path)
        os.system("cls")
        input("Directory Changed: "+os.getcwd())
    elif "mkdir" in command:
        path = command.replace("mkdir ", "")
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        os.system("cls")
        input("Directory Created: "+os.getcwd())
    elif "rm" in command:
        if command == "rm -r":
            path = os.getcwd()
            os.system("cls")
            rm_recursive(path)
        else:
            path = command.replace("rm ", "")
            os.system("cls")
            rm(path)
    elif "nano" in command:
        path = command.replace("nano ", "")
        os.system("cls")
        nano(path)
    elif "vim" in command:
        path = command.replace("vim ", "")
        os.system("cls")
        vim(path)
