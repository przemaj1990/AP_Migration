#

#!/usr/bin/env python

from netmiko import Netmiko
from credentials import password1, username1

cisco1 = {
    "host": "10.223.252.122",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}

cisco2 = {
    "host": "10.223.148.202",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}


for device in (cisco1, cisco2):
    net_connect = Netmiko(**device)
    print(net_connect.find_prompt())