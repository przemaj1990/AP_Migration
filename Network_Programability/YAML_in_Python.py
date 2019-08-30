# Working with YAML in Python
# use module pyyaml
import yaml
with open("example.yml") as f:
    result = yaml.load(f)
    print(result)
    type(result)

# in example.ye:
# {'Brocade': True, 'Cisco': 6500, 'Juniper': 'Also a plant',
# 'VMware': ['esxi', 'vcenter', 'nsx']}
# <type 'dict'>
