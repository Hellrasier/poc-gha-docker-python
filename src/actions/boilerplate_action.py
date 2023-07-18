from __future__ import annotations
from json import JSONDecodeError, loads
from typing import Dict, Optional
from ..base_action import BaseAction
from ..utils.junitxmlParser import JunitXmlParser


class BoilerplateAction(BaseAction):
    parameters: str
    test_execution_results: str
    inputs: dict
    junitxml_parser: JunitXmlParser

    def __init__(self, inputs):
        super().__init__(inputs)
        self.junitxml_parser = JunitXmlParser()

    def run(self):

        print("Handling action of the Boilerplate execution results...")

        if self.inputs["artifact"] != "":
            print(f"Reading artifact from {self.inputs['artifact']}...")
            self.read_artifact()

        if self.inputs["data-type"] == "xml":
            print("Parsing junitxml data...")
            self.load_junitxml()
        elif self.inputs["data-type"] == "json":
            print("Parsing json data...")
            self.load_json()
        else:
            raise ValueError("This type is not supported")

        metadata = self.get_test_results_metadata()

        self.test_execution_results.update(metadata)

        print("Saving results to hat endpoint...")
        # self.save_test_results_hat()

        self.output_report()

    def load_json(self):
        try:
            return loads(self.input_data)
        except JSONDecodeError:
            raise ValueError("Invalid JSON data")

    def load_junitxml(self):
        json_parameters = self.junitxml_parser.parse(self.parameters)
        for detail in json_parameters["details"]:
            testcases = []
            for testsuite in detail["testsuite"]:
                testcases.extend(testsuite["testsuite"])
            detail["testcases"] = testcases
            del detail["testsuite"]

        self.test_execution_results = json_parameters

    @staticmethod
    def create(source: str) -> BoilerplateAction:
        try:
            return BoilerplateAction(loads(source))
        except JSONDecodeError as ex:
            raise ValueError from ex