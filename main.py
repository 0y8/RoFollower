import colorama
from colorama import Fore
import random
import time
import sys

print(Fore.BLUE + '██╗     ███████╗')
print(Fore.BLUE + '██║     ██╔════╝')
print(Fore.BLUE + '██║     ███████╗')
print(Fore.BLUE + '██║     ╚════██║')
print(Fore.BLUE + '███████╗███████║')
print(Fore.BLUE + '╚══════╝╚══════╝')
print('Made by Jaymes#3351')

username = input('Username: ')
amount = input('Amount of followers: ')
amount = int(amount)


for line in range(amount):
    time.sleep(0.2)
    print(Fore.GREEN + "Followed",username,"With Bot #",random.randint(1, 1220000))
