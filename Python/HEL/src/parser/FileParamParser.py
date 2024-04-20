from .FileParser import FileParser



class FileParamParser(FileParser):
    """ Class for parsing input param files """

    _req_kw: str = "-param"

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)