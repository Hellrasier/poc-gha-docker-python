from abc import ABCMeta, abstractmethod


class BaseAction(metaclass=ABCMeta):

    def __init__(self):
        ...

    @abstractmethod
    def run(self):
        ...

    def save_test_results(self):
        headers = {
            'Content-Type': 'application/json',
            'github-action-token': TOKEN
        }

        print("data", input)

        response = requests.post(API_URL, data=input, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Request failed: {response.text}")

        print('Status code:', response.status_code)
        print('Response:', response.text)
