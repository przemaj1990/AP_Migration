#

from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "host": "10.223.244.86",
    "username": "DSV.API",
    "password": "bale-pE3WFx!",
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
print(net_connect.find_prompt())
# output = net_connect.send_command("show ip int brief")
# print(output)
# output = net_connect.send_command("show logging")
# print(output)

net_connect.disconnect()
