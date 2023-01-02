from os import system, chdir, path
from colorama import Fore, init
from ctypes import windll
from time import sleep
from subprocess import run, DEVNULL, Popen, check_output
from requests import get

system("title " + "ProxOnion")
system("cls")

#Initialization of Colorama
init(convert=True)

def process_exists(process_name):
    progs = str(check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

def is_tor_running():
    #To see if Tor is running completely, a proxy query is made on an example site
    get('https://example.com', proxies={"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"})

def credits():
    system("cls")
    input(f"""{Fore.CYAN}
                                       WWNW         
                                 WNXXNNNXNW     
                             WWNX00K000KNW      
                           WWXKOxxxxkKNW               
                           X0kdllod0NW                          
                          NkllcclkXW                   
                      NXNW0l:;:o0W                     
                      XxxKx:,;l0W                          {Fore.LIGHTBLUE_EX}Credits :{Fore.CYAN} 
                       0ok0dllccO                      
                       XldX0kko;x                       
                      XdcOXOkddc:OW                             {Fore.LIGHTBLUE_EX}- Nathoune{Fore.CYAN}
                   N0dclONX0Okxxl:cxKW                             {Fore.LIGHTBLUE_EX}Discord : Nathoune#3630{Fore.CYAN}
                N0dlldOXNNKOOOOxxdl:;cxKW                          {Fore.LIGHTBLUE_EX}Email : nathoune987@proton.me{Fore.CYAN}
              XxccdOXNNNXXKOkO0Ododdoc,,cON                        {Fore.LIGHTBLUE_EX}GitHub : https://github.com/Nathoune987{Fore.CYAN}  
            Nx:ckXNNNXXKXNXOOkO0kllooooc;':OW          
           0c;xXNNNKKKXXNNKOOOkkOo:clllll:''oX         
          0;:0NNXK0KXNNNNNKOkO0kkx:;lcccccc,.lX        
         X:;ONNKO0XNNNNXXXKOxkOOxx:':ccc::::'.dW                {Fore.LIGHTBLUE_EX}- Willem{Fore.CYAN}
         x,oNNKOKNNNXKKXXNXOOkkOkd:.;::::::;;.;K                   {Fore.LIGHTBLUE_EX}Discord : willem#4488{Fore.CYAN}
        Wo,kNKO0NNX00KXNNNKOkOkxkd;.,:;;;;;;;.'O                   {Fore.LIGHTBLUE_EX}Email : contact.fw996@slmail.me{Fore.CYAN}
        Wo,kN0kXNXO0XNNNXK0xdk0xdo,.,;;;;;,,,.'O                   {Fore.LIGHTBLUE_EX}GitHub : https://github.com/willem895{Fore.CYAN}
         Nl;ON0kKOOXNNN0OXXOkdxxl:..',,,,,,'..xW       
          Kc:OX0k0kOXNNOOXX0kddd:,..',,,'''..oN            {Fore.LIGHTBLUE_EX}Press {Fore.CYAN}Enter {Fore.LIGHTBLUE_EX}to return to the main menu.{Fore.CYAN}
           Xo:o00kkkOXN0kKXOkdol,...'''''..'xN         
            W0lclddxdk0XOkKkooc,...'''...,oKW   
              WKxlc;,,:odolc;,.  ....';lkX      
                 WN0xollllc::;;;:cldkKN         
                        WWNNNNNWW""")
    system("cls")
    home()

def disable_tor_proxy():
    #Check if the script is launched in the adminstrator
    if windll.shell32.IsUserAnAdmin():
        print(f"{Fore.LIGHTBLUE_EX}\r\nKill Tor, and disable the proxy.\r\n{Fore.WHITE}")
        #Close tor.exe
        if process_exists('tor.exe'):
            run("TASKKILL /F /IM tor.exe", stdout=DEVNULL)
        else:
            print(f"{Fore.LIGHTRED_EX}Tor is not launched, disabling the proxy.\r\n{Fore.WHITE}")
        #Command to disable the proxy with regedit
        run(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f', stdout=DEVNULL)
        input(f"{Fore.LIGHTGREEN_EX}Proxy successfully disabled.\r\n\r\n{Fore.LIGHTBLUE_EX}Your Internet traffic no longer passes through the Tor servers. You can return to the main menu by pressing {Fore.CYAN}Enter{Fore.LIGHTBLUE_EX}.\r\nTo quit, use the {Fore.CYAN}\"[4] Quit option\"{Fore.LIGHTBLUE_EX}, to avoid errors. For enable the proxy, choose option {Fore.CYAN}\"[1] Set Tor Proxy\"{Fore.LIGHTBLUE_EX}.")
        system("cls")
        home()
    else:
        input(f"\r\n{Fore.LIGHTRED_EX}[!] Error {Fore.LIGHTBLUE_EX}run this in administrator.")
        system("cls")
        home()

def set_tor_proxy_debug():
    #Check if the script is launched in the adminstrator
    if windll.shell32.IsUserAnAdmin():
        print(f"{Fore.LIGHTBLUE_EX}\r\nLaunching Tor, please wait a moment.\r\n{Fore.WHITE}")
        try:
            chdir("assets")
        except FileNotFoundError:
            pass
        Popen(tor_launch_cmd)
        while True:
            try:
                is_tor_running()
                #Command to activate the proxy with regedit
                system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f')
                system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d "socks=127.0.0.1:9050" /f')
                #Verify that the changes are applied
                system(r'netsh winhttp import proxy source=ie')
                input(f"{Fore.LIGHTGREEN_EX}Proxy setup successfully.\r\n\r\n{Fore.LIGHTBLUE_EX}Your Internet traffic now goes through the Tor servers. You can return to the main menu by pressing {Fore.CYAN}Enter{Fore.LIGHTBLUE_EX}.\r\nTo quit, use the {Fore.CYAN}\"[4] Quit option\"{Fore.LIGHTBLUE_EX}, to avoid errors. For disable the proxy, choose option {Fore.CYAN}\"[2] Disable Tor Proxy\"{Fore.LIGHTBLUE_EX}.")
                system("cls")
                home()
            except:
                pass
    else:
        input(f"\r\n{Fore.LIGHTRED_EX}[!] Error {Fore.LIGHTBLUE_EX}run this in administrator.")
        system("cls")
        home()

def set_tor_proxy_silent():
    #Check if the script is launched in the adminstrator
    if windll.shell32.IsUserAnAdmin():
        print(f"{Fore.LIGHTBLUE_EX}\r\nLaunching Tor, please wait a moment.{Fore.WHITE}\r\n")
        #Open tor.exe in silent mode
        try:
            chdir("assets")
        except FileNotFoundError:
            pass
        #Open Tor in silent
        Popen(tor_launch_cmd, creationflags=8, close_fds=True)
        while True:
            try:
                is_tor_running()
                #Command to activate the proxy with regedit
                run(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f', stdout=DEVNULL)
                run(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d "socks=127.0.0.1:9050" /f', stdout=DEVNULL)
                input(f"{Fore.LIGHTGREEN_EX}Proxy setup successfully.\r\n\r\n{Fore.LIGHTBLUE_EX}Your Internet traffic now goes through the Tor servers. You can return to the main menu by pressing {Fore.CYAN}Enter{Fore.LIGHTBLUE_EX}.\r\nTo quit, use the {Fore.CYAN}\"[4] Quit option\"{Fore.LIGHTBLUE_EX}, to avoid errors. For disable the proxy, choose option {Fore.CYAN}\"[2] Disable Tor Proxy\"{Fore.LIGHTBLUE_EX}.")
                system("cls")
                home()
            except:
                pass
    else:
        input(f"\r\n{Fore.LIGHTRED_EX}[!] Error {Fore.LIGHTBLUE_EX}run this in administrator.")
        system("cls")
        home()

def custom_localization_exit_node():
    system("cls")
    print(f"{Fore.LIGHTBLUE_EX}Here are the most famous countries :\r\n")
    print(f"""{Fore.LIGHTBLUE_EX}aq{Fore.CYAN} : ANTARCTICA	        {Fore.LIGHTBLUE_EX}mc{Fore.CYAN} : MONACO 
{Fore.LIGHTBLUE_EX}ar{Fore.CYAN} : ARGENTINA	        {Fore.LIGHTBLUE_EX}no{Fore.CYAN} : NORWAY
{Fore.LIGHTBLUE_EX}au{Fore.CYAN} : AUSTRALIA	        {Fore.LIGHTBLUE_EX}pk{Fore.CYAN} : PAKISTAN
{Fore.LIGHTBLUE_EX}be{Fore.CYAN} : BELGIUM	        {Fore.LIGHTBLUE_EX}pl{Fore.CYAN} : POLAND
{Fore.LIGHTBLUE_EX}br{Fore.CYAN} : BRAZIL	        {Fore.LIGHTBLUE_EX}pt{Fore.CYAN} : PORTUGAL
{Fore.LIGHTBLUE_EX}ca{Fore.CYAN} : CANADA	        {Fore.LIGHTBLUE_EX}ru{Fore.CYAN} : RUSSIA 
{Fore.LIGHTBLUE_EX}dk{Fore.CYAN} : DENMARK 	        {Fore.LIGHTBLUE_EX}uk{Fore.CYAN} : SCOTLAND
{Fore.LIGHTBLUE_EX}eg{Fore.CYAN} : EGYPT	        {Fore.LIGHTBLUE_EX}rs{Fore.CYAN} : SERBIA
{Fore.LIGHTBLUE_EX}fi{Fore.CYAN} : FINLAND 	        {Fore.LIGHTBLUE_EX}si{Fore.CYAN} : SLOVENIA
{Fore.LIGHTBLUE_EX}fr{Fore.CYAN} : FRANCE	        {Fore.LIGHTBLUE_EX}za{Fore.CYAN} : SOUTH AFRICA
{Fore.LIGHTBLUE_EX}de{Fore.CYAN} : GERMANY 	        {Fore.LIGHTBLUE_EX}es{Fore.CYAN} : SPAIN
{Fore.LIGHTBLUE_EX}gr{Fore.CYAN} : GREECE	        {Fore.LIGHTBLUE_EX}se{Fore.CYAN} : SWEDEN
{Fore.LIGHTBLUE_EX}gl{Fore.CYAN} : GREENLAND 	        {Fore.LIGHTBLUE_EX}ch{Fore.CYAN} : SWITZERLAND 
{Fore.LIGHTBLUE_EX}is{Fore.CYAN} : ICELAND 	        {Fore.LIGHTBLUE_EX}tr{Fore.CYAN} : TURKEY
{Fore.LIGHTBLUE_EX}in{Fore.CYAN} : INDIA 	        {Fore.LIGHTBLUE_EX}ua{Fore.CYAN} : UKRAINE 
{Fore.LIGHTBLUE_EX}jp{Fore.CYAN} : JAPAN 	        {Fore.LIGHTBLUE_EX}uk{Fore.CYAN} : UNITED KINGDOM
{Fore.LIGHTBLUE_EX}lu{Fore.CYAN} : LUXEMBOURG	        {Fore.LIGHTBLUE_EX}us{Fore.CYAN} : UNITED STATES 
{Fore.LIGHTBLUE_EX}mx{Fore.CYAN} : MEXICO	        {Fore.LIGHTBLUE_EX}ve{Fore.CYAN} : VENEZUELA

To see all available countries : {Fore.LIGHTBLUE_EX}https://pastebin.com/raw/CNTWLQeg""")
    country_exit_node = input(f"\r\n\r\n{Fore.LIGHTBLUE_EX}Enter the abbreviation of the country you wish to select. Example: {Fore.LIGHTGREEN_EX}fr {Fore.LIGHTBLUE_EX}to select France or {Fore.LIGHTGREEN_EX}ua {Fore.LIGHTBLUE_EX}to select Ukraine\r\n{Fore.CYAN}\r\n  {Fore.LIGHTBLUE_EX}[{Fore.CYAN}>{Fore.LIGHTBLUE_EX}] {Fore.WHITE}Choice : {Fore.CYAN}")
    #If the path exists
    if path.exists(path.join("assets")):
        with open("assets/country_codes.txt") as country_codes:
            available_country = [line.rstrip() for line in country_codes]
        #If the country code is correct
        if country_exit_node in available_country:
            torrc_file = open(path.join("assets/Tor/torrc"), "w")
        else:
            input(f"\r\n{Fore.LIGHTRED_EX}[!] Error {Fore.LIGHTBLUE_EX}invalid country code.")
            system("cls")
            home()
    else:
        with open("country_codes.txt") as country_codes:
            available_country = [line.rstrip() for line in country_codes]
        if country_exit_node in available_country:
            torrc_file = open(path.join("Tor/torrc"), "w")
        else:
            input(f"\r\n{Fore.LIGHTRED_EX}[!] Error {Fore.LIGHTBLUE_EX}invalid country code.")
            system("cls")
            home()
    #Write to the torrc file to change the location of the exit node
    torrc_file.write(f"""GeoIPFile Tor\geoip
DataDirectory Tor
GeoIPv6File Tor\geoip6
ExitNodes {{{country_exit_node}}} StrictNodes 0""")
    torrc_file.close()
    if set_proxy_mod == "silent":
        set_tor_proxy_silent()
    elif set_proxy_mod == "debug":
        set_tor_proxy_debug()

def set_tor_proxy_localisation_menu():
    system("cls")
    print(f"""{Fore.CYAN}         
                                     ___                 ___       _             
                                    / _ \_ __ _____  __ /___\_ __ (_) ___  _ __  
                                   / /_)/ '__/ _ \ \/ ///  // '_ \| |/ _ \| '_ \{Fore.LIGHTBLUE_EX}
                                  / ___/| | | (_) >  </ \_//| | | | | (_) | | | |
                                  \/    |_|  \___/_/\_\___/ |_| |_|_|\___/|_| |_|""")
    print(f"""   
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.WHITE}
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ║            [{Fore.CYAN}1{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Random Localization (Exit Node)                      {Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Custom Localization (Exit Node)            {Fore.WHITE}║
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ║            [{Fore.CYAN}0{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Return To Main Menu                                                                                {Fore.WHITE} ║
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
    choice = input(f"\r\n  {Fore.LIGHTBLUE_EX}[{Fore.CYAN}>{Fore.LIGHTBLUE_EX}] {Fore.WHITE}Choice : {Fore.CYAN}")
    global tor_launch_cmd
    if choice == "1":
        tor_launch_cmd = r"tor.exe"
        if set_proxy_mod == "silent":
            set_tor_proxy_silent()
        elif set_proxy_mod == "debug":
            set_tor_proxy_debug()
    elif choice == "2":
        #Command to support the torrc file
        tor_launch_cmd = r"tor.exe -f Tor\\torrc"
        custom_localization_exit_node()
    elif choice == "0":
        system("cls")
        home()
    else:
        system("cls")
        set_tor_proxy_localisation_menu()

def set_tor_proxy_mod_menu():
    system("cls")
    print(f"""{Fore.CYAN}         
                                     ___                 ___       _             
                                    / _ \_ __ _____  __ /___\_ __ (_) ___  _ __  
                                   / /_)/ '__/ _ \ \/ ///  // '_ \| |/ _ \| '_ \{Fore.LIGHTBLUE_EX}
                                  / ___/| | | (_) >  </ \_//| | | | | (_) | | | |
                                  \/    |_|  \___/_/\_\___/ |_| |_|_|\___/|_| |_|""")
    print(f"""   
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.WHITE}
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ║          [{Fore.CYAN}1{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Silent Mode                  {Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Debug Mode (only if you had an error with the silent mode)          {Fore.WHITE} ║
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ║          [{Fore.CYAN}0{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Return To Main Menu                                                                                  {Fore.WHITE} ║
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
    choice = input(f"\r\n  {Fore.LIGHTBLUE_EX}[{Fore.CYAN}>{Fore.LIGHTBLUE_EX}] {Fore.WHITE}Choice : {Fore.CYAN}")
    if choice == "1":
        global set_proxy_mod
        set_proxy_mod = "silent"
        set_tor_proxy_localisation_menu()
    elif choice == "2":
        set_proxy_mod = "debug"
        set_tor_proxy_localisation_menu()
    elif choice == "0":
        system("cls")
        home()
    else:
        system("cls")
        set_tor_proxy_mod_menu()

def home():
    #The menu of choices
    print(f"""{Fore.CYAN}         
                                     ___                 ___       _             
                                    / _ \_ __ _____  __ /___\_ __ (_) ___  _ __  
                                   / /_)/ '__/ _ \ \/ ///  // '_ \| |/ _ \| '_ \{Fore.LIGHTBLUE_EX}
                                  / ___/| | | (_) >  </ \_//| | | | | (_) | | | |
                                  \/    |_|  \___/_/\_\___/ |_| |_|_|\___/|_| |_|""")
    print(f"""   
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.WHITE}
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ║                  [{Fore.CYAN}1{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Set Tor Proxy                                      {Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Disable Tor Proxy                     {Fore.WHITE} ║
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ║                  [{Fore.CYAN}3{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Credits                                            {Fore.WHITE}[{Fore.CYAN}4{Fore.WHITE}]{Fore.LIGHTBLUE_EX} Quit                                  {Fore.WHITE} ║
{Fore.WHITE} ║                                                                                                                   {Fore.WHITE} ║
{Fore.WHITE} ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
    choice = input(f'\r\n  {Fore.LIGHTBLUE_EX}[{Fore.CYAN}>{Fore.LIGHTBLUE_EX}] {Fore.WHITE}Choice : {Fore.CYAN}')
    if choice == "1":
        set_tor_proxy_mod_menu()
    elif choice == "2":
        disable_tor_proxy()
    elif choice == "3":
        credits()
    elif choice == "4":
        print(f"{Fore.LIGHTBLUE_EX}\r\nThank you for using our tool and see you soon !")
        sleep(2)
        exit()
    else:
        system("cls")
        home()

home()
