from __future__ import annotations
from json import JSONDecodeError, loads
from typing import Dict, Optional
from ..base_action import BaseAction
from ..utils.junitxmlParser import JunitXmlParser


class BoilerplateAction(BaseAction):
    parameters: str
    test_execution_results: str
    inputs: dict
    metadata: dict
    junitxmlParser: JunitXmlParser

    def __init__(self, inputs):
        super().__init__(inputs)

    def run(self):

        print("Handling action of the Boilerplate execution results...")

        if self.inputs["artifact"] != "":
            self.read_artifact()

        if self.inputs["type"] == "xml":
            self.load_junitxml()
        elif self.inputs["type"] == "json":
            self.load_json()
        else:
            raise ValueError("This type is not supported")

        self.test_execution_results.update(self.metadata)

        self.save_test_results_hat()

        self.save_test_results_artifact()

    def load_json(self):
        try:
            return loads(self.input_data)
        except JSONDecodeError:
            raise ValueError("Invalid JSON data")

    def load_junitxml(self):
        json_parameters = self.junitxml_parser.parse(self.parameters)
        print(json_parameters)


    @staticmethod
    def create(source: str) -> BoilerplateAction:
        try:
            return BoilerplateAction(loads(source))
        except JSONDecodeError as ex:
            raise ValueError from ex