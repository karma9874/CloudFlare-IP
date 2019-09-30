import sys
import requests
import base64
from shodan import Shodan
from shodan.cli.helpers import get_api_key
from colorama import Fore, Style
import time
import mmh3
from datetime import datetime
import socket

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def get_hash(url,ssl=False):
    response = requests.get(url,verify=ssl).content
    b64 = base64.encodebytes(response).decode()
    fav_hash = mmh3.hash(b64)
    return fav_hash

def shodan_search(fav_hash):
    ip=None
    shodan = Shodan(get_api_key())
    try:
        search = shodan.search(f"http.favicon.hash:{fav_hash}")
        for result in search["matches"]:
            ip=result['ip_str']
    except:
        print("Shodan Search Error")
    return ip


url = sys.argv[1]


hostname_url = url.split("//")[-1].split("/")[0].split('?')[0]

print("\n")
print(Fore.GREEN+"    Starting"+Fore.RESET)
logo = r"""
    __  _       ___   __ __  ___    _____  _       ____  ____     ___       ____  ____  
   /  ]| |     /   \ |  |  ||   \  |     || |     /    ||    \   /  _]     |    ||    \ 
  /  / | |    |     ||  |  ||    \ |   __|| |    |  o  ||  D  ) /  [_ _____ |  | |  o  )
 /  /  | |___ |  O  ||  |  ||  D  ||  |_  | |___ |     ||    / |    _]     ||  | |   _/ 
/   \_ |     ||     ||  :  ||     ||   _] |     ||  _  ||    \ |   [_|_____||  | |  |   
\     ||     ||     ||     ||     ||  |   |     ||  |  ||  .  \|     |      |  | |  |   
 \____||_____| \___/  \__,_||_____||__|   |_____||__|__||__|\_||_____|     |____||__|   
                              
                                                                                        """                                                     

print(Fore.RED+logo+Fore.RESET)
print(Fore.GREEN+"Initializing CloudFlare-IP -  " + dt_string+Fore.RESET+"\n")
time.sleep(2)
try:
	if sys.argv[2]:
		ssl_check = sys.argv[2]
		new_hash = get_hash(url,ssl_check)
except:
	hash_collected = get_hash(url)


print(Fore.GREEN+"Finding Origin Ip of "+url+Fore.RESET+"\n");

print(Fore.GREEN+"Searching Favicon Hash on Shodan "+Fore.RESET+"\n");

result_ip = shodan_search(hash_collected)

print(Fore.GREEN+"The DNS IP is : " +Fore.RED+str(socket.gethostbyname(hostname_url))+"\n")
print(Fore.GREEN+"The Real IP is : " +Fore.RED+str(result_ip)+"\n")

print(Fore.GREEN+"Exiting...Bye")



