#!/bin/bash
process=$(ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | awk 'NR==4 {print $0}')
pid_port=($(ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | sed -n '4p'))
port=$(sudo netstat -alpn | grep $pid_port | awk '{print $4}' | awk -F ':' '{print $2}'|  awk 1 ORS=' ')

touch process_details.txt

echo "Process Name :  ${process[2]}" >process_details.txt
echo "% CPU  used :  ${process[5]}" >>process_details.txt
echo "% Memory used :  ${process[4]}" >>process_details.txt
echo "PORT :  ${port}" >>process_details.txt
echo "PID  :  ${process[1]}" >>process_details.txt
