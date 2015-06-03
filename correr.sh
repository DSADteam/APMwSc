#!/bin/bash
python3.4 base.py createdb
for x in `ls testing`; do echo $x; python3.4 testing/$x; done
