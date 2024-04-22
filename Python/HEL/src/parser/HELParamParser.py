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
            lambda_list.append([float(l) for l in lmbda])
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

    # ==========================================================================
    def get_Js(self) -> list[float]:
        Js = super().get_column_content("J")
        J_list = []
        for J in Js:
            J_list.append([float(j) for j in J])
        return J_list
    # ==========================================================================

    # ==========================================================================
    def get_w0s(self) -> list[float]:
        w0s = super().get_column_content("w0")
        w0_list = []
        for w0 in w0s:
            w0_list.append([float(j) for j in w0])
        return w0_list
    # ==========================================================================

    # ==========================================================================
    def get_r0s(self) -> list[float]:
        r0s = super().get_column_content("r0")
        r0_list = []
        for r0 in r0s:
            r0_list.append([float(j) for j in r0])
        return r0_list
    # ==========================================================================