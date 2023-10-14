# AUTOTRANSLATE the ui file for PySide6 with pyside6-uic
import subprocess
import os

current_folder = os.getcwd()
ui_file = os.path.join(current_folder,'heaterApp.ui')
py_file = os.path.join(current_folder,'ui_heaterApp.py')

# Run pyside6-uic command to generate the Python module from the UI file
try:
    subprocess.run(['pyside6-uic', ui_file,'-o', py_file], check=True)
    print("GUI translated to file: ",py_file)
except:
    print("There was a problem with translating the GUI.")