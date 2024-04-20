from FilePropagParser import FilePropagParser



class HELPropagParser(FilePropagParser):
    """ Class for parsing propagation files for HEL """

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)