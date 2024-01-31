from random import randint
import os

u_pwd = input("Please input Password: ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# pwd = ['0','1','2','9','4']

pw = ""
while pw != u_pwd:
    pw = ""
    for _ in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw += guess_pwd
    print("Cracking Password...Please wait:", pw)
    os.system("cls")  # For Windows systems, use 'clear' for Unix/Linux/MacOS
print("Your Password is:", pw)
