import paramiko
import time
from getpass import getpass


username = 'admin'
password = 'admin'

DEVICE_LIST = open ('09_devices')
for RTR in DEVICE_LIST:
    print ('\n #### Connecting to the device ' + RTR.strip() + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    COMMANDS = open ('09_config')
    for LINES in COMMANDS:
        time.sleep(1)
        DEVICE_ACCESS.send(str(LINES))

    time.sleep(3)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))

    SESSION.close
