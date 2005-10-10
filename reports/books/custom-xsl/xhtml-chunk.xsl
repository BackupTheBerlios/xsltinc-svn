<?xml version='1.0' encoding='utf-8' ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:import href="../docbook-xsl/xhtml/chunk.xsl"/>

  <xsl:include href="common.xsl"/>
  <xsl:include href="xhtml-common.xsl"/>

  <xsl:param name="base.dir">output/xhtml-chunk/</xsl:param>

  <xsl:param name="chunk.section.depth">0</xsl:param>

  <xsl:param name="chunker.output.encoding">iso-8859-1</xsl:param>
  <xsl:param name="chunker.output.indent">yes</xsl:param>
</xsl:stylesheet>