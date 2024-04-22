from .FileParamParser import FileParamParser



class HELParamParser(FileParamParser):
    """ Class for parsing params files for HEL """

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)

    # ==========================================================================
    def get_wavelengths(self) -> list[float]:
        l = super().get_column_content("wavelength")
        lmbda_list = []
        for lmbda in l:
            lmbda_list.append([float(ll) for ll in lmbda])
        return lmbda_list
    # ==========================================================================