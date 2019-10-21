import paramiko
import time
from getpass import getpass
import datetime

TNOW = datetime.datetime.now().replace(microsecond=0)

username = 'lab'
password = 'cisco123'
scp_pass = getpass( prompt = 'Enter SCP server Password :')

DEVICE_LIST = open ('09_devices')
for RTR in DEVICE_LIST:
    RTR = RTR.strip()
    print ('\n #### Connecting to the device ' + RTR + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send('copy nvram:startup-config scp://user@10.10.10.100//data/05_PYTHON_DEMO/ROUTER_' + RTR + '\n\n\n\n')
    time.sleep(5)
    DEVICE_ACCESS.send(scp_pass +'\n')
    time.sleep(1)
    print ('Backup completed for the device ' + RTR + '\n\n')

    SESSION.close