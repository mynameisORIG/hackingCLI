echo "User Privileges"
whoami /priv 
echo "User Group Privileges"
whoami /groups
echo "See local users"
net user
echo "Attempting to find passwords in txt files in the current directory"
findstr /si password *.txt
