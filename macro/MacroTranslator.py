
if __name__ == '__main__':
    # myParser = KBParser()
    import xml.etree.ElementTree as ET
    from datetime import *

    ET.register_namespace('', "http://schemas.malighting.de/grandma2/xml/MA")
    tree = ET.parse('Templates/macro_3.xml')
    newTree = ET.parse('Templates/macro_3.xml')
    newRoot = newTree.getroot()
    root = tree.getroot()

    # Set datetime on Info element
    infoElement = root.find(".//{http://schemas.malighting.de/grandma2/xml/MA}Info")
    infoElement.set('datetime', datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%S'))
    infoElement.set('showfile', 'KB-Show-' + datetime.strftime(datetime.now(), '%Y-%m-%d-%H%M%S'))

    # namespaces = {'ns': 'http://schemas.malighting.de/grandma2/xml/MA'}
    # macro = root.find(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro")
    # macroLine = root.findall(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro/"
    #  "{http://schemas.malighting.de/grandma2/xml/MA}Macroline")
    # macroText = root.findall(".//Text")

    selectFixtureId = 101
    macroTextSelectFixtureTemplate = 'Fixture {0}'.format(selectFixtureId)
    macroTextMove3DTemplate = 'Move3D At{0}{1}{2}'

    import csv

    csvX = []
    csvY = []
    csvZ = []
    currMacroIndex = 0;

    with open('../csvExample-11-17-17.csv', 'r') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            csvX.append(row[1])
            csvY.append(row[2])
            csvZ.append(row[3])

            fixtureSelect = ET.Element('Macroline', index=str(currMacroIndex))
            fixtureSelectText = ET.SubElement(fixtureSelect, "text")
            fixtureSelectText.text = macroTextSelectFixtureTemplate

            selectFixtureId += 1

            fixtureCommand = ET.Element('Macroline', index=str(currMacroIndex + 1))
            fixtureCommandText = ET.SubElement(fixtureCommand, "text")
            fixtureCommandText.text = macroTextMove3DTemplate.format(row[1], row[3], row[2])

            currMacroIndex += 2

            root.find(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro").append(fixtureSelect)
            root.find(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro").append(fixtureCommand)

    # Renumber all macro lines sequentially
    '''for index, mLine in enumerate(root.find(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro/"
                                            "{http://schemas.malighting.de/grandma2/xml/MA}Macroline")):
        mLine.set('index', str(index))
    '''
    """
    for fix in fixture:
        print('Fixture Info: ID - ', fix.get('fixture_id'), ' Name - ', fix.get('name'), ' Index - ', fix.get('index'))

    print('---------------------------------------')

    for loc in location:
        print('Location Info: x - ', loc.get('x'), ' y - ', loc.get('y'), ' z - ', loc.get('z'))

    print('---------------------------------------')
    """

    """
    for index, loc in enumerate(location):
        loc.set('x', csvX[index].strip())
        loc.set('y', csvY[index].strip())
        loc.set('z', csvZ[index].strip())
        # print(loc.get('x'))
    """

    fileStamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H%M%S')
    fileNameStamp = 'Output/KB_Parser-{}.xml'.format(fileStamp)

    import xml.dom.minidom as MD
    import os

    xmlstr = ET.tostring(root, encoding='utf8', method='xml')
    xml_p = MD.parseString(xmlstr)
    pretty_xml = xml_p.toprettyxml()
    print(pretty_xml)

    # Write new XML
    f = open(fileNameStamp, 'w')
    pretty_xml = os.linesep.join([s for s in pretty_xml.splitlines() if s.strip()])
    f.write(pretty_xml)
    f.close()

    # pretty_xml.
    # pretty_xml.writexml('Output/KB_Parser-{}.xml'.format(fileStamp))
    # tree.write('Output/KB_Parser-{}.xml'.format(fileStamp))
    # newTree.write('Output/KB_Parser-Blank-{}.xml'.format(fileStamp))

"""
<?xml version="1.0" encoding="utf-8"?>
<MA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.malighting.de/grandma2/xml/MA" xsi:schemaLocation="http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.3.4/MA.xsd" major_vers="3" minor_vers="3" stream_vers="4">
	<Info datetime="2017-12-06T04:13:13" showfile="layimptest" />
	<Macro index="2">
		<Macroline index="0">
			<text>Fixture 101</text>
		</Macroline>
		<Macroline index="1">
			<text>Move3D At 10 14 -8</text>
		</Macroline>
	</Macro>
</MA>
"""

# Documentation: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

"""
EXAMPLES:

# Update an attribute
for rank in root.iter('rank'):
     new_rank = int(rank.text) + 1
     rank.text = str(new_rank)
     rank.set('updated', 'yes')

# Find elements
for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)


# XPath Selector Examples:

# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")
"""