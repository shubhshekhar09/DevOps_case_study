#!/bin/python3
import cmd
import getpass
from http import client
from sys import stderr, stdin, stdout
import paramiko
host_file = open('hostfile','r')
hostnames = host_file.readlines()

port = 22

try:
    while True:
        try:
            cmd = input(">")
            if cmd == 'exit': break
            for node in hostnames:
                user = input('Enter Username for the ' + node + ':')
                passwd = getpass.getpass('Enter the Password for the ' + node + ':')                
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
                client.connect(node.strip(), port=port, username=user, password=passwd )
                stdin, stdout, stderr = client.exec_command(cmd)
                exit_status = stdout.channel.recv_exit_status() 
                if exit_status == 0:
                    print("Command has executed on host" + node + ": " + cmd)
                    print(stdout.read().decode())
                    print("Done")
                else:
                    print("Error",exit_status)
                    print(stderr.read().decode())
                client.close() 
        except KeyboardInterrupt:
            break   
except Exception as err:
    print(str(err))
