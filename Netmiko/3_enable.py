#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

password = getpass()

cisco1 = {
    "host": "10.223.244.86",
    "username": "DSV.API",
    "password": "bale-pE3WFx!",
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
print(net_connect.find_prompt())
net_connect.send_command("disable")
print(net_connect.find_prompt())
net_connect.enable()
print(net_connect.find_prompt())

# Go into config mode
# net_connect.config_mode()
# print(net_connect.find_prompt())
# net_connect.exit_config_mode()
# print(net_connect.find_prompt())
net_connect.disconnect()