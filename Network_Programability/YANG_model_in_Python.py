


# leaf hostname {
#     type string;
#     mandatory true;
#     config true;
#     description "Hostname for the network device";
# }

# <vlans>
#   <vlan>
#       <id>100</id>
#       <name>web_vlan></name>
#   </vlan>
#   <vlan>
#       <id>200</id>
#       <name>app_vlan></name>
#   </vlan>
# </vlans>
# {
#     "vlans": {
#         "vlan": [
#             {
#                 "id": "100",
#                 "name": "web_vlan"
#             },
#             {
#                 "id": "200",
#                 "name": "app_vlan"
#             }
#         ]
#     }
# }