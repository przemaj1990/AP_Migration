
# Introduction to Netmiko.
# Simplifies SSH to the networking device
# Simplifies execution of show command as well as configuration in to the device
#
# textfsm:can extract the date from output and give it in a structured way.
# Installation Command:
# pip install netmiko
#
# Netmiko commonly-used methods:
# net_connect.send_command() - Send command down the channel, return output back (pattern based)
# net_connect.send_command_timing() - Send command down the channel, return output back (timing based)
# net_connect.send_config_set() - Send configuration commands to remote device
# net_connect.send_config_from_file() - Send configuration commands loaded from a file
# net_connect.save_config() - Save the running-config to the startup-config
# net_connect.enable() - Enter enable mode
#
# need to import the ConnectHandler function from Netmiko.
# then define a network device dictionary which contains device_type, ip, username, and password.
# verbose in for detailed logging.
# Dictionaries:
# will have mapping between key and value
# Order is not mandatory here
# Script sample:

from netmiko import ConnectHandler
from netmiko import Netmiko
from getpass import getpass
password = getpass()
RTR_10 = {
    'ip':   "10.48.93.10",
    'username': 'lab',
    'password': 'cisco123',
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**RTR_10)

# config_commands = [ 'int lo0',
#                     'ip add 1.1.1.1 255.255.255.0',
#                     'no shut' ]
# output = net_connect.send_config_set(config_commands)
# print(output)

output = net_connect.send_command('show ip int brief')
print(output)