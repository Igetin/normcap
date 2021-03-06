# Default
import os
import sys

# Extra
import PyInstaller.__main__


ARGS = [
    "--name=normcap",
    "--clean",
    "--noconfirm",
    # "--onefile",
    "--onedir",
    "--windowed",
    # "--debug=all",
    # "--log-level=DEBUG",
    f"--icon={os.path.join('ressource', 'normcap.ico')}",
    f"--paths={os.path.join('.venv', 'lib', 'python3.7', 'site-packages')}",
    "--hidden-import=PIL",
    "--hidden-import=PIL._imagingtk",
    "--hidden-import=PIL._tkinter_finder",
]

if sys.platform.lower().startswith("linux"):
    ARGS.extend(["--add-data=/etc/fonts:fonts", "--runtime-hook=rthook.py"])

if sys.platform.lower().startswith("win"):
    ARGS.extend(
        [
            "--add-data=tessdata;tessdata",
            "--runtime-hook=rthook.py",
            "--win-private-assemblies",
        ]
    )

ARGS.append(os.path.join("normcap", "__main__.py"))

PyInstaller.__main__.run(ARGS)
