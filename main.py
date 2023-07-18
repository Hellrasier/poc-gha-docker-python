from os import environ
from src import ActionFactory, InputsType


_PREFIX = "INPUT_HAT-"


def main():

    inputs: InputsType = \
        tuple(
            (name.replace(_PREFIX, "").lower(), environ.get(name), )
            for name in environ
            if name.startswith(_PREFIX) and environ.get(name) != ""
        )

    print("The input parameters: ", tuple(name for name, _ in inputs))

    try:
        handler = ActionFactory.create(inputs)
        handler.run()
    except ValueError as ex:
        print("Something goes wrong...")


if __name__ == "__main__":
    main()

