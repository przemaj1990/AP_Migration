from telnetlib import Telnet
cmd = 'show ip int b'
cmd2 = raw_input('Enter Config: ')
t = Telnet(''10.1.1.1')
t.write('pma\n')
t.write('Mugin2345!\n')
t.write('show version\n')
t.write(cmd + '\n')
t.write(cmd2 + '\n')


print(t.read_all)

# for 3.6
t.write(b'something\n')
t.write(cmd.encode('ascii') + n'\n')
print(t.read_all().decode('ascii'))