import colorama
from colorama import Fore
import random
import time
import secrets
import string
import os

os.system('clear')

print(Fore.RED + "______       ______      _  _                            ")
time.sleep(0.1)
print(Fore.RED + "| ___ \      |  ___|    | || |                           ")
time.sleep(0.1)
print(Fore.RED + "| |_/ / ___  | |_  ___  | || |  ___ __      __ ___  _ __ ")
time.sleep(0.1)
print(Fore.RED + "|    / / _ \ |  _|/ _ \ | || | / _ \\ \ /\ / // _ \| '__|")
time.sleep(0.1)
print(Fore.RED + "| |\ \| (_) || | | (_) || || || (_) |\ V  V /|  __/| |   ")
time.sleep(0.1)
print(Fore.RED + "\_| \_|\___/ \_|  \___/ |_||_| \___/  \_/\_/  \___||_|   ")
time.sleep(1)
print('Made by Jaymes#3351')

time.sleep(1)
print(Fore.BLUE + 'Bots in stock:',random.randint(100000, 500000))
time.sleep(1)

username = input(Fore.RED + 'Username: ')
amount = input('Amount of followers: ')
amount = int(amount)
             
             
                          
             
for line in range(amount):
    
    time.sleep(0)
    bot = ''.join(secrets.choice(string.ascii_letters + string.digits)
                         for i in range(8))
    print(Fore.GREEN + "Followed User:",username,"With Bot:",bot)
