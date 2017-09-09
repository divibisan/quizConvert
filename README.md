A simple script to convert multiple choice quizes written sequentially in word (.doc or .docx) documents into .csv files that can easily be imported into web based quiz programs.

USAGE: Place quizes in word format in a folder called "to\_convert" within the directory containing quizConvert.py and convertQuiz.command. These two files must be in the same folder. Run convertQuiz.command to convert all .doc/.docx into .tsv format in a newly created converted\_files folder.


FILES:

#######
quizConvert.py:
	Arguments: file name of the .doc or .docx file being converted
	STDIN: receives text of converted file via STDIN. Pipe output of textutil into the script
	Outputs: generates a .csv file with the same name as the original file in converted\_files/

Python script that accepts a .txt file from STDIN with quiz questions and answers. It parses it using regex and writes the questions and answers in .csv format to a outfile

Only questions beginning with a Q or q are copied.
Each question, answer choice, and answer must be on separate consecutive lines, though content before or after doesn't matter
Questions can have 4 or 5 answers which begin wiht the letters A - D/E, or a bullet • (which is what is generated from a word auto-list)
Answers must begin with "Answer" or "answer"

#######
convertQuiz.command:

A bash script that finds all .doc or .docx files in the "to\_convert" directory,
converts them to .txt files with textutil,
and runs quizConvert.py on them, converting them into .csv files in a converted\_files directory
