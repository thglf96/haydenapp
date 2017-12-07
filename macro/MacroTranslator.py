
if __name__ == '__main__':
    # myParser = KBParser()
    import xml.etree.ElementTree as ET

    ET.register_namespace('', "http://schemas.malighting.de/grandma2/xml/MA")
    tree = ET.parse('macro_3.xml')
    root = tree.getroot()

    # namespaces = {'ns': 'http://schemas.malighting.de/grandma2/xml/MA'}
    macro = root.find(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro/")
    macroLine = root.findall(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro/"
                             "{http://schemas.malighting.de/grandma2/xml/MA}Macroline")
    # macroText = root.findall(".//Text")

    macroTextMove3DTemplate = 'Move3D At {0} {1} {2}'

    import csv

    csvX = []
    csvY = []
    csvZ = []

    with open('../csvExample-11-17-17.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            csvX.append(row[1])
            csvY.append(row[2])
            csvZ.append(row[3])
            currIndex = len(root.findall(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro/"
                                         "{http://schemas.malighting.de/grandma2/xml/MA}Macroline")) + 1
            tempLine = ET.Element('Macroline', index=str(currIndex))
            # tempLineText = ET.Element('text', text=macroTextMove3DTemplate.format(row[1], row[3], row[2]))
            # newMacro = ET.SubElement(tempLine, tempLineText)
            # root.append(newMacro)

            # currMacroLine = ET.SubElement(macro, 'Macroline')
            # currMacroLineText = ET.SubElement(currMacroLine, 'text')
            # currMacroLineText.text = macroTextMove3DTemplate.format(row[1], row[3], row[2])

            tempA = ET.SubElement(tempLine, "text")
            tempA.text = macroTextMove3DTemplate.format(row[1], row[3], row[2])
            root.find(".//{http://schemas.malighting.de/grandma2/xml/MA}Macro/").append(tempLine)

            # macroLine[len(macroLine) - 1].append(tempLine)
            # print(macro)
            # your_list = map(tuple, reader)

    # Renumber all macro lines sequentially
    for index, mLine in enumerate(macroLine):
        mLine.set('index', str(index))

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

    from datetime import *

    fileStamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H%M%S')

    # Write new XML
    tree.write('Output/KB_Parser-{}.xml'.format(fileStamp))

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