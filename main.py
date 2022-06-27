import colorama
from colorama import Fore
import random
import time
import secrets
import string
import os

os.system('clear')

print(Fore.BLUE + '██████╗ ███████╗██████╗')
time.sleep(0.1)
print(Fore.BLUE + '██╔══██╗██╔════╝██╔══██╗')
time.sleep(0.1)
print(Fore.BLUE + '██████╔╝█████╗  ██████╔╝')
time.sleep(0.1)
print(Fore.BLUE + '██╔══██╗██╔══╝  ██╔══██╗')
time.sleep(0.1)
print(Fore.BLUE + '██║  ██║██║     ██████╔╝')
time.sleep(0.1)
print(Fore.BLUE + '╚═╝  ╚═╝╚═╝     ╚═════╝')
time.sleep(1)
print('Made by complex#3351')

time.sleep(1)
print(Fore.RED + 'Bots in stock:',random.randint(100000, 500000))
time.sleep(1)

username = input(Fore.BLUE + 'Username: ')
amount = input('Amount of followers: ')
amount = int(amount)
             
             
                          
             
for line in range(amount):
    
    time.sleep(0)
    bot_number = random.randint(100000, 500000)
    print(Fore.GREEN + "Followed User:",username,"With Bot #:",bot_number)
