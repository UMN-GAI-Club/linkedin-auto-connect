#!/usr/bin/env bash
set -e
cd /Users/jiazhenghao/CodingProjects/linkedin-auto-connect
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py --delay 2000 --max-connection 50
