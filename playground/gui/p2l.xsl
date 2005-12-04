<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
    <h1>Person List</h1>
      <xsl:apply-templates/>
  </body>
  </html>
</xsl:template>

<xsl:template match="persons">
  <ul><xsl:apply-templates select="person"/></ul>
</xsl:template>

<xsl:template match="person">
  <li><xsl:value-of select="firstname"/> <xsl:value-of select="lastname"/></li>
</xsl:template>

</xsl:stylesheet>