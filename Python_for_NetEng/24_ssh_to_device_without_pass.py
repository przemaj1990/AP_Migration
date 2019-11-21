# ip ssh pubkey-chain
#   username admin1
#    key-hash ssh-rsa 83D9C8976CF994C80FFBCA704C9FCD90 shibi.v@ptpll359
# ssh-keygen -f admin1.pub -l
import datetime

TNOW = datetime.datetime.now().replace(microsecond=0)
IP_LIST = open('09_devices.txt')
for IP in IP_LIST:
    print ('\n'+ IP.strip() + ' \n' )
    RTR = {
    'ip':   IP,
    'username': 'admin1',
    'use_keys': True,
    'key_file': '/data/05_PYTHON_DEMO/SSH_KEY/admin1',
    'device_type': 'cisco_ios',
    }