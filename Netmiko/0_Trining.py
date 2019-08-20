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
print(net_connect.find_prompt())
# output = net_connect.send_command("show ip int brief")
# print(output)
# output = net_connect.send_command("show logging")
# print(output)

net_connect.disconnect()
