A simple script to convert multiple choice quizes written sequentially in word (.doc or .docx) documents into .tsv files that can easily be imported into web based quiz programs.

USAGE: Place quizes in word format in a folder within the directory containing quizConvert.py and convertQuiz.command. These two files must be in the same folder. Run convertQuiz.command to convert all .doc/.docx into .tsv format in a newly created converted_files folder.


FILES:

#######
quizConvert.py:
	Arguments: file name of the .doc or .docx file being converted
	STDIN: receives text of converted file via STDIN. Pipe output of textutil into the script
	Outputs: generates a .tsv file with the same name as the original file in converted_files/

Python script that accepts a .txt file from STDIN with quiz questions and answers. It parses it using regex and writes the question in .tsv format to a outfile

#######
convertQuiz.command:

A bash script that finds all .doc or .docx files in the current directory and subdirectories,
converts them to .txt files with textutil,
and runs quizConvert.py on them, converting them into .tsv files in a converted_files directory
