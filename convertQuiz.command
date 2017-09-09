#!/bin/bash
IFS=$'\n'

script_dir=$(dirname $0)
echo $script_dir
cd $script_dir

mkdir converted_files

# Get all .doc or .docx files in "to_convert" directory
for file in `find ./to_convert -name "*.doc*"`
do
    echo $file
    # Convert to .txt using textutil, pass to quizConvert.py to process
    #  and output .tsv files
    textutil -stdout -convert txt $file | python3 ./quizConvert.py "$file"
done
