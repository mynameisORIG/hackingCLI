#!/usr/bin/python3
from lib.arguments import argNmap

def httpIfElse():
    from lib.dictionary1 import wordlist
    import subprocess

    print(f'Running gobuster on port {ports}\n')
    subprocess.run(['gobuster', 'dir', '-u', f'http://{argNmap.args.ip}:{ports}', '-w', wordlist['gobuster'], '-t', '50', '>', f'files/gobuster/{argNmap.args.ip}{ports}.nmap'])

def ftp21IfElse():
    from ftplib import FTP
    with FTP(argNmap.args.ip) as ftp:
        # this logins as anonymous with password anonymous
        ftp.login(user='anonymous', passwd='anonymous')
        try:
            ftp.dir()
        except FTP.error_perm as resp:
            if str(resp) == "530 Permission denied":
                pass

def smb445IfElse():
    import subprocess
    subprocess.run(['smbclient', '-NL', f'//{argNmap.args.ip}', '-R'])