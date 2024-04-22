from src.body.World import World
from src.body.HEL import HEL
from src.body.Drone import Drone



class ConsistencyCheckerWorld:
    """ A class to check if sheet names are consistent with names in column """

    def __init__(self,
                    names_sheets: list[str],
                    names_col: list[str],
                ) -> None:
        self._names_sheets: list[str] = names_sheets
        self._names_col: list[str] = names_col

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





if __name__ == "__main__":
    pass