#!/bin/bash

function enumerateShell(){
    echo "finding the user's permssions"
    id
    echo "finding kernel version"
    uname -a
    # prints all files in root that have a suid of 4000 
    echo "printing the 4000 suid of $HOSTNAME"
    suidFind= find / -perm -4000 2>/dev/null
    $suidFind
    
}
enumerateShell