import os
os.system("pyinstaller.exe -w -i gtl.ico gtl_pane.py")
path_dirs = os.listdir("./dist/gtl_pane")
if "gtl.ico" not in path_dirs:
    os.system("copy gtl.ico dist\\gtl_pane")