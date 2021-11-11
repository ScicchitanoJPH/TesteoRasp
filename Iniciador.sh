#!/bin/bash

sudo apt update
cd Desktop
cd Codigos
sudo pigpiod
sudo chmod -R 777 ./
python TesteoRasp.py
echo "script ejecutado - $(date)" >> /home/test/Documentos/log-script.txt

exit
