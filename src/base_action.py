from abc import ABCMeta, abstractmethod
from os import environ


class BaseAction(metaclass=ABCMeta):
    test_execution_results: str
    inputs: dict
    def __init__(self, inputs):
        self.inputs = inputs

    @abstractmethod
    def run(self):
        ...

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

    def save_test_results_artifact(self):
        ...
