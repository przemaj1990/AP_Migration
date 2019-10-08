import netmiko
from netmiko import ConnectHandler
from netmiko import BaseConnection
from Netmiko_project.credentails import password1, username1
# from ntc_templates.parse import parse_output
from netmiko.utilities import get_template_dir


cisco1 = {
    "ip": "10.223.2.100",
    "username": username1,
    "password": password1,
    "device_type": "cisco_wlc_ssh",
    'global_delay_factor': 4,
    'banner_timeout': 7
}

command = "show ap summary"

net_connect = ConnectHandler(**cisco1)
# net_connect.send_command("pma\n", strip_command=False, strip_prompt=False, expect_string="User:")
# net_connect.send_command_timing("Mugin2345!\n", strip_command=False, strip_prompt=False, delay_factor=1)
print(net_connect.find_prompt())
# new_output = net_connect.send_command(command, use_textfsm=True)
output = net_connect.send_command(command)
# new_output = parse_output(platform="cisco_wlc_ssh", command="ssh show ap summary", data=output)

# print(dir(output))
# print(dir(net_connect))
# print(new_output)

# print(get_template_dir.)



net_connect.disconnect()