import requests,random,os,time,webbrowser 
from user_agent import generate_user_agent
headers={'user-agent': generate_user_agent()}
E = '\033[1;37m'
B = '\033[2;96m'
G = '\033[1;12m'
S = '\033[1;23m'
webbrowser.open('https://t.me/Pak_Trick')
logo = '\x1b[97;1m  \n\x1b[97;1m  \n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m  \x1b[1;37m OWNER.    :-\x1b[1;37m PAK TRICK x UNKOWN SCRIPTER \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mDEVELOPER :- \x1b[1;37mMR ILYAS\x1b[1;37m                  \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mTELEGRAM  :- \x1b[1;306m@Pak_TRICK\x1b[1;37m                    \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   TOOL      :- \x1b[1;37mNON &&                           \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   version   :- \x1b[1;37mD\x1b[1;37m                                \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   TOOL      :-\x1b[1;38m PAID  \x1b[1;37m                           \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;97m'
webbrowser.open('https://t.me/Pak_Trick')
def like():
 user='qwertyuiopasdfghjklzxcvbnm'
 os.system('clear')
 urlm=input('\x1b[97;1m  \n\x1b[97;1m  \n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m  \x1b[1;37m OWNER.    :-\x1b[1;37m PAK TRICK x UNKOWN SCRIPTER \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mDEVELOPER :- \x1b[1;37mMR ILYAS\x1b[1;37m                  \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mTELEGRAM  :- \x1b[1;306m@Pak_TRICK\x1b[1;37m                    \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   TOOL     :-\x1b[1;38m PAID  \x1b[1;37m                           \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;97m'
'Enter TikTok Video Link:- ')
 urlm=urlm.split('/?')[0]
 urlm1=urlm
 id=2410
 qu= 1000
 fol=0
 def likes(id,fol):
  while True:
   url = 'https://fastfame.com/api/v2'
   rn = str("".join(random.choice(user)for i in range(4)))
   urlm=(urlm1+'/?igshid=YmMyMTA'+rn+'2M2Y=')
   data={'key':key,'action':'add','service':id,'link':urlm,'quantity':qu,}
   abhi=requests.post(url,data=data)
   if 'You have active order with this link. Please wait until order being completed.' in abhi.text:
    print('[+] Wait The Past Order Complet')
   if '{"order":' in abhi.text:
    print('\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●')
   if 'Invalid API key' in abhi.text:
    print(f'{E}[×] tool dead bro paid tool lele @pak_trick')
    exit()
   if 'Bad link' in abhi.text:
     print('link sahi nhi hai')
   if 'Not enough funds on balance'in abhi.text:
    print('dead ho gaya bro paid tool lele ye sab error nhi aayega dm :- @Pak_Trick')
    likes(id,fol)
   else:
    print(abhi.json())
 likes(id,fol)
os.system('clear')
key='ade90ae48d73ca2ffaddab411714d950'
url ='https://fastfame.com/api/v2'
data={'key':key,'action':'balance'}
abhi=requests.post(url,data=data,headers=headers)
if 'Invalid key' in abhi.text:
 print(f'{E}[×] TOOL DEAD BRO ')
 print(f'{B}[=] by paid tools here  ==> @Pak_Trick ')
 exit()
else:
  os.system('clear')
  ch=input('\x1b[97;1m  \n\x1b[97;1m  \n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m  \x1b[1;37m OWNER.    :-\x1b[1;37m PAK TRICK x UNKOWN SCRIPTER \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mDEVELOPER :- \x1b[1;37mMR ILYAS\x1b[1;37m                  \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;31m   \x1b[1;37mTELEGRAM  :- \x1b[1;306m@Pak_TRICK\x1b[1;37m                    \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a:*:~\x1b[1;37m   TOOL     :-\x1b[1;38m PAID  \x1b[1;37m                           \x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;33m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;30m\x1a:*:~\x1b[1;31m\x1b[1;33m\x1a~:*:\x1b[1;34m\x1a~:*::\x1b[1;30m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;37m\x1a~:*:\x1b[1;34m\x1a~:*:\x1b[1;39m\x1a~:*:\x1b[1;31m\x1a~:*:\x1b[1;32m\x1a~:*:\x1b[1;33m\x1a~:*:\x1b[1;37m:\n\x1b[1;91m●\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m❴\x1b[47m\x1b[1;30m ᴘᴀᴋ ᴛʀɪᴄᴋ \x1b[40m\x1b[00m\x1b[1;91m ❵\x1b[1;91m\x1b[1;92m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;91m═\x1b[1;92m━\x1b[1;93m═\x1b[1;94m━\x1b[1;95m═\x1b[1;96m━\x1b[1;90m═\x1b[1;97m━\x1b[1;94m═\x1b[1;92m━\x1b[1;91m═\x1b[1;95m━\x1b[1;90m═\x1b[1;96m━\x1b[1;90m═\x1b[1;91m●\n\x1b[1;97m'f'''{B}[{G}01{B}] {S} TikTok Views
  press 1 and enter
{G}Choose ==> ''')
  if ch == '1' or ch == '01':
   like()
   webbrowser.open('https://t.me/Pak_Trick')