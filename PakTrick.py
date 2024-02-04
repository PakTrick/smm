# This script is decrypted by shoaib hassan
# mujhy pta hai baad mai credit hta do gy 
# bs choro gali nahi do ga

import webbrowser
import requests
import random
import os
import time
import webbrowser
from user_agent import generate_user_agent
headers = {
    'user-agent': generate_user_agent() }
logo = '\x1b[97;1m  \n\x1b[97;1m  \n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m  \x1b[1;37m OWNER.    :-\x1b[1;37m PAK TRICK x UNKOWN SCRIPTER \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mDEVELOPER :- \x1b[1;37mMR ILYAS\x1b[1;37m                  \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mTELEGRAM  :- \x1b[1;306m@Pak_TRICK\x1b[1;37m                    \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   TOOL      :- \x1b[1;37mNON &&                           \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   version   :- \x1b[1;37mD\x1b[1;37m                                \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   TOOL      :-\x1b[1;38m PAID  \x1b[1;37m                           \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;97m'

webbrowser.open('https://t.me/Pak_Trick')
def IGVIEW1():
    user = 'qwertyuiopasdfghjklzxcvbnm'
    os.system('clear')
    print(logo)
    urlm = input('   ENTER TO IG VIEW link :- ')
    urlm = urlm.split('/?')[0]
    urlm1 = urlm
    id = 2409
    qu = 100
    fol = 0
    
    def likes(id = None, fol = None):
        url = 'https://fastfame.com/api/v2'
        rn = str(''.join(random.choice(user) for i in range(int(4))))
        urlm = urlm1 + '/?igshid=YmMyMTA' + rn + '2M2Y='
        data = {
            'key': key,
            'action': 'add',
            'service': id,
            'link': urlm,
            'quantity': qu }
        abhi = requests.post(url, data=data)
        if 'You have active order with this link. Please wait until order being completed.' in abhi.text:
            print('[+] Wait The Past Order Complet')
        if '{"order":' in abhi.text:
            print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
        if 'Invalid API key' in abhi.text:
            print(f'''{E}[×] @PakOwner''')
            exit()
        if 'Bad link' in abhi.text:
            print('link sahi nhi hai')
        if 'No money no honey' in abhi.text:
            print('@PakOwner')
            likes(id, fol)
        print(abhi.json())


    likes(id, fol)

os.system('clear')
key = '4215db89ffacf44d91096a02b736dd3a'
url = 'https://fastfame.com/api/v2'
data = {
    'key': key,
    'action': 'balance' }
abhi = requests.post(url, data=data, headers=headers)
if 'Key galat h bro' in abhi.text:
    print(f'''{E}[×] lelo pudina''')
    print(f'''{B}[=] by free tools here  ==> @PakOwner''')

def A():
    os.system('clear')
    print(logo)
    print('\x1b[1;96m[1] IG VIEW')
    print('[2] HOME MENU')
    print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
    choice = input('\x1b[1;90mEnter your choice : \x1b[1;95m')
    if choice == '1' or choice == '01':
        IGVIEW1()
    if choice == '2' or choice == '02':
        main()
    print('Invalid choice. Please enter ')


def tk():
    user = 'qwertyuiopasdfghjklzxcvbnm'
    os.system('clear')
    print(logo)
    urlm = input('   ENTER TO tik-tok VIEW link :- ')
    urlm = urlm.split('/?')[0]
    urlm1 = urlm
    id = 2410
    qu = 100
    fol = 0
    
    def likes(id = None, fol = None):
        url = 'https://fastfame.com/api/v2'
        rn = str(''.join(random.choice(user) for i in range(int(4))))
        urlm = urlm1 + '/?igshid=YmMyMTA' + rn + '2M2Y='
        data = {
            'key': key,
            'action': 'add',
            'service': id,
            'link': urlm,
            'quantity': qu }
        abhi = requests.post(url, data=data)
        if 'You have active order with this link. Please wait until order being completed.' in abhi.text:
            print('[+] Wait The Past Order Complet')
        if '{"order":' in abhi.text:
            print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
        if 'Invalid API key' in abhi.text:
            print(f'''{E}[×] @PakOwner''')
            exit()
        if 'Bad link' in abhi.text:
            print('link sahi nhi hai')
        if 'No money no honey' in abhi.text:
            print('@PakOwner')
            likes(id, fol)
        print(abhi.json())


    likes(id, fol)

os.system('clear')
key = '4215db89ffacf44d91096a02b736dd3a'
url = 'https://fastfame.com/api/v2'
data = {
    'key': key,
    'action': 'balance' }
abhi = requests.post(url, data=data, headers=headers)
if 'Key galat h bro' in abhi.text:
    print(f'''{E}[×] lelo pudina''')
    print(f'''{B}[=] by free tools here  ==> @PakOwner''')

def B():
    os.system('clear')
    print(logo)
    print('\x1b[1;96m[1] TIK-TOK VIEW')
    print('[2] HOME MENU')
    print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
    choice = input('\x1b[1;90mEnter your choice : \x1b[1;95m')
    if choice == '1' or choice == '01':
        tk()

    if choice == '2' or choice == '02':
        main()

    print('Invalid choice. Please enter ')



def tt():
    user = 'qwertyuiopasdfghjklzxcvbnm'
    os.system('clear')
    print(logo)
    urlm = input('   ENTER TO TWITTER VIEW link :- ')
    urlm = urlm.split('/?')[0]
    urlm1 = urlm
    id = 2411
    qu = 100
    fol = 0
    
    def likes(id = None, fol = None):
        url = 'https://fastfame.com/api/v2'
        rn = str(''.join(random.choice(user) for i in range(int(4))))
        urlm = urlm1 + '/?igshid=YmMyMTA' + rn + '2M2Y='
        data = {
            'key': key,
            'action': 'add',
            'service': id,
            'link': urlm,
            'quantity': qu }
        abhi = requests.post(url, data=data,headers=headers)
        if 'You have active order with this link. Please wait until order being completed.' in abhi.text:
            print('[+] Wait The Past Order Complet')
        if '{"order":' in abhi.text:
            print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
        if 'Invalid API key' in abhi.text:
            print(f'''{E}[×] @PakOwner''')
            exit()
        if 'Bad link' in abhi.text:
            print('link sahi nhi hai')
        if 'No money no honey' in abhi.text:
            print('@PakOwner')
            likes(id, fol)

        print(abhi.json())


    likes(id, fol)

os.system('clear')
key = 'c9412152e86fd527b6dbe9e86b36a4ca'
url = 'https://fastfame.com/api/v2'
data = {
    'key': key,
    'action': 'balance' }
abhi = requests.post(url, data=data, headers=headers)
if 'Key galat h bro' in abhi.text:
    print(f'''{E}[×] lelo pudina''')
    print(f'''{B}[=] by free tools here  ==> @PakOwner''')

def C():
    os.system('clear')
    print(logo)
    print('\x1b[1;96m[1] TWITTER VIEW')
    print('[2] HOME MENU')
    print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
    choice = input('\x1b[1;90mEnter your choice :\x1b[1;95m ')
    if choice == '1' or choice == '01':
        tt()

    if choice == '2' or choice == '02':
        main()

    print('Invalid choice. Please enter ')



def main():
    print('')
    os.system('clear')
    print(logo)
    print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
    print('\x1b[1;92m| \x1b[1;91m [\x1b[1;93mA\x1b[1;91m] \x1b[1;96mINSTA    VIEW UNLIMITED      \x1b[1;92m |   \x1b[1;95m●  \x1b[1;91m[ \x1b[1;93mON \x1b[1;91m]  \x1b[1;95m●\x1b[1;92m      |')
    print('\x1b[1;92m| \x1b[1;91m [\x1b[1;93mB\x1b[1;91m] \x1b[1;96mTIK-TOK  VIEW UNLIMITED      \x1b[1;92m |   \x1b[1;95m●  \x1b[1;91m[ \x1b[1;93mON \x1b[1;91m]  \x1b[1;95m●\x1b[1;92m      |')
    print('\x1b[1;92m| \x1b[1;91m [\x1b[1;93mC\x1b[1;91m] \x1b[1;96mTWITTER  VIEW UNLIMITED      \x1b[1;92m |   \x1b[1;95m●  \x1b[1;91m[ \x1b[1;93mON \x1b[1;91m]  \x1b[1;95m●\x1b[1;92m      |')
    print('\x1b[1;92m| \x1b[1;91m [\x1b[1;93mD\x1b[1;91m] \x1b[1;96mOWNER   CONTACT              \x1b[1;92m |   \x1b[1;95m●  \x1b[1;91m[ \x1b[1;93mON \x1b[1;91m]  \x1b[1;95m●\x1b[1;92m      |')
    print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
    choice = input('Enter your choice :\x1b[1;95m ')
    if choice == 'A' or choice == 'a':
        A()

    if choice == 'B' or choice == 'b':
        B()

    if choice == 'C' or choice == 'c':
        C()

    if choice == 'D' or choice == 'd':
        webbrowser.open('https://t.me/PakOwner')

    print('Invalid choice. Please enter ')


if __name__ == '__main__':
    main()
