#! /bin/bash
cd ~/
cd ~/django/ccbd/static/
python gen.py $1
cp out trillion/SourceCode
cp out CCBD/
mv out multicore/	
