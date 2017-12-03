class KBParser:
    def __init__(self):
        self.speed = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))


if __name__ == '__main__':
    myParser = KBParser()
    import xml.etree.ElementTree as ET

    tree = ET.parse('layers_4.xml')
    root = tree.getroot()

    fixture = root.findall(".//*[@fixture_id]")
    locations = root.findall(".//Layers")
    xyz = root.findall(".//*[@x][@y][@z]")
    fixtureLoc = root.findall("./Layers/Layer/Fixture/SubFixture/AbsolutePosition/Location")

    print('Fixtures: ', len(fixture))
    print('Locations: ', len(locations))

    # for child in fixture:
    # print(child.tag)

    from datetime import *
    fileStamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H%M%S')

    # Write new XML
    # tree.write('KB_Parser-{}.xml'.format(fileStamp))

"""
 Objective:
 The location we seek to affect on multi-instance fixtures is a child of the ‘Fixture' Element, whereas on a single
     instance fixture it is a child of the ‘SubFixture' Element.


Structure:     
CSV Key (a, b, c, d) a=fixture id b=x c=y d=z.

‘a’ will reference the ‘fixture_id’

‘b’ will replace the current ‘x’ attribute of Fixture/SubFixture/AbsolutePosition/Location

‘c’ will replace the current ‘z’ attribute of Fixture/SubFixture/AbsolutePosition/Location

‘d’ will replace the current ‘y’ attribute of Fixture/SubFixture/AbsolutePosition/Location
     
 -MA
    -Layers
            -Layer
                    -Fixture(single instance)[name= ,  fixture_id= ]
                            -SubFixture
                                    -AbsolutePosition
                                            -Location[x= , y= , z= ]
                                            -Rotation[x= , y= , z= ]
                    -Fixture(multi instance)[name= , fixture_id= ]
                            -AbsolutePosition
                                    -Location[x= , y= , z= ]
                                    -Rotation[x= , y= , z= ]
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