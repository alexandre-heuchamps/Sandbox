from .FileParser import FileParser



class FileParamParser(FileParser):
    """ Class for parsing input param files """

    _req_kw: str = "-param"

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)

    def get_names_in_files(self) -> list[list[str]]:
        names = []
        for df in super().get_dfs():
            for data in df:
                names.append(list(data["Name"]))
        return names