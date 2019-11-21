from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import time
import datetime
import schedule

def BACKUP():
    TNOW = datetime.datetime.now().date()
    IP_LIST = open('09_devices.txt')
    for IP in IP_LIST:
        RTR = {
            'ip': IP,
            'username': 'lab',
            'password': 'cisco123',
            'device_type': 'cisco_ios',
        }

        print ('\n Connecting to the device ' + IP.strip() + ' \n')
        try:
            net_connect = ConnectHandler(**RTR)
        except NetMikoTimeoutException:
            print ('Device not reachable' )
            continue

        except NetMikoAuthenticationException:
            print ('Authentication Failure' )
            continue

        except SSHException:
            print ('Make sure SSH is enabled' )
            continue

        print('Initiating config backup at ' + str(TNOW))
        output = net_connect.send_command('show run')
        SAVE_FILE = open('ROUTER_' + IP + str(TNOW), 'w')
        SAVE_FILE.write(output)
        SAVE_FILE.close
        print('Finished config backup')

schedule.every().minute.at(":00").do(BACKUP)
while True:
    schedule.run_pending()
    time.sleep(1)