#!/bin/bash

echo "Criando ambiente"
python3 -m venv .venv

echo "Iniciando ambiente"
source .venv/bin/activate

echo "Instalando CV2"
pip install opencv-python

echo "Instalando DLIB"
echo "NEcessário instalar o CMAKE"
sudo apt-get install libboost-all-dev
sudo apt-get install build-essential cmake

pip install dlib
