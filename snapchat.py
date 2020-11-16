import webbrowser
import requests
import pyfiglet
from colorama import Fore, init
import csv
init(autoreset=True)

banner = pyfiglet.figlet_format("SnapSearch")
print(Fore.YELLOW + banner)

def single_lookup():
    username = input("Enter a username: ")
    print()
    url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ".format(username)
    verify_snap = "https://snapchat.com/add/{}".format(username)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://accounts.snapchat.com/",
        "Cookie": "xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    }

    r = requests.post (url, headers=headers)
    data = r.json()


    status = data.get ("reference").get ("status_code")
    sugestions = data.get ("reference").get ("suggestions")

    if "TAKEN" in r.text:
        print(Fore.GREEN + "[-] " + Fore.WHITE + " اسم المستخدم محجوز")
        print()
        verify = input("هل تريد التحقق ؟ " + Fore.RED + "(y/n) " + Fore.WHITE)
        print()
        if verify == "y":
            webbrowser.open(verify_snap)
        else:
            exit()
    else:
        print (" [-] " + Fore.RED + " اسم المستخدم متوفر")

def csv_lookup():
    f = open("usersnap.csv")
    csv_f = csv.reader(f)

    for row in csv_f:
        row = "".join(row)
        url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ".format (row)
        verify_snap = "https://snapchat.com/add/{}".format (row)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://accounts.snapchat.com/",
            "Cookie": "xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }

        r = requests.post (url, headers=headers)
        data = r.json ()

        status = data.get ("reference").get ("status_code")
        sugestions = data.get ("reference").get ("suggestions")
        if "TAKEN" in r.text:
            print(Fore.BLUE + row + Fore.GREEN + " [-] " + Fore.WHITE + "اسم المستخدم محجوز")
        else:
            print(Fore.BLUE + row + Fore.RED + " [+] " + Fore.WHITE + "اسم المستخدم متوفر يمكنك اخذه")
    print()

print(Fore.YELLOW + "[1] " + Fore.WHITE + "Look up a single username")
print(Fore.YELLOW + "[2] " + Fore.WHITE + "Look up from csv")
print()
option = input("Select an option: ")
print()

if option == "1":
    single_lookup()
elif option == "2":
    csv_lookup()
