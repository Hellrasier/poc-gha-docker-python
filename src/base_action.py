from abc import ABCMeta, abstractmethod


class BaseAction(metaclass=ABCMeta):

    def __init__(self):
        ...

    @abstractmethod
    def run(self):
        ...
