from __future__ import annotations
from json import JSONDecodeError, loads
from typing import Dict, Optional
from ..base_action import BaseAction


class BoilerplateAction(BaseAction):

    test_execution_results: str
    inputs: dict

    def __init__(self, inputs):
        super().__init__(inputs)

    def run(self):
        print("Handling action of the Boilerplate execution results...")
        ...

    @staticmethod
    def create(source: str) -> BoilerplateAction:
        try:
            return BoilerplateAction(loads(source))
        except JSONDecodeError as ex:
            raise ValueError from ex


