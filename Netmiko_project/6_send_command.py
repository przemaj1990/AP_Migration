#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
from credentials import password1, username1
cisco1 = {
    "host": "10.223.244.86",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
command = "show ip int brief"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()