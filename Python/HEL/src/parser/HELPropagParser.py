from .FilePropagParser import FilePropagParser



class HELPropagParser(FilePropagParser):
    """ Class for parsing propagation files for HEL """

    def __init__(self, file: str) -> None:
        self._file: str = file