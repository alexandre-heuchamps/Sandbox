from FileParser import FileParser



class FilePropagParser(FileParser):
    """ Class for parsing input param files """

    _req_kw: str = "-propag"

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)