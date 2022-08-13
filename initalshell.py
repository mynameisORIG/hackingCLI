#!/usr/bin/python3

class argNmap():
    import argparse
    parser = argparse.ArgumentParser()
    # gbf is the gobuster file
    parser.add_argument("-gbf", type=str, required=True, help="gobuster file you might be able to do more with")
    args = parser.parse_args()

def phpinfo():
    import mmap
    gobusterFileRead = open(rgNmap.args.gbf, "r+")
    with open(gobusterFileRead) as gobusFile, \
        mmap.mmap(gobusFile.fileno(), 0, access=mmap.ACCESS_READ) as phpinfostring:
        if phpinfostring.find(b'phpinfo.php') != -1:
            PHPInfoFileUpload = input('Would you like to exploit phpinfo.php? (Y/N): ')
        if PHPInfoFileUpload == 'Y':
            print('figure out how to see if file_upload is on')