A simple script to convert multiple choice quizes written sequentially in word documents into .tsv files that can easily be imported into web based quiz programs.


FILES:

#######
quizConvert.py:
	Arguments: file name of a .txt file containing the quiz
	Outputs: generates a .tsv file with the same name

Python script that accepts a .txt file with quiz questions and answers. It parses it using regex and writes the question in .tsv format to a outfile

#######
convertQuiz.command:

A bash script that finds all .doc files in the current directory,
converts them to .txt using textutil,
renames them to .txt,
prints their filename to the terminal,
runs quizConvert.py on them,
and deletes the original file
