 ## install tensorflow to anaconda
print("Are you running anacocnda? Y/N")
print("Scanning system for anaconda...")
import os
import sys
import subprocess
import time
import shutil
import requests
import json
import re
import random
import string
import numpy as np
## Design A UX to check if the user wants to install miniforge, anaconda,transformers, gradio and huggingface
def install_miniforge():
    print("Do you want to install miniforge? Y/N")
    miniforge = input()
    if miniforge == "Y":
        print("installing miniforge")
        subprocess.call(["curl", "-L","", "-o", "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh"])
        subprocess.call(["bash", "Miniforge3-MacOSX-arm64.sh"])
        subprocess.call(["curl", "-L","", "-o", ""], shell=True)
        subprocess.call(["bash", "Miniforge3-MacOSX-arm64.sh"])
        ## install Miniforge3-MacOSX-arm64.sh""
        ## prompt the ai to install brew and miniforge using the terminal
        ## install miniforge
        os.call = ("brew", "install", "miniforge")
        print("Done.")
    else:
        print("You chose not to install miniforge")
        print("Continuing...")
        os.sys.exit()

        print(install_miniforge())