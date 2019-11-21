from netmiko import ConnectHandler
from operator import itemgetter

RTR = {
            'ip': '10.48.93.10',
            'username': 'lab',
            'password': 'cisco123',
            'device_type': 'cisco_ios',
        }

print ('Checking interface status..')
net_connect = ConnectHandler(**RTR)

output = net_connect.send_command('show ip int brie', use_textfsm=True)
print(output)
# Fetch data from dict and print
name = output[1]['intf']
status = output[1]['status']
print ('\nInterface ' + name + ' status is ' + status )

if status == 'up':
    print ('Finishing the script')
else :
    print ('making backup interface UP')
    # config_commands = [ 'int fa0/1',
    #                     'no shut' ]
    # output = net_connect.send_config_set(config_commands)
    # print (output)
    print ('Finished configuration')