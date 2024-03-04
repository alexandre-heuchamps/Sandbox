import os
import subprocess
import sys

try:
    import pandas as pd
except:
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')

    # upgrade pip
    subprocess.call([python_exe, "-m", "ensurepip"])
    subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

    # install required packages
    subprocess.call([python_exe, "-m", "pip", "install", "pandas"])


class ExcelParser():
    """ Defines a class to parse an input excel file """

    __file_extensions = (".xls", ".xlsx", ".xlsm", ".xlsb", ".odf", ".ods", ".odt")

    def __init__(self,
                 file: str = "./Effectors.xlsx",
                 sys_tech: str = "HEL",
                 sys_model: str = "HELMA-P") -> None:
        self._file = file
        self._sys_tech = sys_tech
        self._sys_model = sys_model

    # ==========================================================================
    @classmethod
    def get_file_extensions(cls) -> list:
        return cls.__file_extensions
    # ==========================================================================

    # ==========================================================================
    @property
    def file(self) -> str:
        """ Get the excel file containing relevant data

        Parameters
        ----------
        None

        Returns
        -------
        self._file : str
            The file containing the data """
        return self._file

    @file.setter
    def file(self, file: str) -> None:
        """ Set the excel file containing relevant data

        Parameters
        ----------
        file : str
            The file containing the data

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the input file has the wrong format """
        if not file.endswith(self.get_file_extensions()):
            raise ValueError(f"Invalid file type. Can only be extensions {self.get_file_extensions()}")
        else:
            self._file = file

    @file.deleter
    def file(self) -> None:
        """ Delete the excel file containing relevant data """
        del self._file
    # ==========================================================================

    # ==========================================================================
    @property
    def sys_tech(self) -> str:
        """ Get the technology to consider

        Parameters
        ----------
        None

        Returns
        -------
        self._sys_tech : str
            The technology considered """
        return self._sys_tech

    @sys_tech.setter
    def sys_tech(self, sys_tech: str) -> None:
        """ Set the system technology to consider

        Parameters
        ----------
        sys_tech : str
            The system technology

        Returns
        -------
        None """
        self._sys_tech = sys_tech

    @sys_tech.deleter
    def sys_tech(self) -> None:
        """ Delete the system technology """
        del self._sys_tech
    # ==========================================================================

    # ==========================================================================
    @property
    def sys_model(self) -> str:
        """ Get the model to consider

        Parameters
        ----------
        None

        Returns
        -------
        self._sys_model : str
            The model considered """
        return self._sys_model

    @sys_model.setter
    def sys_model(self, sys_model: str) -> None:
        """ Set the system model to consider

        Parameters
        ----------
        sys_model : str
            The system model

        Returns
        -------
        None """
        self._sys_model = sys_model

    @sys_model.deleter
    def sys_model(self) -> None:
        """ Delete the system model """
        del self._sys_model
    # ==========================================================================

    # ==========================================================================
    @property
    def all_data(self) -> dict:
        """ Get dataframes containing the various data

        Parameters
        ----------
        None

        Returns
        -------
        dfs : dict
            The various data contained in the file """
        all_data = pd.ExcelFile(self.file)
        data_sheets = all_data.sheet_names
        return pd.read_excel(all_data, sheet_name = data_sheets)
    # ==========================================================================

    # ==========================================================================
    @property
    def get_data(self) -> dict:
        """ Get the  data for the particular system of interest

        Parameters
        ----------
        None

        Returns
        -------
        dfs[self.sys_tech].iloc[indices] : pandas.core.frame.DataFrame
            The dataframe contained the data of the requested system """
        dfs = self.all_data
        indices = dfs[self.sys_tech][dfs[self.sys_tech].apply(lambda row: row.astype(str).str.contains(f"{self.sys_model}").any(), axis=1)].index.tolist()
        return dfs[self.sys_tech].iloc[indices]
    # ==========================================================================

    # ==========================================================================
    @property
    def get_value(self, field: str = "Beam Power [kW]"):
        """ Get the value of a particular field

        Parameters
        ----------
        field : str (default: 'Beam Power [kW]')

        Returns
        -------
        data[field].values : numpy.ndarray
            The value of the particular field required """
        data = self.get_data
        return data[field].values
    # ==========================================================================