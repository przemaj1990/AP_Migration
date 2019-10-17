import paramiko
import time
from getpass import getpass
from pprint import pprint



username = 'admin'
password = 'admin'

DEVICE_LIST =['10.10.10.' + str(n) for n in range(10,12)]
for RTR in DEVICE_LIST:
    print ('\n #### Connecting to the device ' + RTR + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'config t\n')
    for N in range (2,5):
        DEVICE_ACCESS.send('int lo ' +str(N) + '\n')
        DEVICE_ACCESS.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')

    time.sleep(3)
    DEVICE_ACCESS.send(b'do term length 0\n')
    DEVICE_ACCESS.send(b'do show ip int brief\n')
    time.sleep(3)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))
    SESSION.close


DEVICE_LIST = ['10.10.10.10','10.10.10.11']
for RTR in DEVICE_LIST:
    print (RTR)

DEVICE_LIST = ['10.10.10.'+ str(n) for n in range(10,15)]
for RTR in DEVICE_LIST:
    print (RTR)

# python  help() -  topics
# help  SEQUENCES
# - LISTS

# interface = ['Gi'+str(n) for n in range(2,5)] list comprehension
# Indexing
# DEVICE_LIST = ['10.10.10.10','10.10.10.11','R1']
# print (DEVICE_LIST[0])
# some of the operations
#  type(devices)
# dir(devices)
# devices.append('SW4')
# DEVICE_LIST = ['10.10.10.10','10.10.10.11']
# DEVICE_LIST = ['10.10.10.'+ str(n) for n in range(10,15)]
#
# for RTR in DEVICE_LIST:
#     ip = "10.10.10." + str(n)