from .FilePropagParser import FilePropagParser



class DronePropagParser(FilePropagParser):
    """ Class for parsing propagation files for drone """

    def __init__(self, file: str) -> None:
        self._file: str = file