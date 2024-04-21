from .FileParser import FileParser



class FileParamParser(FileParser):
    """ Class for parsing input param files """

    _req_kw: str = "-param"

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)

    def get_column_content(self, column_name: str) -> list[list[str]]:
        """ Function returning a list of list of strings corresponding to the
        data of the requested column """
        data = []
        for df in super().get_dfs():
            for d in df:
                data.append(list(d[column_name]))
        return data

    def get_names_in_files(self) -> list[list[str]]:
        """ Function returning all the names contained in the files """
        return self.get_column_content(column_name = "Name")