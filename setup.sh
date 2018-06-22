#!/bin/bash

# First install curl (sudo apt install curl)
# Then run with sh -c "$(curl -fsSL https://raw.github.com/AdGold/config-manager/master/setup.sh)"

sudo apt install -y git python3

sudo apt install -y zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

cd ~/Downloads
git clone https://github.com/AdGold/config-manager.git
cd config-manager
./config_manager.py config.json
