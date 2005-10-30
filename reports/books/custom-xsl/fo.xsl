<?xml version='1.0' encoding='utf-8' ?>
<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:fo="http://www.w3.org/1999/XSL/Format"
  version="1.0">

  <xsl:import href="../docbook-xsl/fo/docbook.xsl"/>
  <xsl:include href="common.xsl"/>
  <xsl:include href="titlepage.xsl"/>

  <xsl:param name="paper.type">A4</xsl:param>

	<xsl:param name="page.margin.top" select="'1.5cm'"/>		
	<xsl:param name="region.before.extent" select="'1cm'"/>
	<xsl:param name="body.margin.top" select="'1cm'"/>
	
	<xsl:param name="page.margin.bottom" select="'1.5cm'"/>
	<xsl:param name="region.after.extent" select="'1cm'"/>
	<xsl:param name="body.margin.bottom" select="'1.5cm'"/>

	<xsl:param name="page.margin.inner" select="'2.5cm'"/>
	<xsl:param name="page.margin.outer" select="'2.5cm'"/>

	<xsl:param name="body.start.indent" select="'5cm'"/>
	<xsl:param name="title.margin.left" select="'0cm'"/>

	<xsl:attribute-set name="normal.para.spacing">
    <xsl:attribute name="text-indent">0.6cm</xsl:attribute>
 	</xsl:attribute-set>

	<xsl:param name="header.rule" select="1"/>
	<xsl:param name="footer.rule" select="1"/>

	<xsl:param name="headers.on.blank.pages" select="1"></xsl:param>
	<xsl:param name="footers.on.blank.pages" select="1"></xsl:param>

  <xsl:param name="insert.xref.page.number">0</xsl:param>

  <xsl:attribute-set name="section.title.level1.properties">
  	<xsl:attribute name="font-size">14pt</xsl:attribute>
	</xsl:attribute-set>

	<xsl:attribute-set name="section.title.level2.properties">
  	<xsl:attribute name="font-size">11pt</xsl:attribute>
	</xsl:attribute-set>

	<xsl:attribute-set name="section.title.level3.properties">
  	<xsl:attribute name="font-size">10pt</xsl:attribute>
	</xsl:attribute-set>

	<xsl:attribute-set name="section.title.level4.properties">
  	<xsl:attribute name="font-size">10pt</xsl:attribute>
  	<xsl:attribute name="font-style">italic</xsl:attribute>  	
	</xsl:attribute-set>
	
	<xsl:attribute-set name="section.title.level5.properties">
  	<xsl:attribute name="font-size">10pt</xsl:attribute>
  	<xsl:attribute name="font-weight">normal</xsl:attribute>
  	<xsl:attribute name="font-style">italic</xsl:attribute>  	
	</xsl:attribute-set>

	<xsl:param name="make.single.year.ranges" select="1"/>
	<xsl:param name="make.year.ranges" select="1"/>
	<xsl:param name="ulink.hyphenate" select="'​​​​​​'"/>
	
	<!--
	<xsl:param name="hyphenate.verbatim" select="1"/>
	
	<xsl:attribute-set name="monospace.verbatim.properties">
  	<xsl:attribute name="wrap-option">wrap</xsl:attribute>
  	<xsl:attribute name="hyphenation-character">%</xsl:attribute>
	</xsl:attribute-set>
	-->
	
	<xsl:attribute-set name="formal.title.properties">
  	<xsl:attribute name="font-weight">bold</xsl:attribute>
	  <xsl:attribute name="font-size">10pt</xsl:attribute>
	  <xsl:attribute name="text-align">center</xsl:attribute>
	  <xsl:attribute name="hyphenate">false</xsl:attribute>
	  <xsl:attribute name="space-after.minimum">0.4em</xsl:attribute>
	  <xsl:attribute name="space-after.optimum">0.6em</xsl:attribute>
	  <xsl:attribute name="space-after.maximum">0.8em</xsl:attribute>
	</xsl:attribute-set>	
	
	<xsl:attribute-set name="verbatim.properties">
		<xsl:attribute name="background-color">#e0e0e0</xsl:attribute>
  	<xsl:attribute name="border">0.5pt solid black</xsl:attribute>
  	<xsl:attribute name="padding">0.1cm</xsl:attribute>
	</xsl:attribute-set>
	
	<xsl:attribute-set name="figure.properties">
		<!--<xsl:attribute name="background-color">#e0e0e0</xsl:attribute>-->
  	<xsl:attribute name="border">0.5pt solid black</xsl:attribute>
  	<xsl:attribute name="padding">0.1cm</xsl:attribute>
	</xsl:attribute-set>	

	<xsl:attribute-set name="table.properties">
		<!--<xsl:attribute name="background-color">#e0e0e0</xsl:attribute>-->
  	<xsl:attribute name="border">0.5pt solid black</xsl:attribute>
  	<xsl:attribute name="padding">0.1cm</xsl:attribute>
	</xsl:attribute-set>	
	
	<xsl:param name="header.column.widths">0 1 0</xsl:param>
	
	<xsl:param name="formal.title.placement">
		figure after
		example after
		equation after
		table after
		procedure after
	</xsl:param>
		
<!-- ============================== Chapter ======================= -->

<xsl:template name="chapter.title">
  <xsl:param name="node" select="."/>
	
	<fo:block start-indent="14cm" width="2cm" font-size="10pt" 
	  font-variant="small-caps" text-align="center" 
	  background-color="black" color="white">
		<xsl:call-template name="gentext">
	 		<xsl:with-param name="key" select="'Chapter'"/>
		</xsl:call-template>
	</fo:block>
	
	<fo:block padding-before="6pt" padding-after="2pt" font-size="36pt" 
		start-indent="14cm" width="2cm" text-align="center" 
		background-color="black" color="white" space-before="4pt">
	  <xsl:apply-templates select="$node" mode="label.markup"/>
	</fo:block>
	
	<fo:block space-before="4cm" space-after="0cm" font-variant="small-caps" text-align="center">
		<xsl:apply-templates select="$node" mode="title.markup"/>
	</fo:block>

	<fo:block space-after="0.5cm" space-before="0.2cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== Appendix ======================= -->

<xsl:template name="appendix.title">
  <xsl:param name="node" select="."/>
	
	<fo:block start-indent="14cm" width="2cm" font-size="10pt" 
	  font-variant="small-caps" text-align="center" 
	  background-color="black" color="white">
		<xsl:call-template name="gentext">
	 		<xsl:with-param name="key" select="'Appendix'"/>
		</xsl:call-template>
	</fo:block>
	
	<fo:block padding-before="6pt" padding-after="2pt" font-size="36pt" 
		start-indent="14cm" width="2cm" text-align="center" 
		background-color="black" color="white" space-before="4pt">
	  <xsl:apply-templates select="$node" mode="label.markup"/>
	</fo:block>
	
	<fo:block space-before="4cm" space-after="0cm" font-variant="small-caps" text-align="center">
		<xsl:apply-templates select="$node" mode="title.markup"/>
	</fo:block>

	<fo:block space-after="0.5cm" space-before="0.2cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== Bibliography ======================= -->

<xsl:template name="bibliography.title">
  <xsl:param name="node" select="."/>
		
	<fo:block space-before="6.25cm" space-after="0cm" font-variant="small-caps" text-align="center">
		<xsl:call-template name="gentext">
	 		<xsl:with-param name="key" select="'Bibliography'"/>
		</xsl:call-template>
	</fo:block>

	<fo:block space-after="0.5cm" space-before="0.2cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== Glossary ======================= -->

<xsl:template name="glossary.title">
  <xsl:param name="node" select="."/>
		
	<fo:block space-before="6.25cm" space-after="0cm" font-variant="small-caps" 
		text-align="center">
		<xsl:call-template name="gentext">
	 		<xsl:with-param name="key" select="'Glossary'"/>
		</xsl:call-template>
	</fo:block>

	<fo:block space-after="0.5cm" space-before="0.2cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== table.of.contents ======================= -->

<xsl:template name="table.of.contents.titlepage">
	<fo:block space-before="5.9cm" space-after="0cm" font-variant="small-caps" 
		text-align="center" font-size="24.8832pt" font-weight="bold"
	  font-family="{$title.fontset}">
		<xsl:call-template name="gentext">
      <xsl:with-param name="key" select="'TableofContents'"/>
		</xsl:call-template>
	</fo:block>

	<fo:block space-after="1cm" space-before="0.65cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== list.of.tables ======================= -->

<xsl:template name="list.of.tables.titlepage">
	<fo:block space-before="6.25cm" space-after="0cm" font-variant="small-caps" 
		text-align="center" font-size="24.8832pt" font-weight="bold"
	  font-family="{$title.fontset}">
		<xsl:call-template name="gentext">
      <xsl:with-param name="key" select="'ListofTables'"/>
		</xsl:call-template>
	</fo:block>

	<fo:block space-after="1cm" space-before="0.65cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== table.of.figures ======================= -->

<xsl:template name="list.of.figures.titlepage">
	<fo:block space-before="6.25cm" space-after="0cm" font-variant="small-caps" 
		text-align="center" font-size="24.8832pt" font-weight="bold"
	  font-family="{$title.fontset}">
		<xsl:call-template name="gentext">
      <xsl:with-param name="key" select="'ListofFigures'"/>
		</xsl:call-template>
	</fo:block>

	<fo:block space-after="1cm" space-before="0.65cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== list.of.examples ======================= -->

<xsl:template name="list.of.examples.titlepage">
	<fo:block space-before="6.25cm" space-after="0cm" font-variant="small-caps" 
		text-align="center" font-size="24.8832pt" font-weight="bold"
	  font-family="{$title.fontset}">
		<xsl:call-template name="gentext">
      <xsl:with-param name="key" select="'ListofExamples'"/>
		</xsl:call-template>
	</fo:block>

	<fo:block space-after="1cm" space-before="0.65cm">
		<fo:leader leader-pattern="rule" leader-length="16cm" rule-thickness="0.5pt"/>
	</fo:block>
</xsl:template>

<!-- ============================== Titlepage.verso ======================= -->

<xsl:template name="book.titlepage.verso">
	<fo:block space-before="21.6cm" padding="4pt" border="1.5pt solid black" 
		start-indent="0.5cm" end-indent="0.5cm">
	<fo:block text-align="center" font-weight="bold" space-after="6pt">
		© Copyright
		<xsl:call-template name="copyright.years">
			<xsl:with-param name="years" select="/book/bookinfo/copyright/year"/>
    	<xsl:with-param name="print.ranges" select="$make.year.ranges"/>
			<xsl:with-param name="single.year.ranges" select="$make.single.year.ranges"/>
		</xsl:call-template>
		<xsl:text> </xsl:text>
		<xsl:value-of select="/book/bookinfo/copyright/holder"/>
	</fo:block>
	<fo:block>
		<xsl:value-of select="/book/bookinfo/legalnotice/para"/>  
	</fo:block>
	</fo:block>
</xsl:template>

<!-- ============================== Titlepage.recto ======================= -->

<xsl:template name="book.titlepage.recto">
	<fo:block font-variant="small-caps" text-align="center"
		font-size="16pt" font-weight="bold" space-after="6pt">
		<xsl:value-of select="bookinfo/affiliation/orgname"/>
	</fo:block>
		<fo:block font-variant="small-caps" text-align="center"
		font-size="14pt" font-weight="bold">
		<xsl:value-of select="bookinfo/affiliation/orgdiv"/>
	</fo:block>
	<fo:block font-variant="small-caps" text-align="center"
		font-size="10pt" font-weight="bold" space-after="18pt">
		<xsl:value-of select="bookinfo/affiliation/year"/>
	</fo:block>
	
	<fo:block text-align="center"
		font-size="14pt" font-weight="bold" space-after="8pt">
	Projet de recherche
	</fo:block>
	
	<fo:block text-align="center"
		font-size="10pt" font-weight="bold" space-after="6cm">
	ANNÉE UNIVERSITAIRE 2005/2006
	</fo:block>
	
	<fo:block text-align="center"
		font-size="16pt" space-after="18pt">
		"<xsl:value-of select="bookinfo/title"/>"
	</fo:block>
	
	<fo:block text-align="center"
		font-size="12pt" space-after="6cm">
		<xsl:value-of select="bookinfo/subtitle"/>
	</fo:block>
	
	<fo:block text-align="center"
		font-size="12pt" space-after="1cm">
		Présenté par 
		<xsl:for-each select="bookinfo/authorgroup/author">
			<xsl:sort select="current()/surname"/>
			<xsl:value-of select="current()/firstname"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="current()/surname"/>
			<xsl:if test="position() != last()">
				<xsl:if test="(position() + 1) != last()">
					<xsl:text>, </xsl:text>
				</xsl:if>
				<xsl:if test="(position() + 1) = last()">
					<xsl:text> et </xsl:text>
				</xsl:if>
			</xsl:if>
		</xsl:for-each> 
	</fo:block>

	<fo:block text-align="center"
		font-size="12pt" space-after="3.5cm">
		<xsl:value-of select="bookinfo/pubdate"/>
	</fo:block>
	
	<fo:block text-align="center"
		font-size="12pt">
		<xsl:for-each select="bookinfo/othercredit[@class='coordinateur']">
			<xsl:sort select="current()/surname"/>
			
			<xsl:if test="position() = 1">
			Coordinateur<xsl:if test="last() &gt; 1">s</xsl:if>
			<xsl:text> : </xsl:text>
			</xsl:if>
			
			<xsl:value-of select="current()/firstname"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="current()/surname"/>
			<xsl:if test="position() != last()">
				<xsl:if test="(position() + 1) != last()">
					<xsl:text>, </xsl:text>
				</xsl:if>
				<xsl:if test="(position() + 1) = last()">
					<xsl:text> et </xsl:text>
				</xsl:if>
			</xsl:if>
		</xsl:for-each> 
	</fo:block>
	
	<fo:block text-align="center"
		font-size="12pt">
		<xsl:for-each select="bookinfo/othercredit[@class='enseignant']">
			<xsl:sort select="current()/surname"/>
			
			<xsl:if test="position() = 1">
			Tuteur<xsl:if test="last() &gt; 1">s</xsl:if>
			enseignant<xsl:if test="last() &gt; 1">s</xsl:if><xsl:text>  : </xsl:text>
			</xsl:if>
			
			<xsl:value-of select="current()/firstname"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="current()/surname"/>
			<xsl:if test="position() != last()">
				<xsl:if test="(position() + 1) != last()">
					<xsl:text>, </xsl:text>
				</xsl:if>
				<xsl:if test="(position() + 1) = last()">
					<xsl:text> et </xsl:text>
				</xsl:if>
			</xsl:if>
		</xsl:for-each> 
	</fo:block>
	
	<fo:block text-align="center"
		font-size="12pt">
		<xsl:for-each select="bookinfo/othercredit[@class='entreprise']">
			<xsl:sort select="current()/surname"/>
			
			<xsl:if test="position() = 1">
			Tuteur<xsl:if test="last() &gt; 1">s</xsl:if>
			<xsl:text> entreprise : </xsl:text>
			</xsl:if>
			
			<xsl:value-of select="current()/firstname"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="current()/surname"/>
			<xsl:if test="position() != last()">
				<xsl:if test="(position() + 1) != last()">
					<xsl:text>, </xsl:text>
				</xsl:if>
				<xsl:if test="(position() + 1) = last()">
					<xsl:text> et </xsl:text>
				</xsl:if>
			</xsl:if>
		</xsl:for-each> 
	</fo:block>	
</xsl:template>

<!-- ============================== Header.table ======================= -->

<xsl:template name="header.table">
  <xsl:param name="pageclass" select="''"/>
  <xsl:param name="sequence" select="''"/>
  <xsl:param name="gentext-key" select="''"/>

  <!-- default is a single table style for all headers -->
  <!-- Customize it for different page classes or sequence location -->

  <xsl:choose>
      <xsl:when test="$pageclass = 'index'">
          <xsl:attribute name="margin-left">0pt</xsl:attribute>
      </xsl:when>
  </xsl:choose>

  <xsl:variable name="column1">
    <xsl:choose>
      <xsl:when test="$double.sided = 0">1</xsl:when>
      <xsl:when test="$sequence = 'first' or $sequence = 'odd'">1</xsl:when>
      <xsl:otherwise>3</xsl:otherwise>
    </xsl:choose>
  </xsl:variable>

  <xsl:variable name="column3">
    <xsl:choose>
      <xsl:when test="$double.sided = 0">3</xsl:when>
      <xsl:when test="$sequence = 'first' or $sequence = 'odd'">3</xsl:when>
      <xsl:otherwise>1</xsl:otherwise>
    </xsl:choose>
  </xsl:variable>

  <xsl:variable name="candidate">
    <fo:table table-layout="fixed" width="100%">
      <xsl:call-template name="head.sep.rule">
        <xsl:with-param name="pageclass" select="$pageclass"/>
        <xsl:with-param name="sequence" select="$sequence"/>
        <xsl:with-param name="gentext-key" select="$gentext-key"/>
      </xsl:call-template>

      <fo:table-column column-number="1">
        <xsl:attribute name="column-width">
          <xsl:text>proportional-column-width(</xsl:text>
          <xsl:call-template name="header.footer.width">
            <xsl:with-param name="location">header</xsl:with-param>
            <xsl:with-param name="position" select="$column1"/>
          </xsl:call-template>
          <xsl:text>)</xsl:text>
        </xsl:attribute>
      </fo:table-column>
      <fo:table-column column-number="2">
        <xsl:attribute name="column-width">
          <xsl:text>proportional-column-width(</xsl:text>
          <xsl:call-template name="header.footer.width">
            <xsl:with-param name="location">header</xsl:with-param>
            <xsl:with-param name="position" select="2"/>
          </xsl:call-template>
          <xsl:text>)</xsl:text>
        </xsl:attribute>
      </fo:table-column>
      <fo:table-column column-number="3">
        <xsl:attribute name="column-width">
          <xsl:text>proportional-column-width(</xsl:text>
          <xsl:call-template name="header.footer.width">
            <xsl:with-param name="location">header</xsl:with-param>
            <xsl:with-param name="position" select="$column3"/>
          </xsl:call-template>
          <xsl:text>)</xsl:text>
        </xsl:attribute>
      </fo:table-column>

      <fo:table-body>
        <fo:table-row height="14pt">
          <fo:table-cell text-align="left"
                         display-align="before">
            <xsl:if test="$fop.extensions = 0">
              <xsl:attribute name="relative-align">baseline</xsl:attribute>
            </xsl:if>
            <fo:block>
              <xsl:call-template name="header.content">
                <xsl:with-param name="pageclass" select="$pageclass"/>
                <xsl:with-param name="sequence" select="$sequence"/>
                <xsl:with-param name="position" select="'left'"/>
                <xsl:with-param name="gentext-key" select="$gentext-key"/>
              </xsl:call-template>
            </fo:block>
          </fo:table-cell>
          <fo:table-cell text-align="center"
                         display-align="before">
            <xsl:if test="$fop.extensions = 0">
              <xsl:attribute name="relative-align">baseline</xsl:attribute>
            </xsl:if>
            <fo:block>
              <xsl:call-template name="header.content">
                <xsl:with-param name="pageclass" select="$pageclass"/>
                <xsl:with-param name="sequence" select="$sequence"/>
                <xsl:with-param name="position" select="'center'"/>
                <xsl:with-param name="gentext-key" select="$gentext-key"/>
              </xsl:call-template>
            </fo:block>
          </fo:table-cell>
          <fo:table-cell text-align="right"
                         display-align="before">
            <xsl:if test="$fop.extensions = 0">
              <xsl:attribute name="relative-align">baseline</xsl:attribute>
            </xsl:if>
            <fo:block>
              <xsl:call-template name="header.content">
                <xsl:with-param name="pageclass" select="$pageclass"/>
                <xsl:with-param name="sequence" select="$sequence"/>
                <xsl:with-param name="position" select="'right'"/>
                <xsl:with-param name="gentext-key" select="$gentext-key"/>
              </xsl:call-template>
            </fo:block>
          </fo:table-cell>
        </fo:table-row>
      </fo:table-body>
    </fo:table>
  </xsl:variable>

  <!-- Really output a header? -->
  <xsl:choose>
    <xsl:when test="$pageclass = 'titlepage'">
    		<!--
    			and $gentext-key = 'book'
                    and $sequence='first'">-->
      <!-- no, book titlepages have no headers at all -->
    </xsl:when>
    <xsl:when test="$sequence='first'">
      <!-- no, first page of front matter have no headers  -->
    </xsl:when>
        <xsl:when test="$pageclass='front'">
      <!-- no, first page of front matter have no headers  -->
    </xsl:when>
    <xsl:when test="$sequence = 'blank' and $headers.on.blank.pages = 0">
      <!-- no output -->
    </xsl:when>
    <xsl:otherwise>
      <xsl:copy-of select="$candidate"/>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<!-- ============================== Header.content ======================= -->

<xsl:template name="header.content">
  <xsl:param name="pageclass" select="''"/>
  <xsl:param name="sequence" select="''"/>
  <xsl:param name="position" select="''"/>
  <xsl:param name="gentext-key" select="''"/>

<!--
  <fo:block>
    <xsl:value-of select="$pageclass"/>
    <xsl:text>, </xsl:text>
    <xsl:value-of select="$sequence"/>
    <xsl:text>, </xsl:text>
    <xsl:value-of select="$position"/>
    <xsl:text>, </xsl:text>
    <xsl:value-of select="$gentext-key"/>
  </fo:block>
-->

  <fo:block>

    <!-- sequence can be odd, even, first, blank -->
    <!-- position can be left, center, right -->
    <xsl:choose>
      <xsl:when test="$sequence = 'blank'">
        <!-- nothing -->
      </xsl:when>

      <xsl:when test="$position='left'">
        <!-- Same for odd, even, empty, and blank sequences -->
        <xsl:call-template name="draft.text"/>
      </xsl:when>

      <xsl:when test="($sequence='odd' or $sequence='even') and $position='center'">
        <xsl:if test="$pageclass != 'titlepage'">
          <xsl:choose>
            <xsl:when test="ancestor::book and ($double.sided != 0)">
              <fo:retrieve-marker retrieve-class-name="section.head.marker"
                                  retrieve-position="first-including-carryover"
                                  retrieve-boundary="page-sequence"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:apply-templates select="." mode="object.title.markup"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:if>
      </xsl:when>

      <xsl:when test="$position='center'">
        <!-- nothing for empty and blank sequences -->
      </xsl:when>

      <xsl:when test="$position='right'">
        <!-- Same for odd, even, empty, and blank sequences -->
        <xsl:call-template name="draft.text"/>
      </xsl:when>

      <xsl:when test="$sequence = 'first'">
        <!-- nothing for first pages -->
      </xsl:when>

      <xsl:when test="$sequence = 'blank'">
        <!-- nothing for blank pages -->
      </xsl:when>
    </xsl:choose>
  </fo:block>
</xsl:template>

<!-- ============================== Footer.table ======================= -->

<xsl:template name="footer.table">
  <xsl:param name="pageclass" select="''"/>
  <xsl:param name="sequence" select="''"/>
  <xsl:param name="gentext-key" select="''"/>

  <!-- default is a single table style for all footers -->
  <!-- Customize it for different page classes or sequence location -->

  <xsl:choose>
      <xsl:when test="$pageclass = 'index'">
          <xsl:attribute name="margin-left">0pt</xsl:attribute>
      </xsl:when>
  </xsl:choose>

  <xsl:variable name="column1">
    <xsl:choose>
      <xsl:when test="$double.sided = 0">1</xsl:when>
      <xsl:when test="$sequence = 'first' or $sequence = 'odd'">1</xsl:when>
      <xsl:otherwise>3</xsl:otherwise>
    </xsl:choose>
  </xsl:variable>

  <xsl:variable name="column3">
    <xsl:choose>
      <xsl:when test="$double.sided = 0">3</xsl:when>
      <xsl:when test="$sequence = 'first' or $sequence = 'odd'">3</xsl:when>
      <xsl:otherwise>1</xsl:otherwise>
    </xsl:choose>
  </xsl:variable>

  <xsl:variable name="candidate">
    <fo:table table-layout="fixed" width="100%">
      <xsl:call-template name="foot.sep.rule">
        <xsl:with-param name="pageclass" select="$pageclass"/>
        <xsl:with-param name="sequence" select="$sequence"/>
        <xsl:with-param name="gentext-key" select="$gentext-key"/>
      </xsl:call-template>
      <fo:table-column column-number="1">
        <xsl:attribute name="column-width">
          <xsl:text>proportional-column-width(</xsl:text>
          <xsl:call-template name="header.footer.width">
            <xsl:with-param name="location">footer</xsl:with-param>
            <xsl:with-param name="position" select="$column1"/>
          </xsl:call-template>
          <xsl:text>)</xsl:text>
        </xsl:attribute>
      </fo:table-column>
      <fo:table-column column-number="2">
        <xsl:attribute name="column-width">
          <xsl:text>proportional-column-width(</xsl:text>
          <xsl:call-template name="header.footer.width">
            <xsl:with-param name="location">footer</xsl:with-param>
            <xsl:with-param name="position" select="2"/>
          </xsl:call-template>
          <xsl:text>)</xsl:text>
        </xsl:attribute>
      </fo:table-column>
      <fo:table-column column-number="3">
        <xsl:attribute name="column-width">
          <xsl:text>proportional-column-width(</xsl:text>
          <xsl:call-template name="header.footer.width">
            <xsl:with-param name="location">footer</xsl:with-param>
            <xsl:with-param name="position" select="$column3"/>
          </xsl:call-template>
          <xsl:text>)</xsl:text>
        </xsl:attribute>
      </fo:table-column>

      <fo:table-body>
        <fo:table-row height="14pt">
          <fo:table-cell text-align="left"
                         display-align="after">
            <xsl:if test="$fop.extensions = 0">
              <xsl:attribute name="relative-align">baseline</xsl:attribute>
            </xsl:if>
            <fo:block>
              <xsl:call-template name="footer.content">
                <xsl:with-param name="pageclass" select="$pageclass"/>
                <xsl:with-param name="sequence" select="$sequence"/>
                <xsl:with-param name="position" select="'left'"/>
                <xsl:with-param name="gentext-key" select="$gentext-key"/>
              </xsl:call-template>
            </fo:block>
          </fo:table-cell>
          <fo:table-cell text-align="center"
                         display-align="after">
            <xsl:if test="$fop.extensions = 0">
              <xsl:attribute name="relative-align">baseline</xsl:attribute>
            </xsl:if>
            <fo:block>
              <xsl:call-template name="footer.content">
                <xsl:with-param name="pageclass" select="$pageclass"/>
                <xsl:with-param name="sequence" select="$sequence"/>
                <xsl:with-param name="position" select="'center'"/>
                <xsl:with-param name="gentext-key" select="$gentext-key"/>
              </xsl:call-template>
            </fo:block>
          </fo:table-cell>
          <fo:table-cell text-align="right"
                         display-align="after">
            <xsl:if test="$fop.extensions = 0">
              <xsl:attribute name="relative-align">baseline</xsl:attribute>
            </xsl:if>
            <fo:block>
              <xsl:call-template name="footer.content">
                <xsl:with-param name="pageclass" select="$pageclass"/>
                <xsl:with-param name="sequence" select="$sequence"/>
                <xsl:with-param name="position" select="'right'"/>
                <xsl:with-param name="gentext-key" select="$gentext-key"/>
              </xsl:call-template>
            </fo:block>
          </fo:table-cell>
        </fo:table-row>
      </fo:table-body>
    </fo:table>
  </xsl:variable>

  <!-- Really output a footer? -->
  <xsl:choose>
    <xsl:when test="$pageclass='titlepage'">
    		<!--
    		and $gentext-key='book'
                    and $sequence='first'"> -->
      <!-- no, book titlepages have no footers at all -->
    </xsl:when>
    <xsl:when test="$sequence = 'blank' and $footers.on.blank.pages = 0">
      <!-- no output -->
    </xsl:when>
    <xsl:otherwise>
      <xsl:copy-of select="$candidate"/>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<!-- ============================== Footer.content ======================= -->

<xsl:param name="footer.column.widths">8 1 1</xsl:param>

<xsl:template name="footer.content">
  <xsl:param name="pageclass" select="''"/>
  <xsl:param name="sequence" select="''"/>
  <xsl:param name="position" select="''"/>
  <xsl:param name="gentext-key" select="''"/>

  <fo:block>
    <!-- pageclass can be front, body, back -->
    <!-- sequence can be odd, even, first, blank -->
    <!-- position can be left, center, right -->
    <xsl:choose>
      <xsl:when test="$pageclass = 'titlepage'">
        <!-- nop; no footer on title pages -->
      </xsl:when>

      <xsl:when test="$double.sided != 0 and $sequence = 'even'
                      and $position='left'">
        <fo:page-number/>
      </xsl:when>

      <xsl:when test="$double.sided != 0 and ($sequence = 'odd' or $sequence = 'first')
                      and $position='right'">
        <fo:page-number/>
      </xsl:when>

      <xsl:when test="$double.sided = 0 and $position='left'">
        <xsl:value-of select="/book/bookinfo/affiliation/orgname"/>
      </xsl:when>

      <xsl:when test="$double.sided = 0 and $position='right'">
        <fo:page-number/>
      </xsl:when>

      <xsl:when test="$sequence='blank'">
        <xsl:choose>
          <xsl:when test="$double.sided != 0 and $position = 'left'">
            <fo:page-number/>
          </xsl:when>
          <xsl:when test="$double.sided = 0 and $position = 'center'">
            <fo:page-number/>
          </xsl:when>
          <xsl:otherwise>
            <!-- nop -->
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>


      <xsl:otherwise>
        <!-- nop -->
      </xsl:otherwise>
    </xsl:choose>
  </fo:block>
</xsl:template>

</xsl:stylesheet>