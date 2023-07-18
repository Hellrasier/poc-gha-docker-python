from __future__ import annotations
from os import path
from typing import Final
from ..base_action import BaseAction


_WORKSPACE_DIR: Final[str] = "/github/workspace"


class PHPUnitAction(BaseAction):

    _report_path: str

    def __init__(self, artifact: str):
        super().__init__()

        self._report_path = f"{_WORKSPACE_DIR}/{artifact}"

    def run(self):
        if not path.exists(self._report_path):
            raise ValueError

        print("Handling action of the PHPUnit execution results...")
        with open(self._report_path, "r") as file:
            print(file.read())




