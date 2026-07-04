#!/usr/bin/env python3
"""Module that serialize and deserialize with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML"""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML to a dictionary"""

    tree = ET.parse(filename)
    root = tree.getroot()

    return {child.tag: child.text for child in root}
