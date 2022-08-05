#! /usr/bin/python3
#from lib.enum.arguments import argNmap
import nmap
import subprocess

nmap = nmap.PortScanner()

class argNmap():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", type=str, required=True, help="IP or hostname you wish to scan")
    args = parser.parse_args()
#argNmap()

def nmapPreReq():
    global victimPortsList
    victimPortsList = []

    global victim
    victim = nmap.scan(argNmap.args.ip, 
        arguments="-sC -sV -T4 -Pn -p-")
def nmapifElsePorts():
    victimPortsList = list(nmap[argNmap.args.ip]['tcp'].keys())
    for ports in victimPortsList:
        # gobuster's any http sites
        if nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'http':
            from lib.enum.dictionary1 import wordlist
            print(f'Running gobuster on port {ports}\n')
            subprocess.run(['gobuster', 'dir', '-u', f'http://{argNmap.args.ip}:{ports}', '-w', wordlist['gobuster'], '-t', '50', '>', f'files/gobuster/{argNmap.args.ip}{ports}.nmap'])
            subprocess.run(['nikto', '-h', f'{argNmap.args.ip}:{ports}'])
        #print(nmap[argNmap.args.ip]['tcp'][ports]['name'])
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'ftp':
            print('still working on ftp\n')
            from ftplib import FTP
            with FTP(argNmap.args.ip) as ftp:
                # this logins as anonymous with password anonymous
                ftp.login(user='anonymous', passwd='anonymous')
                try:
                    ftp.dir()
                except FTP.error_perm as resp:
                    if str(resp) == "530 Permission denied":
                        pass
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'smbd' or 'netbios-ssn':
            print(f'Running smbclient on port {ports}\n')
            subprocess.run(['smbclient', '-NL', f'//{argNmap.args.ip}', '-R'])
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'telnet':
            print('do something with telnet') 


def main():
    nmapPreReq()
    nmapifElsePorts()

if __name__ == '__main__':
    main()