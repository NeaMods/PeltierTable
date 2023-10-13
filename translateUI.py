# AUTOTRANSLATE the ui file for PySide
import subprocess
import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.Loader)

print(cfg["translateUI"]["ui_file"])

ui_file = cfg["translateUI"]["ui_file"]
py_file = cfg["translateUI"]["py_file"]
uic_file = cfg["translateUI"]["uic_file"]

# Run pyside2-uic command to generate the Python module from the UI file
try:
    subprocess.run([uic_file, ui_file, '-g', 'python', '-o', py_file])
except:
    print("There was a problem with translating the GUI.")