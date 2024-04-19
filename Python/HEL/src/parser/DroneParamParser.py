from FileParamParser import FileParamParser



class DroneParamParser(FileParamParser):
    """ Class for parsing params files for drone """

    def __init__(self, file: str) -> None:
        self._file: str = file