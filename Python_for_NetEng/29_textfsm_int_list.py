from netmiko import ConnectHandler
from operator import itemgetter

RTR = {
            'ip': '10.48.93.10',
            'username': 'lab',
            'password': 'cisco123',
            'device_type': 'cisco_ios',
        }

net_connect = ConnectHandler(**RTR)

output = net_connect.send_command('show ip int brief', use_textfsm=True)

l = len(output)
print ('\nList of interfaces which are UP \n')
for i in range(0,l):
    if output[i]['status'] == 'up':
        print (output[i]['intf'] +' ' + output[i]['status'])

print ('\nList of interfaces which are DOWN \n')
for i in range(0,l):
    if output[i]['status'] != 'up':
        print (output[i]['intf'] +' ' + output[i]['status'])