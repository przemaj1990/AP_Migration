
from netmiko import Netmiko
from Netmiko_project.credentails import password1, username1
cisco1 = {
    "host": "10.223.44.102",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}

# I was forced to use my own TACACS credentials to make this work

commands = ["logging history size 500"]

net_connect = Netmiko(**cisco1)

print(net_connect.find_prompt())
net_connect.send_config_set("conf t")
net_connect.send_config_set(commands)
output = net_connect.send_command("sh run | i logging ")
net_connect.disconnect()

print(output)


