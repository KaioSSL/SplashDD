import sys
from cx_Freeze import setup, Executable
import pygame


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("start.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["pygame","guerra", 'res', 'bala', 'tanque'],
        include_files = ["Imagens","Sounds","__pycache__"],
        excludes = []
)




setup(
    name = "SPLASHDD",
    version = "1.0",
    description = "Descrição do programa",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
