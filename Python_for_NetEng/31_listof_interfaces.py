from pprint import pprint

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



devlist = []
for i in output:
    if i['status'] == 'up':
        devlist.append(i['intf'])
pprint(devlist)

print([i for i in output if i['status'] == 'up'])
print([i['intf'] for i in output if i['status'] == 'up'])

print('\n \n')

print('\nList of interfaces which are UP \n')
statusup = [i['intf'] for i in output if i['status'] == 'up']

for ifaceup in statusup:
    print (ifaceup)

print ('\nList of interfaces which are DOWN \n')
statusother =[i for i in output if i['status'] != 'up']
for ifaceother in statusother:
    print (ifaceother['intf'] + ' ' + ifaceother['status']  )