#!/bin/bash
IFS=$'\n'

script_dir=$(dirname $0)
echo $script_dir
cd $script_dir

for file in `find ./ -name "*.doc"`
do                    
    echo $file
    textutil -convert txt $file
    file_text=${file%.doc}.txt
    echo $file_text
    python3 quizConvert.py $file_text
    rm $file_text
done