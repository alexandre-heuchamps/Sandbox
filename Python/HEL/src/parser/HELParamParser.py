from FileParamParser import FileParamParser



class HELParamParser(FileParamParser):
    """ Class for parsing params files for HEL """

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)