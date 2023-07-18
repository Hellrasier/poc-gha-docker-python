from abc import ABCMeta, abstractmethod
from os import environ
from base64 import b64decode
import json
from .schemas.test_execution_base_schema import BaseTestExecutionResult

class BaseAction(metaclass=ABCMeta):
    input_data: str
    test_execution_results: BaseTestExecutionResult
    inputs: dict
    metadata: dict
    def __init__(self, inputs):
        self.inputs = inputs


    @abstractmethod
    def run(self):
        ...

    def get_test_results_metadata(self):
        metadata = dict()
        metadata["githubProps"] = {
            "name": environ.get("GITHUB_REPOSITORY"),
            "commit": environ.get("GITHUB_SHA"),
            "branch": environ.get("GITHUB_REF_NAME")
        }
        metadata["application"] = environ.get("GITHUB_REPOSITORY")
        metadata["capabilities"] = \
            self.inputs["environment"] if self.inputs["environment"] != "" else environ.get("GITHUB_REF_NAME")
        metadata["platform"] = self.inputs["platform"]
        return metadata
    def read_artifact(self):
        path = self.inputs["artifact"]
        try:
            with open(path, 'r') as file:
                self.input_data = file.read()
        except IOError:
            raise FileNotFoundError(f"Could not read file at {path}")

    def read_parameters(self):
        bytes = b64decode(self.input["parameters"])
        self.input_data = bytes.decode('utf-8')

    def save_test_results_hat(self):
        headers = {
            'Content-Type': 'application/json',
            'github-action-token': environ.get("GITHUB_ACTION_TOKEN")
        }

        print("data", self.test_execution_results)

        response = requests.post(API_URL, data=self.test_execution_results.json(), headers=headers)

        if response.status_code != 200:
            raise Exception(f"Request failed: {response.text}")

        print('Status code:', response.status_code)
        print('Response:', response.text)

    def output_report(self):
        print(f"::set-output name=reports::{self.test_execution_results.dict()}")
