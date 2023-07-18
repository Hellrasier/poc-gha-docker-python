from typing import List, Optional
from lxml import etree
from src.utils.removeDictField import remove_dict_field

class JunitXmlParser:
    def _collect_xml_properties(self, xml_node, output):
        properties = xml_node.find("properties")
        if properties is None:
            return {}

        properties = properties.findall("property")
        result = {}
        for property in properties:
            if property.attrib.get("type") == "array":
                values = property.attrib.get("values").replace(" ", "").split(",")
                result[property.attrib.get("name")] = values
            else:
                result.update({property.attrib.get("name"): remove_dict_field(property.attrib, "name")})
        output.update(result)

    def _collect_attribs(self, xml_node, output):
        output.update(dict(xml_node.attrib))

    def _collect_exception(self, xml_node, output, key):
        exception = xml_node.find("failure")
        if exception is not None:
            output[key] = {**dict(exception.attrib), "reason": exception.text}

    def _get_child_nodes(self, xml_node) -> Optional[List[etree.Element]]:
        child_nodes = xml_node.findall("testsuite")
        if len(child_nodes) == 0:
            child_nodes = xml_node.findall("testcase")
        return child_nodes

    def _is_test_case(self, xml_node) -> bool:
        child_nodes = self._get_child_nodes(xml_node)

        return len(child_nodes) == 0

    def _collect_details(self, xml_node, output, key):
        child_nodes = self._get_child_nodes(xml_node)

        if len(child_nodes) == 0:
            return

        output[key] = []
        for child in child_nodes:
            detail = {}
            self._collect_attribs(child, detail)
            self._collect_xml_properties(child, detail)
            self._collect_exception(child, detail, "exceptionProps")
            self._collect_details(child, detail, child.tag)
            if self._is_test_case(child):
                detail["status"] = "passed" if detail.get("exceptionProps") is None else "failed"
            output[key].append(detail)

    def _remove_xml_declaration(self, xml_data: str) -> str:
        return xml_data.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')

    def parse(self, xml):
        xml_data = etree.fromstring(self._remove_xml_declaration(xml))

        json_result = {}

        general_node = xml_data.find("testsuite")

        self._collect_attribs(general_node, json_result)
        self._collect_xml_properties(general_node, json_result)

        self._collect_details(general_node, json_result, "details")

        return json_result