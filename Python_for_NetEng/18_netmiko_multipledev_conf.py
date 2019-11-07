from netmiko import ConnectHandler

RTR_10 = {
    'ip':   '10.10.10.10',
    'username': 'admin',
    'password': 'admin',
    'device_type': 'cisco_ios',
}

RTR_11 = {
    'ip':   '10.10.10.11',
    'username': 'admin',
    'password': 'admin',
    'device_type': 'cisco_ios',
}

DEVICE_LIST = [RTR_10, RTR_11]
for DEVICE in DEVICE_LIST:
    print ('Connecting to the Device ' + DEVICE['ip'])
    net_connect = ConnectHandler(**DEVICE)

    config_commands = [ 'int lo0',
                        'ip add 1.1.1.1 255.255.255.0',
                        'no shut' ]
    output = net_connect.send_config_set(config_commands)
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)