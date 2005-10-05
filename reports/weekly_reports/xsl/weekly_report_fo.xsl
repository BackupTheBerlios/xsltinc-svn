<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:fn="http://www.w3.org/2005/02/xpath-functions"
xmlns:fo="http://www.w3.org/1999/XSL/Format">

<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>

<xsl:template match="weekly_report">

	<fo:root>

		<fo:layout-master-set>
			<fo:simple-page-master master-name="page"
				page-height="29.7cm" page-width="21cm"
				margin-top="2.5cm" margin-bottom="2cm"
				margin-left="2.5cm" margin-right="2.5cm">
				
				<fo:region-before extent="0cm"/>
				<fo:region-after extent="0cm"/>
				<fo:region-body margin-top="0cm" margin-bottom="0cm"/>
				
			</fo:simple-page-master>
		</fo:layout-master-set>
	
		<fo:page-sequence master-reference="page">
			<fo:flow flow-name="xsl-region-body" 
				font-size="12pt"
				font-family="serif">		
				<xsl:apply-templates />				
			</fo:flow>
		</fo:page-sequence>

	</fo:root>

</xsl:template>

<xsl:template match="reportinfo">
	<fo:block font-variant="small-caps" padding-top="3pt" 
					text-align="center" color="white" background-color="#000000"
					space-after.optimum="10pt" line-height="24pt"
					font-family="sans-serif" font-size="18pt">
					Fiche de suivi de projet <xsl:value-of select="schoolyears"/>
	</fo:block>
	<fo:block font-variant="small-caps" text-align="center"
		font-family="sans-serif" font-size="14pt">
		<xsl:value-of select="school"/>
	</fo:block>
	<fo:block text-align="center" font-family="sans-serif">
		Département <xsl:value-of select="department"/> - <xsl:value-of select="promotion"/>
	</fo:block>
	
	<fo:block space-before.optimum="24pt" 
		font-variant="small-caps" text-align="center" 
		font-size="16pt">
		<xsl:value-of select="projecttitle"/>
	</fo:block>

	<fo:block font-size="4pt" text-align="center" space-after.optimum="20pt">
		<fo:leader leader-length="10cm" leader-pattern="rule"/>
	</fo:block>
	
	<xsl:apply-templates select="team"/>
	
	<fo:block space-before.optimum="16pt"
		text-align="center" font-size="4pt">
		<fo:leader leader-length="10cm" leader-pattern="rule"/>
	</fo:block>
			
	<fo:block text-align="center" font-size="14pt" font-weight="bold" 
		space-before.optimum="0.2cm" space-after.optimum="0.2cm">
		Semaine <xsl:value-of select="/weekly_report/@week"/> 
		(<xsl:value-of select="/weekly_report/@startdate"/>  - <xsl:value-of select="/weekly_report/@stopdate"/> )
	</fo:block>
			
	<fo:block space-after.optimum="16pt"
		text-align="center" font-size="4pt">
		<fo:leader leader-length="10cm" leader-pattern="rule"/>
	</fo:block>

</xsl:template>

<xsl:template match="team">
	<fo:table table-layout="fixed" text-align="center">
		<fo:table-column column-width="8cm" />
		<fo:table-column column-width="8cm" />
					
		<fo:table-header font-weight="bold">
			<fo:table-row>
				<fo:table-cell padding="0.15cm" 
					background-color="#6d7179" color="#ffffff">
					<fo:block>Étudiants</fo:block>
				</fo:table-cell>
				<fo:table-cell padding="0.15cm" 
					background-color="#6d7179" color="#ffffff">
					<fo:block>Tuteurs enseignants</fo:block>
				</fo:table-cell>
			</fo:table-row>
		</fo:table-header>
		<fo:table-body>
			<fo:table-row>
				<fo:table-cell padding-top="0.2cm">							
					<xsl:apply-templates select="students"/>						
				</fo:table-cell>
				<fo:table-cell padding-top="0.2cm">
					<xsl:apply-templates select="tutors"/>
				</fo:table-cell>						
			</fo:table-row>
		</fo:table-body>		
	</fo:table>
</xsl:template>

<xsl:template match="tutors">
	<xsl:for-each select="tutor">
		<xsl:sort select="lastname"/>
		<xsl:sort select="firstname"/>
		<fo:block>
			<xsl:value-of select="firstname"/><xsl:text> </xsl:text><xsl:value-of select="lastname"/>
		</fo:block>
		<fo:block space-before.maximum="0pt" space-after.optimum="6pt">
			&lt;<fo:inline font-size="9pt" color="blue" text-decoration="underline"><xsl:value-of select="email"/></fo:inline>&gt;
		</fo:block>
	</xsl:for-each>
</xsl:template>

<xsl:template match="students">
	<xsl:for-each select="student">
		<xsl:sort select="lastname"/>
		<xsl:sort select="firstname"/>	
		<fo:block>
			<xsl:value-of select="firstname"/><xsl:text> </xsl:text><xsl:value-of select="lastname"/>
		</fo:block>
		<fo:block space-before.maximum="0pt" space-after.optimum="6pt">
			&lt;<fo:inline font-size="9pt" color="blue" text-decoration="underline"><xsl:value-of select="email"/></fo:inline>&gt;
		</fo:block>
	</xsl:for-each>
</xsl:template>

<xsl:template match="donelist">
	<fo:block space-before.optimum="16pt" space-after.optimum="6pt"
		font-weight="bold" font-size="16pt">
		Travail effectué
		<fo:block font-size="4pt">
			<fo:leader leader-length="5cm" leader-pattern="rule"/>
		</fo:block>
	</fo:block>
				
	<xsl:for-each select="done">
		<fo:block text-align="justify" font-size="12pt" space-after.optimum="10pt" font-weight="normal">
			<xsl:value-of select="current()"/>
		</fo:block>	
	</xsl:for-each> 
</xsl:template>

<xsl:template match="issues">
	<fo:block space-before.optimum="16pt" space-after.optimum="6pt"
		font-weight="bold" font-size="16pt">
		Problèmes rencontrés
		<fo:block font-size="4pt">
			<fo:leader leader-length="5cm" leader-pattern="rule"/>
		</fo:block>
	</fo:block>
				
	<xsl:for-each select="issue">
		<fo:block text-align="justify" font-size="12pt" space-after.optimum="10pt" font-weight="normal">
			<xsl:value-of select="current()"/>
		</fo:block>	
	</xsl:for-each>  
</xsl:template> 

<xsl:template match="todolist">
 	<fo:block space-before.optimum="16pt" space-after.optimum="6pt"
		font-weight="bold" font-size="16pt">
		Travail prévisionnel
		<fo:block font-size="4pt">
			<fo:leader leader-length="5cm" leader-pattern="rule"/>
		</fo:block>
	</fo:block>
				
	<xsl:for-each select="todo">
		<fo:block text-align="justify" font-size="12pt" space-after.optimum="10pt" font-weight="normal">
			<xsl:value-of select="current()"/>
		</fo:block>	
	</xsl:for-each> 
</xsl:template>

</xsl:stylesheet>