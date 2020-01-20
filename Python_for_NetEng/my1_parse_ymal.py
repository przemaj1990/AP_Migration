import yaml
from pprint import pprint

tunnel_conf = ""

# with open("C:\Users\przemyslaw.majdanski\PycharmProjects\AP_Migration\instalation_file\tunnel_configuration_v1.1.yml", 'r') as yaml_file:
#     tunnel_conf = yaml.load(yaml_file)


stream = open("C:/Users/przemyslaw.majdanski/PycharmProjects/AP_Migration/instalation_file/tunnel_configuration_v1.1.yml", 'r')
# tunnel_conf = yaml.load(stream, Loader=yaml.Loader)
tunnel_conf = dict(yaml.load(stream, Loader=yaml.Loader))
for config in tunnel_conf['ARGS']:
    print(config['CONFIG']['LOCAL AS'])


# output_1 = ""
# for key, value in tunnel_conf.items():
#     output_1 += (key + " : " + str(value))
# pprint(output_1)