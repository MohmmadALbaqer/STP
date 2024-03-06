import sys
import os
import time
import speedtest
import requests
from time import sleep
from tqdm import tqdm
from colorama import Fore, Style, init
from termcolor import colored

def clear_screen():
    operating_system = os.name

    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"An error occurred: {e}")
clear_screen()

def spin():
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    for _ in range(1):
        for i in spinner:
            message = f"[*] {Fore.BLUE}Checking your internet connection...[{i}]{Style.RESET_ALL}"
            colored_message = colored(message, 'blue', attrs=['bold'])
            sys.stdout.write(f"\r{colored_message}   ")
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write("\r")
    sys.stdout.flush()
    done_message = colored("[+] Your Internet connection has been verified", 'yellow', attrs=['bold'])
    sys.stdout.write("\033[K") 
    print(done_message)
    time.sleep(1)

spin()

def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

if check_internet_connection():
    print(f"{Fore.GREEN}[*] Internet connection is available. You can proceed with execution.{Style.RESET_ALL}")
    time.sleep(0.25)

else:
    print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.RED} No internet connection !{Style.RESET_ALL}")
    exit()
    
def clear_screen():
    operating_system = os.name

    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"An error occurred: {e}")
clear_screen()

print(f"""{Fore.BLUE}
  ____________________________ 
 /   _____/__    ___/______   \\
 \_____  \  |    |   |     ___/
 /        \ |    |   |    |    
/_______  / |____|   |____|  {Fore.GREEN}Version : 3{Fore.BLUE}
        \/ {Style.RESET_ALL}""")
print(f'''
{Fore.RED}+------------------------------------------------------------------+
{Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
{Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.comr94xs/        {Fore.RED}|
{Fore.RED}+------------------------------------------------------------------+{Style.RESET_ALL}''')

init(autoreset=True)
print(f"{Fore.GREEN}[*] GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED.....{Style.RESET_ALL}")

st = speedtest.Speedtest()
st.get_best_server()

for _ in tqdm(range(10), colour="green", desc="Finding Optimal Server"):
    sleep(0.05)

st.download()
for _ in tqdm(range(10), colour="yellow", desc="Getting Download Speed"):
    sleep(0.05)

st.upload()
for _ in tqdm(range(10), colour="red", desc="Getting Upload Speed"):
    sleep(0.05)

res_dict = st.results.dict()

dwnl = f"{res_dict['download'] / 10**6:.2f}"
upl = f"{res_dict['upload'] / 10**6:.2f}"

print("")
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.BLUE}Internet test information{Style.RESET_ALL}")
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.YELLOW}Download:{Fore.BLUE} {dwnl} Mbps ({float(dwnl) * 0.125:.2f} MB/s) ")
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.YELLOW}Upload:{Fore.BLUE} {upl} Mbps ({float(dwnl) * 0.125:.2f} MB/s)")  
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.YELLOW}Ping:{Fore.BLUE} {res_dict['ping']:.2f} ms")
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.YELLOW}HOST:{Fore.BLUE} {res_dict['server']['host']}") 
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.YELLOW}SPONSOR:{Fore.BLUE} {res_dict['server']['sponsor']}")  
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.YELLOW}LATENCY:{Fore.BLUE} {res_dict['server']['latency']:.2f} ms")
