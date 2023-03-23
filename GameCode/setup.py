import cx_Freeze

executables = [cx_Freeze.Executable("mainGame.py")]

build_exe_options = {
"excludes": ["tkinter", "unittest"],
"zip_include_packages": ["encodings", "PySide6"],
"include_files":["attacks.py","enemy.py","player.py","mapGen.py","classes.py","levelGen.py","Assets/"],
}


cx_Freeze.setup(
    name="Escape 3008",
    options={"build_exe": {"packages":["pygame","os"],
                           "build_exe":build_exe_options,}},
    executables = executables

    )