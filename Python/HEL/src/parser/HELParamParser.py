from .FileParamParser import FileParamParser



class HELParamParser(FileParamParser):
    """ Class for parsing params files for HEL """

    def __init__(self, files: list[str]) -> None:
        super().__init__(files = files)

    # ==========================================================================
    def get_wavelengths(self) -> list[float]:
        lambdas = super().get_column_content("wavelength")
        lambda_list = []
        for lmbda in lambdas:
            lambda_list.append([float(ll) for ll in lmbda])
        return lambda_list
    # ==========================================================================

    # ==========================================================================
    def get_Ps(self) -> list[float]:
        Ps = super().get_column_content("Power")
        P_list = []
        for P in Ps:
            P_list.append([float(p) for p in P])
        return P_list
    # ==========================================================================

    # ==========================================================================
    def get_M2s(self) -> list[float]:
        M2s = super().get_column_content("Power")
        M2_list = []
        for M2 in M2s:
            M2_list.append([float(m2) for m2 in M2])
        return M2_list
    # ==========================================================================