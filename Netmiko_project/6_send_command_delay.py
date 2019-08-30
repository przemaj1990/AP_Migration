#!/usr/bin/env python
# Not used - example of how to deplay
#


from netmiko import Netmiko
from credentials import password1, username1
cisco1 = {
    "host": "10.223.244.86",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
command = "copy flash:c880data-universalk9-mz.154-2.T1.bin flash:test1.bin"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command, delay_factor=4)
print(output)
print()