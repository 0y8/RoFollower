import colorama
from colorama import Fore
import random

print(Fore.BLUE + '██╗     ███████╗')
print(Fore.BLUE + '██║     ██╔════╝')
print(Fore.BLUE + '██║     ███████╗')
print(Fore.BLUE + '██║     ╚════██║')
print(Fore.BLUE + '███████╗███████║')
print(Fore.BLUE + '╚══════╝╚══════╝')
print('Made by complex#3351')

username = input('Username: ')
amount = input('Amount of followers: ')
amount = int(amount)

for line in range(amount):
    print(Fore.GREEN + "Followed",username,"With Bot #",random.randint(1, 1220000))
