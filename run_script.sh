#!/usr/bin/env bash
set -e
cd /Users/jiazhenghao/CodingProjects/linkedin-auto-connect
conda activate web-scrape
python3 main.py --delay 2000 --max-connection 100
