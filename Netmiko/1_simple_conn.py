#

from netmiko import Netmiko

net_connect = Netmiko(
    "10.223.244.86",
    username="DSV.API",
    password="bale-pE3WFx!",
    device_type="cisco_ios",
)

print(net_connect.find_prompt())
net_connect.disconnect()