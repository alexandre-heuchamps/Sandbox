class ConsistencyCheckerNames:
    """ A class to check if sheet names are consistent with names in column """

    def __init__(self,
                    names_sheets: list[str],
                    names_col: list[str],
                ) -> None:
        self._names_sheets: list[str] = names_sheets
        self._names_col: list[str] = names_col

        if not (self.are_lengths_consistent() and self.are_names_consistency()):
            raise ValueError("Name consistency error")

    # ==========================================================================
    @property
    def names_sheets(self) -> list[str]:
        return self._names_sheets
    # ==========================================================================

    # ==========================================================================
    @property
    def names_col(self) -> list[str]:
        return self._names_col
    # ==========================================================================

    # ==========================================================================
    def are_lengths_consistent(self) -> bool:
        """ Function checking if the number of sheets match the number of names """
        return True if len(self._names_sheets) == len(self._names_col) else False
    # ==========================================================================

    # ==========================================================================
    def are_names_consistency(self) -> bool:
        if not self.are_lengths_consistent():
            raise ValueError("Name inconsistency between sheets and column names")
        else:
            snames = self._names_sheets
            cnames = self._names_col
            all_ok = all(sn == cn for sn, cn in zip(snames, cnames))
            return True if all_ok else False
    # ==========================================================================





if __name__ == "__main__":
    nsheet = ["DJI1", "R"]
    ncol = ["DJI1", "R"]
    c_check = ConsistencyCheckerNames(names_sheets = nsheet, names_col = ncol)
    print(f"Are names consistent? {c_check.are_names_consistency()}")