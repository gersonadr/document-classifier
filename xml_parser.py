import xml.etree.ElementTree as ET


def get_fields_from_xml(xml_string):
    data = xml_string.replace("\\n", "").replace("\\t", "")

    # parse the XML string
    root = ET.fromstring(data)

    # Define the namespace
    ns = {"alto": "http://www.loc.gov/standards/alto/ns-v3#"}

    # Find all the String elements
    strings = root.findall(".//alto:String", ns)

    # Extract the required fields from each String element and store them in a list
    fields = []
    for string in strings:
        field = {
            "x": int(string.attrib["HPOS"]),
            "y": int(string.attrib["VPOS"]),
            "w": int(string.attrib["WIDTH"]),
            "h": int(string.attrib["HEIGHT"]),
            "confidence": float(string.attrib["WC"]),
            "text": string.attrib["CONTENT"],
        }
        fields.append(field)

    return fields
