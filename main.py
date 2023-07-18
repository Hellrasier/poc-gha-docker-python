from os import environ
from src import ActionFactory, InputsType


_PREFIX = "INPUT_HAT-"


def main():

    inputs: InputsType = {name.replace(_PREFIX, "").lower(): value for name, value in environ.items()}

    # print("The input parameters: ", inputs)


    try:
        handler = ActionFactory.create(inputs)
        handler.run()
    except ValueError as ex:
        print("Something goes wrong...")


if __name__ == "__main__":
    main()

