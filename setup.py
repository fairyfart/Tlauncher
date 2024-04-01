from urllib.request import urlretrieve
import json
import os
import time


def space():
    os.system("")

def clear_output():
    os.system("clear")

def logo_outputer():
    clear_output()
    space()
    with open("Logo.json", "r") as json_file:
        ascii_art_data = json.load(json_file)
        ascii_art = ascii_art_data["ascii_art"]
        print(ascii_art)
        space()

def install():
    url_package = "https://tlauncher.org/jar"
    filename = "TLauncher-2.899.zip"
    urlretrieve(url_package, filename)

def unzip():
    os.system("unzip TLauncher-2.899.zip")

def delete():
    os.system("rm -f TLauncher-2.899.zip")
    os.system("rm -f README-EN.txt")
    os.system("rm -f README-RUS.txt")

def rename():
    old_file_name = "TLauncher-2.899.jar"
    new_file_name = "TLauncher-2.86.jar"
    if os.path.exists(old_file_name):
        os.rename(old_file_name, new_file_name)

logo_outputer()

print("  This Program Going To Download Tlauncher.")


time.sleep(1)
get_request = input("   Do You Wanna Continue Downloading? [Y/n]: ")

minefile = "TLauncher-2.86.jar"


if get_request == "n":
    space()
    clear_output(), print("  Program Closed, By The User.")
    space()
    exit()

if os.path.exists(minefile):
    clear_output()
    logo_outputer()
    print("   Minecraft Already Exists.\n  It can Be run by Opening 'The main.sh' file.")
    exit()


if get_request.lower() == "y":
    try:    
        install()
        clear_output()
        logo_outputer()
        unzip()
        delete()
        rename()
        space()
        
        
        if_wants = input(" Do You Wanna Run The Minecraft? [Y/n]: ")
        if if_wants.lower() == "y":
            space()
            
            os.system("chmod +x main.sh")
            os.system("./main.sh")
            space()
            space()
            time.sleep(1)
        elif if_wants.lower() == "n":
            clear_output()
            logo_outputer()

    except FileNotFoundError:
        clear_output()
        logo_outputer()
        space()
        print("  Installation Failed. (Cannot Find The File.)")
        space()
        time.sleep(0.9)
else:
    space()


if get_request.lower() == "n":
    time.sleep(0.8)
    clear_output()
