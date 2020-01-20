from netmiko import ConnectHandler
from operator import itemgetter
ip = input('Enter the IP: ')
RTR = {
            'ip': '10.48.93.10',
            'username': 'lab',
            'password': 'cisco123',
            'device_type': 'cisco_ios',
        }
print ('Connecting to the device..')
net_connect = ConnectHandler(**RTR)

output = net_connect.send_command('show ip int brie', use_textfsm=True)

print ('\nSearch result \n')



ipsearch =[i['intf'] for i in output if i['ipaddr'] == ip]
for ipoutput in ipsearch:
    print ('IP Address ' + ip + ' belongs to interface ' + ipoutput )
print ('IP Address ' + ip + ' belongs to interface ' + str(ipsearch) )