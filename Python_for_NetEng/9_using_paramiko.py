import paramiko
import time
from pprint import pprint
from time import sleep

# pprint(dir(paramiko))
# pprint(help(paramiko))

router = {"ip": "10.48.93.10",
          "port": "443",
          "user": "lab ",
          "pass": "cisco123"}
ip = "10.48.93.10"

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(ip, port=22, username="lab", password="cisco123", look_for_keys=False, allow_agent=False)
dev = session.invoke_shell()
dev.send(b'term length 0\n')
dev.send(b'show version')
time.sleep(20)
output = dev.recv(6500)
print(output)
print(output.decode('ascii'))

# session.send(b'config t\n')
# for N in range (a,b):
#     session.send('no int lo ' +str(N) + '\n')
#    DEVICE_ACCESS.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')

time.sleep(3)
session.send(b'do term length 0\n')
session.send(b'do show ip int brief\n')
time.sleep(3)
output = session.recv(65000)
print(output.decode('ascii'))

session.close
