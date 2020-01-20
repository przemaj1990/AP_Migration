
from napalm import get_network_driver
from pprint import pprint


driver = get_network_driver('ios')
device = driver('10.48.93.10', 'lab', 'cisco123')
device.open()

device.load_merge_candidate(filename="ROUTER- 10.48.93.10-2019-11-07")
pprint(device.compare_config())

# if len(device.compare_config()) >  0:
#     choice = input("Would you like to commit these changes? [yN]: ")
#     if choice == 'y':
#         print('Committing ...')
#         device.commit_config()
#     else:
#         print('Discarding ...')
#         device.discard_config()
# else:
#     print ('No difference')
#
# device.close()
print('Done.')