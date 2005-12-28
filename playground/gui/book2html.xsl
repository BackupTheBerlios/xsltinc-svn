<?xml version="1.0" encoding="UTF-8"?> <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"> 
<xsl:template match="/">
  <html>
  <body>
      <xsl:apply-templates/>
  </body>
  </html>
</xsl:template>


<xsl:template match="book">
   <h1><xsl:value-of select="titre"/></h1>
      <xsl:apply-templates/>
</xsl:template>


<xsl:template match="authors">
   <h2>Auteurs</h2>
  <ul><xsl:apply-templates select="person"/></ul>
</xsl:template>

<xsl:template match="person">
  <li><xsl:value-of select="firstname"/><xsl:text>~</xsl:text><xsl:value-of select="lastname"/></li>
</xsl:template>

<xsl:template match="section">
  <div>
     <h3><xsl:value-of select="title"/></h3>
     <p>
       <xsl:value-of select="para"/>
     </p>
  </div>
</xsl:template>

<xsl:template match="titre">
</xsl:template>

</xsl:stylesheet>
