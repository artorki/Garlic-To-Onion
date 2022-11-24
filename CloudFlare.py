# Garlic To Onion / Cloud Flare


from time import sleep
from ipapi import location
from socket import gethostbyname

from Banner import banner


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


def cloud_flare() :

    while True :

    
        banner()

        sleep (0.05)
        print (yellow , "–•[Cloud Flare]•–———————————————————————————————————————————————————————————")


        sleep (0.05)
        print (yellow , "\n [~] ENTER A URL:")
    
        sleep (0.05)
        print (white)
        url = input(" @G.O>>> ") . lower()

        if url == "0" :
            exit()
        
        elif url == "" :
            print (red , "\n [!] ERROR")
            exit()


        sub_list = ["home","admin","administrator","blog","blogs","shop","downloads","webmail","mail","email","mysql","local","localhost","cpanel","ftp","direct","forums","www","www1","www2","www3","www4","www5","api","server","vpn"]

        try :
            sleep (0.05)
            print (green)
            print (" [+] " + gethostbyname(str(url)) + " : " + url)
        
        except :
            print (red , "\n [!] Error")
            exit()

        
        for i in sub_list :

            try :
                host = str(i) + "." + url
                ip = gethostbyname (str(host))
                loc = location (ip)
                print (" [+] " + loc["country_name"] + " : " + ip + " : " + host)
            
            except :
                pass
    
    
        print (yellow , "\n Finish")

        input()
