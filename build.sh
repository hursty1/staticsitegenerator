#!/bin/bash

python3 src/main.py "/hursty1/"
cd docs && python3 -m http.server 8888