from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import datetime

TNOW = str(datetime.datetime.now().date())

IP_LIST = open('09_devices.txt')
for IP in IP_LIST:
    print ('\n  '+ IP.strip() + ' \n' )
    RTR = {
    'ip':   IP,
    'username': 'lab',
    'password': 'cisco123',
    'device_type': 'cisco_ios',
    }
    try:
        net_connect = ConnectHandler(**RTR)
    except NetMikoTimeoutException:
        print ('Device not reachable.')
        continue
    except AuthenticationException:
        print ('Authentication Failure.')
        continue
    except SSHException:
        print ('Make sure SSH is enabled in device.')
        continue

    print ('Initiating cofig backup')
    output = net_connect.send_command('show run')

    SAVE_FILE = open('ROUTER-' + RTR['ip'] + "-" + TNOW, 'w')
    SAVE_FILE.write(output)
    SAVE_FILE.close
    print ('Finished config backup')