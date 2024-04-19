from FileParamParser import FileParamParser



class HELParamParser(FileParamParser):
    """ Class for parsing params files for HEL """

    def __init__(self, file: str) -> None:
        self._file: str = file