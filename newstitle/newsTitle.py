import time
import concurrent.futures
import requests
import datetime
import colorama
import os
import sys
import threading
from time import gmtime, strftime, sleep
from colorama import init, Fore, Back, Style
api_lock = threading.Lock()
os.system("title getTitleNews-sf")
os.system('cls')

#Token for the program to acces the api
tokenOpen = open("token.txt", "r")
userToken = tokenOpen.read()  

token = 'userToken'

getTitle = requests.get('https://77ee.playfabapi.com/Client/GetTitleNews', json={}, headers={"X-Authorization": token})

if "OK" not in str(getTitle):
    print(Fore.RED + "Status not ok?".center(os.get_terminal_size().columns))
        
else:
    print(Fore.GREEN + "Status is ok?".center(os.get_terminal_size().columns))
#FreePar

