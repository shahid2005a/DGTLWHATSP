#!/bin/bash

echo "===== Termux Setup Start ====="

echo "===== Update kar raha hai ====="
pkg update -y && pkg upgrade -y

echo "===== Packages install kar raha hai ====="
pkg install python git cloudflared python-pip unzip wget php curl openssh -y

echo "===== Python libraries install kar raha hai ====="
pip install flask colorama requests

echo "===== Repo clone kar raha hai ====="
git clone https://github.com/shahid2005a/DGTLWHATSP.git

echo "===== Folder me ja raha hai ====="
cd DGTLWHATSP || { echo "Folder nahi mila!"; exit 1; }

echo "===== static.zip unzip kar raha hai ====="
unzip -o static.zip

echo "===== Script run kar raha hai ====="
python main.py