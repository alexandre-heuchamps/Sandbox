from FilePropagParser import FilePropagParser



class HELPropagParser(FilePropagParser):
    """ Class for parsing propagation files for HEL """

    def __init__(self, files: list[str]) -> None:
        self._files: list[str] = files