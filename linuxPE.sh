#!/bin/bash

function userGRP(){
	echo -e "Finding the groups $USER belongs to: \n"
	id
}

function kernelINFO(){
	echo "finding the kernel version"
	uname -a
}

function suid(){
	echo -e "printing the 4000 suid of $HOSTNAME \n"
	echo "This is for GTFO"
	suidFind = find / -perm 04000 -ls 2>/dev/null
	$suidFIND
}

function enumerateShell(){
    userGRP
    kernelINFO
    suid
}
enumerateShell
