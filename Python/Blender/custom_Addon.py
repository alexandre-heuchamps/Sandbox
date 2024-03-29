import bpy
import sys
import subprocess
import os
from . import *

try:
    import pandas as pd
    from ExcelParser import ExcelParser
except:
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')

    # upgrade pip
    subprocess.call([python_exe, "-m", "ensurepip"])
    subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

    # install required packages
    subprocess.call([python_exe, "-m", "pip", "install", "pandas"])

if __name__ == "__main__":
    p = ExcelParser()
    print(p.file)