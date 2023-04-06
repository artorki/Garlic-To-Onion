import platform, os, sys, getpass, json

System = platform.uname()[0]
Clear = lambda : os.system ("cls" if System == "Windows" else "clear")
Clear()


libraries = ["Config", "colorama", "time", "requests", "socket"]

def Check(x) :
    try:
        exec (f"import {x}")
    except:
        sys.exit (f" [-] Error (Import-L13) - Install {x}")
x = [Check(i) for i in libraries]

import Config, time, socket, requests

from colorama import Fore, init
init()
white, cyan = "\033[0;37m", "\033[96m"


def Banner() :
    num = Config.time_out
    while num >= 0 :

        try:
            Connection = requests.get ("https://google.com")
            print (Fore.WHITE, f"""
  --██████████-██████████-██████████-██-------██-██████████--██████████-██████████
 |--██---------██------██-██------██-██-------██-██--------------██-----██------██
 |--██---█████-██████████-████████---██-------██-██--------------██-----██------██
 |--██------██-██------██-██------██-██-------██-██--------------██-----██------██
 |--██████████-██------██-██------██-████████-██-██████████------██-----██████████
 |----------------------------------------------------
 |--██████████-████----██-██-██████████-████----██--██
 |--██------██-██-██---██-██-██------██-██-██---██--██       ARTorki - V3
 |--██------██-██--██--██-██-██------██-██--██--██--██
 |--██------██-██---██-██-██-██------██-██---██-██----       Hello  {getpass.getuser()}
  --██████████-██----████-██-██████████-██----████--██
""")
            break

        except:
            Clear()
            print (Fore.WHITE, f"""
  --██████████-██████████-██████████-██-------██-██████████--██████████-██████████
 |--██---------██------██-██------██-██-------██-██--------------██-----██------██
 |--██---█████-██████████-████████---██-------██-██--------------██-----██------██
 |--██------██-██------██-██------██-██-------██-██--------------██-----██------██
 |--██████████-██------██-██------██-████████-██-██████████------██-----██████████
 |----------------------------------------------------
 |--██████████-████----██-██-██████████-████----██--██
 |--██------██-██-██---██-██-██------██-██-██---██--██       ARTorki - V3
 |--██------██-██--██--██-██-██------██-██--██--██--██       Connection Error
 |--██------██-██---██-██-██-██------██-██---██-██----       Closed: {num} s
  --██████████-██----████-██-██████████-██----████--██
""")
            num -= 1
            sys.exit() if num == -1 else time.sleep (1)


def Modules () :
    SubList = Config.SubList
    Port = Config.Port
    Iran = ""

    print (f"{white} =====================================================")
    try:
        URL = input (f"{cyan} [{white}~{cyan}] {white}Enter URL: {cyan}") .lower()
        URL.replace("https://","").replace("http://","").replace("www.","") if "https://" == URL or "http://" == URL or "www." == URL else ...
    except:
        sys.exit()

    print (f"{white} =====================================================")
    print (f"{cyan} [{white}~{cyan}] {white}Location, URL, IP")
    for i in SubList :
        if i != "" :
            URL = i + "." + URL
        else:
            pass
        try:
            IP = socket.gethostbyname (URL)
            Location = requests.post ("https://iplocation.com/", data={"ip": f"{IP}"}) .text
            Location = str(json.loads (Location) ["country_name"]) .replace(" ","")
            print (f"{cyan} [{white}+{cyan}] {cyan}{Location}, {URL}, {IP}")
            if Iran == "" and Location == "Iran" :
                Iran = IP
        except:
            try:
                Connection = requests.get ("https://google.com")
            except:
                sys.exit()

    print (f"{white} =====================================================")
    print (f"{cyan} [{white}~{cyan}] {white}Port, service")
    for i in Port :
        try:
            scan = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            scan = scan.connect_ex ((Iran, i))
            if scan == 0 :
                service = socket.getservbyport (i)
                print (f"{cyan} [{white}+{cyan}] {cyan}{service}, {i}")              
        except:
            try:
                Connection = requests.get ("https://google.com")
            except:
                sys.exit()

    print (f"{white} =====================================================")
    print (f"{cyan} [{white}~{cyan}] {white}Key, Value")
    # for i in Port :
    #     try:
    #         scan = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    #         scan = scan.connect_ex ((Iran, i))
    #         if scan == 0 :
    #             service = socket.getservbyport (i)
    #             print (f"{cyan} [{white}+{cyan}] {cyan}{service}, {i}")              
    #     except:
    #         pass


Banner()
Modules()
