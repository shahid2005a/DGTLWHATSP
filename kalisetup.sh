#!/bin/bash

echo "===== Kali Linux Setup Start ====="

echo "===== Update kar raha hai ====="
sudo apt update && sudo apt upgrade -y

echo "===== Packages install kar raha hai ====="
sudo apt install python3 python3-pip git unzip wget php curl openssh-server -y

echo "===== Python libraries install kar raha hai ====="
pip3 install flask colorama requests

echo "===== Repo clone kar raha hai ====="
git clone https://github.com/shahid2005a/DGTLWHATSP.git

echo "===== Folder me ja raha hai ====="
cd DGTLWHATSP || { echo "Folder nahi mila!"; exit 1; }

echo "===== static.zip unzip kar raha hai ====="
unzip -o static.zip

echo "===== Script run kar raha hai ====="
python3 main.py