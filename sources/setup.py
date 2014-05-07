import sys
from cx_Freeze import setup, Executable

product_name = "Triangulation"

exe = Executable(
    script = "main.py",
    base = "Win32GUI",
    targetName = "Triangulation.exe",
    icon = "icon.ico",
    shortcutName = "Triangulation",
    shortcutDir = "ProgramMenuFolder"
    )
	
build_exe_options = {"packages": ["os"], 
					 "excludes": ["tkinter"],
					 "include_files": ["icon.ico"]
					}
					
bdist_msi_options = {"upgrade_code": "{66620F3A-DC3A-11E2-B341-002219E9B01E}",
					 "add_to_path": False,
					 "initial_target_dir": r"[ProgramFilesFolder]\%s" % (product_name),
					}

setup(
    version = "0.3",
    description = "ear-clipping triangulation of flat polygons",
    author = "Yannick Augenstein",
    author_email = "yannick.augenstein@student.kit.edu",
    name = "Triangulation",
	executables = [exe],
    options = 	{"build_exe": build_exe_options, 
				 "bdist_msi": bdist_msi_options
				}
    )