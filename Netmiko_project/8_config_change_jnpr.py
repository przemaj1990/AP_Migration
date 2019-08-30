#!/usr/bin/env python

from netmiko import Netmiko
from credentials import password1, username1
cisco1 = {
    "host": "10.223.44.102",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}

commands = ["logging history size 500"]

net_connect = Netmiko(**cisco1)

print()
print(net_connect.find_prompt())
net_connect.send_config_set("conf t")
output = net_connect.send_config_set(commands, exit_config_mode=False)
print(output)
# I was no able to use "and_quite"
output = net_connect.commit(and_quit=True)
print(output)
output = net_connect.send_command("sh run | i logging ")
print(output)

net_connect.disconnect()