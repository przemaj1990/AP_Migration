import paramiko
import time
from getpass import getpass
import datetime

TNOW = datetime.datetime.now().replace(microsecond=0)

username = 'lab'
password = 'cisco123'


DEVICE_LIST = open('09_devices.txt')
for RTR in DEVICE_LIST:
    RTR = RTR.strip()
    print ('\n #### Connecting to the device ' + RTR.strip() + ' ####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR.strip(),port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'terminal len 0\n')
    DEVICE_ACCESS.send(b'show run\n')

    time.sleep(5)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))
    SAVE_FILE = open('ROUTER_' + RTR , 'w')
    SAVE_FILE.write(output.decode('ascii'))
    SAVE_FILE.close

    SESSION.close

# methods and attributes of the object
name1 = '  test1   '
name2 = 'test2'
dir(name1)

# strip() is a method

print (name1.lstrip()+name2)

help(str)
help-str

# strip() is a method
# help()- topics
      # -STRINGS ,STRINGSMETHODS

print (name2.upper())
print (name1.upper().lstrip())
# capitalize(),upper()