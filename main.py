import colorama
from colorama import Fore
import random
import time
import secrets
import string

# Printing the logo and account stock.

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
# Generating a random number for the account stock.
print(Fore.RED + 'Bots in stock:',random.randint(100000, 500000))
# Waiting one second to ask for the user input.
time.sleep(1)
# Getting the user input vars.
username = input(Fore.BLUE + 'Username: ')
amount = input('Amount of followers: ')
# Converting the 'amount' var to an int.
amount = int(amount)
# The string length for the username.
str_length = 8
# getting the "amount" of followers the user wants.
for line in range(amount):
    # Cooling down the print function.
    time.sleep(00.1)
    # Generating a random string for the username.
    r_string = ''.join(secrets.choice(string.ascii_letters + string.digits)
                   for i in range(str_length))
    # Printing out all the vars.
    print(Fore.GREEN + "Followed",username,"With Bot:",r_string)
