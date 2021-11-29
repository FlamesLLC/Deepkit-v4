 ## install tensorflow to anaconda
print("Are you running anacocnda? Y/N")
answer = input()
if answer == "Y":
    print("Installing Tensorflow")
    import os
    os.system("conda install tensorflow")
    print("Tensorflow installed")
    ## installl miniforge through pip3 
    print("Installing miniforge")
    import os
import sys 
## import brew to mac terminal
if sys.platform == "darwin":
    ruby = os.environ.get('RUBY')
    ##i stall brew through ruby
    os.system("ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
# install miniforge with ruby
    os.system("ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/cask/cask/master/go)\"")

    os.system("brew install miniforge")
    os.system("miniforge install tensorflow")
    os.system("miniforge install opencv")
else:
    print("Please install Tensorflow to anaconda")
    print("Exiting")
    exit()
    