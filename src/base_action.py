from abc import ABCMeta, abstractmethod
from os import environ


class BaseAction(metaclass=ABCMeta):
    parameters: str
    test_execution_results: str
    inputs: dict
    metadata: dict
    def __init__(self, inputs):
        self.inputs = inputs
        self.parameters = inputs["parameters"]

    @abstractmethod
    def run(self):
        ...

    def get_test_results_meta(self):
        self.metadata["githubProps"] = {
            "name": environ.get("GITHUB_REPOSITORY"),
            "commit": environ.get("GITHUB_SHA"),
            "branch": environ.get("GITHUB_REF_NAME")
        }
        self.metadata["application"] = environ.get("GITHUB_REPOSITORY")
        self.metadata["capabilities"] = \
            self.inputs["environment"] if self.inputs["environment"] != "" else environ.get("GITHUB_REF_NAME")
        self.metadata["platform"] = self.inputs["platform"]

    def read_artifact(self):
        try:
            with open(self.inputs["artifact"], 'r') as file:
                self.parameters = file.read()
        except IOError:
            raise FileNotFoundError(f"Could not read file at {path}")

    def save_test_results_hat(self):
        headers = {
            'Content-Type': 'application/json',
            'github-action-token': environ.get("GITHUB_ACTION_TOKEN")
        }

        print("data", self.test_execution_results)

        response = requests.post(API_URL, data=self.test_execution_results, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Request failed: {response.text}")

        print('Status code:', response.status_code)
        print('Response:', response.text)

    def output_report(self):
        print(f"::set-output name=reports::{self.test_execution_results}")
