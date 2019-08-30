
from netmiko import Netmiko
from credentials import password1, username1
cisco1 = {
    "host": "10.223.44.102",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}


cfg_file = "change_file.txt"

net_connect = Netmiko(**cisco1)



print()
print(net_connect.find_prompt())
net_connect.send_config_from_file(cfg_file)
output = net_connect.send_command("sh run | i logging ")
print(output)
print()



# net_connect.save_config()
net_connect.disconnect()