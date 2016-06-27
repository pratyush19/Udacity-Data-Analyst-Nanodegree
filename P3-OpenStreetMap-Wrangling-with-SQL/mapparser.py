"""
Parse the OSM file and count the numbers of unique tag
"""

import xml.etree.cElementTree as ET
import pprint


OSMFILE = "ahmedabad_india.osm"

def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags: 
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags
    
pprint.pprint(count_tags(OSMFILE))
