from prompt_toolkit.shortcuts import yes_no_dialog
from time import sleep
def installer():
     import wget
     import zipfile
     import os
     print("Beggining the process of installing Files...\n")
     wget.download("https://allpetsworld.000webhostapp.com/HackerBox/Dics/Dics.zip")
     current_dir = os.getcwd()
     current_dir23 = current_dir+"\\Dics.zip"
     with zipfile.ZipFile(current_dir23, 'r') as zip_ref:
              zip_ref.extractall()
     os.remove("Dics.zip")
     sleep(1)
     print("The Downloaded files were : Dics.zip -> Dics")
     print("The Folder contains Pre-Made Dictionaries Used in Scripts..")     
     print("The Download went Successfull.")
result = yes_no_dialog(
  title='Required Packages',
  text="This Program requires some Additional resources to run. Do you want to download them?").run()
if result == True:
    installer()
else:
    result = yes_no_dialog(
    title='Warning!',
    text="Are you sure? This could cause Errors in Scripts.").run()
    if result == True:
        pass
    else:
        installer()