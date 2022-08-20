import os
currdir = os.getcwd()

class commands():
    def ls():
        from datetime import datetime
        import os

        from progressbar import FormatCustomText

        filelist = []
        # This lists the current directory '.' <- is specified for current dir.
        dir1 = os.listdir('.')
        dir_org = [f for f in dir1]  # This will organize the files
        # prints the text "Date of creation\t   Folders"
        print("Time Created\tDate when created\t\tLast modified\tSize\t Directory Files")
        for f in dir_org:
            if os.path.isdir(f) == True:
                cretation_time = os.path.getctime(f)
                last_modified = os.path.getmtime(f)
                get_bites = os.path.getsize(f)
                Format_creationtime = datetime.fromtimestamp(
                    cretation_time).strftime("%H.%M %p")
                Format_lastmodified = datetime.fromtimestamp(
                    last_modified).strftime("%H.%M %p")
                Format_creationtime2 = datetime.fromtimestamp(cretation_time)
                filelist.append(f)
                for f in filelist:
                    global byte_dir
                    byte_dir = os.path.getsize(f)
                print(
                    f"{Format_creationtime}\t{Format_creationtime2}\t{Format_lastmodified}\t{byte_dir}\t ./{f}")
            if os.path.isfile(f) == True:
                cretation_time = os.path.getctime(f)
                last_modified = os.path.getmtime(f)
                get_bites = os.path.getsize(f)
                Format_creationtime = datetime.fromtimestamp(
                    cretation_time).strftime("%H.%M %p")
                Format_lastmodified = datetime.fromtimestamp(
                    last_modified).strftime("%H.%M %p")
                Format_creationtime2 = datetime.fromtimestamp(cretation_time)
                filelist.append(f)
                for f in filelist:
                    global byte_dir2
                    byte_dir2 = os.path.getsize(f)
                print(
                    f"{Format_creationtime}\t{Format_creationtime2}\t{Format_lastmodified}\t{byte_dir2}\t {f}")

    def clear():
      try:  
        os.system("clear")
      except:
          pass
      finally:
          os.system("cls")
    def cd(dir1):
        os.chdir(dir1)
if __name__ == "__main__":
    while True:
     try: 
        askdir = input(f"HB {currdir}> ")
        if askdir =="ls":
            commands.ls()
        elif askdir =="cls":
            commands.clear()
        elif askdir == "cd":
            pass
     except:
         pass   