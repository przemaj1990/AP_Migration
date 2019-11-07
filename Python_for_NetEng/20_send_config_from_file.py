from netmiko import Netmiko

IP_LIST = open('09_devices')
for IP in IP_LIST:
    print ('\n ##### '+ IP.strip() + ' ##### \n' )
    RTR = {
    'ip':   IP,
    'username': 'admin',
    'password': 'admin',
    'device_type': 'cisco_ios',
    }

    net_connect = Netmiko(**RTR)

    output = net_connect.send_config_from_file(config_file = '16_config')
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)