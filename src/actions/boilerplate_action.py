from __future__ import annotations
from json import JSONDecodeError, loads
from typing import Dict, Optional
from ..base_action import BaseAction


class BoilerplateAction(BaseAction):

    _parameters: Dict[str, Optional[str]]

    def __init__(self, parameters: Dict[str, Optional[str]]):
        super().__init__()

        self._parameters = parameters

    def run(self):
        print("Handling action of the Boilerplate execution results...")
        ...

    @staticmethod
    def create(source: str) -> BoilerplateAction:
        try:
            return BoilerplateAction(loads(source))
        except JSONDecodeError as ex:
            raise ValueError from ex


