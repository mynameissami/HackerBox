import os
dir1 = [f for f in os.listdir('.')]
if "Settings.ini" in dir1:
     os.remove("Settings.ini")