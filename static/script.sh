#! /bin/bash
cd ~/
cd ~/cloaked-octo-lana/static/
python gen.py $1
cp q.txt trillion/SourceCode
cp q.txt CCBD/
mv q.txt multicore/	
