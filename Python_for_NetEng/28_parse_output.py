# pip list
# git clone
# export NET_TEXTFSM=/git/ntc-templates/templates/
from pprint import pprint

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

# pprint(output)
# pprint(output['GigabitEthernet0/0/1'])

print(output[3])

l = len(output)
print ('\nTotal number of interfaces are ' + str(l))

name = output[1]['intf']
status = output[1]['status']
print ('\nInterface ' + name + ' status is ' + status )

interface0 = output[1]
getint = itemgetter('intf')
getstatus =  itemgetter('status')
name = getint(interface0)
status = getstatus(interface0)
print ('\nInterface ' + name + ' status is ' + status )