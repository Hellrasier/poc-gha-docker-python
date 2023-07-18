import src.actions
from inspect import signature, getmembers, isclass, getfile
from typing import TypeVar, Tuple, Optional
from .base_action import BaseAction

A = TypeVar("A", bound=BaseAction)

Inputs = Tuple[Tuple[str, Optional[str]]]


class ActionFactory:
    """
    Factory class for creating actions.

    The instantiated action based on the correspondence of the GHA input parameter names and the action class constructor signature..
    """

    @staticmethod
    def create(inputs: Inputs) -> A:
        """
        Creates and returns an action instance.

        The action is initialized with the attributes of the factory.

        Args:
            inputs (Inputs): The collection of name/value GHA input parameters.

        Returns:
            A: The action instance.

        Raises:
            ValueError: If action class haven't been found.
        """

        action = None

        for cls in [cls for name, cls in getmembers(src.actions, isclass)]:
            platform = getfile(cls).replace("/action/src/actions/", "").replace("_action.py", "")
            print(platform)
            print(inputs["platform"])
            if inputs["platform"] == platform:
                action = cls(inputs)

        if not isinstance(action, BaseAction):
            raise ValueError

        return action

