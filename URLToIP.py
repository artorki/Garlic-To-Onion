# Garlic To Onion / URL To IP


from time import sleep
from socket import gethostbyname
from colorama import Fore

from Banner import banner


ly,lr,lg,w = Fore.LIGHTYELLOW_EX,Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.WHITE


def url_ip() :
    
    banner()

    sleep (0.05)
    print (ly , "–•[URL TO IP]•–———————————————————————————————————————————————————————————")

    
    sleep (0.05)
    print (ly , "\n [~] ENTER A URL:")

    sleep (0.05)
    print (w)
    url = input(" @G.O>>> ") . lower()

    if url == "0" :
        exit()
        
    elif url == "" :
        print (lr , "\n [!] ERROR")
        exit()


    try :
        ip = gethostbyname(url)
        print (lg , "\n [+] IP:" , ip)

    except :
        print (lr , "\n [!] ERROR")
    
    
    print(ly,"\n Finish")
