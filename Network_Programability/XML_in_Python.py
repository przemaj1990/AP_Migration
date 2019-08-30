# ~$ pyxbgen -u schema.xsd -m schema

# <?xml version="1.0" encoding="utf-8"?>
# <xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/
# XMLSchema">
#   <xs:element name="device">
#   <xs:complexType>
#     <xs:sequence>
#       <xs:element name="vendor" type="xs:string"/>
#       <xs:element name="model" type="xs:string"/>
#       <xs:element name="osver" type="xs:string"/>
#     </xs:sequence>
#   </xs:complexType>
# </xs:element>
# </xs:schema>


import schema
dev = schema.device()
dev.vendor = "Cisco"
dev.model = "Nexus"
dev.osver = "6.1"
dev.toxml("utf-8")

# '<?xml version="1.0" encoding="utf-8"?><device><vendor>Cisco</vendor><model>Nexus
# </model><osver>6.1</osver></device>'