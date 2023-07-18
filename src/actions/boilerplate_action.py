from __future__ import annotations
from json import JSONDecodeError, loads
from typing import Dict, Optional
from ..base_action import BaseAction
from ..utils.junitxmlParser import JunitXmlParser
from ..schemas.boilerplate_detail_schema import BoilerplateTestResult, BoilerplateDetails


class BoilerplateAction(BaseAction):
    inputs: dict
    input_data: str
    test_execution_results: BoilerplateTestResult
    junitxml_parser: JunitXmlParser

    def __init__(self, inputs):
        super().__init__(inputs)
        self.junitxml_parser = JunitXmlParser()

    def run(self):
        print("Handling action of the Boilerplate execution results...")

        if self.inputs["artifact"] != "":
            print(f"Reading artifact from {self.inputs['artifact']}...")
            self.read_artifact()
        else:
            print("Decoding base64 encoded input parameters")
            self.read_parameters()

        if self.inputs["data-type"] == "xml":
            print("Parsing junitxml data...")
            json_data = self.load_junitxml()
        elif self.inputs["data-type"] == "json":
            print("Parsing json data...")
            json_data = self.load_json()
        else:
            raise ValueError("This type is not supported")


        metadata = self.get_test_results_metadata()
        json_data.update(metadata)

        print(json_data)
        print("Validating the data...")
        self.test_execution_results = BoilerplateTestResult(**json_data)

        print("Saving results to hat endpoint...")
        # self.save_test_results_hat()

        self.output_report()


    def load_json(self) -> dict:
        try:
            return loads(self.input_data)
        except JSONDecodeError:
            raise ValueError("Invalid JSON data")

    def load_junitxml(self) -> dict:
        json_parameters = self.junitxml_parser.parse(loads(self.input_data))
        return json_parameters

    @staticmethod
    def create(inputs: dict) -> BoilerplateAction:
        try:
            return BoilerplateAction(inputs)
        except JSONDecodeError as ex:
            raise ValueError from ex