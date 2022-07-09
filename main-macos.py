import os
import shutil
import json
from termcolor import colored
import colorama
import getpass

config = []
colorama.init()

print("Loading Config...")

with open('config-macos.json') as i:
    config = json.load(i)

print(f"Loaded Config ({len(config)} items)")
print(f"\nNow detecting files...")



#os.rename()
files = []
for r, d, f in os.walk("./mods"):
    for file in f:
        if '.jar' in file:
            files.append(os.path.join(r, file))
            print(colored(f"[SUCCESS] Detected {file}","green"))
        else:
            print(colored(f"[ERROR] {file} is not a mod! All mods must be a java file (.jar)","red"))

if files == []:
    print(colored(f"[WARN] No mods found in the mods folder. (Program Exited)","yellow"))
    exit

print(f"Detected {len(files)} files!")
print("Copying files...\n")

success = []
fail = []
for file in files:
    try:
        fl = file.split('./mods')
        fl = "".join(fl)
        os.rename(file,f"/Users/{getpass.getuser()}/Library/Application Support/minecraft/mods/{fl}")
        print(colored(f"[SUCCESS] Copied {fl} over","green"))
        success.append(fl)
    except:
        fl = file.split('./mods')
        fl = "".join(fl)
        print(colored(f"[ERROR] Failed to copy {fl}","red"))
        
        fail.append(fl)


    

print(f"\nFinished!\n\nCopied {len(success)} files\nFailed on {len(fail)} files")
    


