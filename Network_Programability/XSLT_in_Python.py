

# <?xml version="1.0" encoding="UTF-8"?>
#
# <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
# <xsl:output indent="yes"/>
# <xsl:template match="/">
#   <html>
#   <body>
#   <h2>Authors</h2>
#     <table border="1">
#       <tr bgcolor="#9acd32">
# <th style="text-align:left">First Name</th>
#         <th style="text-align:left">Last Name</th>
#       </tr>
#       <xsl:for-each select="authors/author">
#       <tr>
#         <td><xsl:value-of select="firstName"/></td>
#         <td><xsl:value-of select="lastName"/></td>
#       </tr>
#       </xsl:for-each>
#     </table>
#   </body>
#   </html>
# </xsl:template>
# </xsl:stylesheet>


from lxml import etree
xslRoot = etree.fromstring(open("template.xsl").read())
transform = etree.XSLT(xslRoot)
xmlRoot = etree.fromstring(open("xmldata.xml").read())
transRoot = transform(xmlRoot)
print(etree.tostring(transRoot))

# <html><body><h2>Authors</h2><table border="1"><tr bgcolor="#9acd32">
# <th style="text-align:left">First Name</th><th style="text-align:left">Last Name
# </th></tr>
# <tr><td>Jason</td><td>Edelman</td></tr>
# <tr><td>Scott</td><td>Lowe</td></tr>
# <tr><td>Matt</td><td>Oswalt</td></tr></table></body></html>