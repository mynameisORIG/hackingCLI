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
        arguments=f"-sC -sV -T4 -Pn -p- -oN files/nmap/{argNmap.args.ip}.nmap")
def nmapifElsePorts():
    import mmap
    victimPortsList = list(nmap[argNmap.args.ip]['tcp'].keys())
    for ports in victimPortsList:
        #print(nmap[argNmap.args.ip]['tcp'][ports]['name'])
        # gobuster's any http sites
        if nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'http':
            from lib.enum.dictionary1 import wordlist
            print(f'Running gobuster on port {ports}\n')
            gobusterFile = f'files/gobuster/{argNmap.args.ip}-{ports}.gbuster'
            gobuster = subprocess.run(['gobuster', 'dir', '-u', f'http://{argNmap.args.ip}:{ports}', '-w', wordlist['gobuster'], '-t', '50', '-o', gobusterFile])
            nikto = subprocess.run(['nikto', '-h', f'{argNmap.args.ip}:{ports}'])
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'ftp':
            # print('still working on ftp\n')
            from ftplib import FTP
            ftp = FTP(argNmap.args.ip)
            # this logins as anonymous with password anonymous
            ftp.login(user='anonymous', passwd='anonymous')
            ftp.retrlines('LIST')
            # try:
            #     ftp.dir()
            # except FTP.error_perm as resp:
            #     if str(resp) == "530 Permission denied":
            #         pass
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'mountd':
            showmount = subprocess.run(['showmount', '-e', f'{argNmap.args.ip}'], stdout=subprocess.PIPE)
            if showmount.stdout == f'Export list for {argNmap.args.ip}':
                subprocess.run(['mount',
                                '-t',
                                'nfs', 
                                f'{argNmap.args.ip}:{showmount.stdout[31:40]}, /mnt'], stdout=subprocess.PIPE)
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'domain':
            subprocess.run(['dnsrecon', 
                            '-r', 
                            '127.0.0.0/24', 
                            '-n',
                            f'{argNmap.args.ip}',
                            '-d', 
                            'blah'])
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'smbd' or 'netbios-ssn':
            print(f'Running smbclient on port {ports}\n')
            subprocess.run(['smbclient', 
                            '-NL', 
                            f'//{argNmap.args.ip}',
                            '-R'])
        elif nmap[argNmap.args.ip]['tcp'][ports]['name'] == 'telnet':
            print('do something with telnet')



def main():
    nmapPreReq()
    nmapifElsePorts()

if __name__ == '__main__':
    main()