#

#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

# Not working as our devices are using TACACS+

from credentials import password1, username1
cisco1 = {
    "host": "10.223.244.86",
    "username": username1,
    "password": password1,
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