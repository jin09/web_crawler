import sys
from cx_Freeze import setup, Executable

setup( name = "Any Name", 
version = "3.1", 
description = "can reboot the router automatically using the browser API",
 executables = [Executable("extractinglinks.py", base = "Win32GUI")])
