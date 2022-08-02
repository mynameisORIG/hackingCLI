#! /usr/bin/python3
from lib.dicPorts import *
from lib.arguments import argNmap
from lib.nmapifelse import *
import nmap
import subprocess

nmap = nmap.PortScanner()

argNmap()

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
            from lib.dictionary1 import wordlist
            print(f'Running gobuster on port {ports}\n')
            subprocess.run(['gobuster', 'dir', '-u', f'http://{argNmap.args.ip}:{ports}', '-w', wordlist['gobuster'], '-t', '50', '>', f'files/gobuster/{argNmap.args.ip}{ports}.nmap'])
        #print(nmap[argNmap.args.ip]['tcp'][ports]['name'])
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'ftp':
            print('still working on ftp\n')
            #ftp21IfElse()
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