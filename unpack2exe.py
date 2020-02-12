import os
if os.path.exists("./dist"):
    path_dirs = os.listdir("./dist")
    if "gtl.ico" not in path_dirs:
        os.system("copy gtl.ico dist\\")

os.system("pyinstaller.exe -F -w -i gtl.ico gtl_pane.py")