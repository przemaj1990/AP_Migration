import netmiko
from netmiko import ConnectHandler
from netmiko import BaseConnection

from .credentails import password1, username1

cisco1 = {
    "ip": "10.223.2.100",
    "username": username1,
    "password": password1,
    "device_type": "cisco_wlc",
    'global_delay_factor': 4,
    'banner_timeout': 15
}

net_connect = netmiko.Netmiko(**cisco1)
# print(net_connect.find_prompt())
# output = net_connect.send_command("show ip int brief")
# print(output)
# output = net_connect.send_command("show logging")
# print(output)

# net_connect = BaseConnection(**cisco1).special_login_handler(delay_factor=5)
# net_connect.special_login_handler(delay_factor=5)
print(net_connect.find_prompt())
net_connect.disconnect()

# output = net_connect.send_command("show ip int brief")
# print(output)
# output = net_connect.send_command("show logging")
# print(output)

