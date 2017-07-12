import re
import sys

# Check for correct command line arguments
if len(sys.argv) != 2:
    print("ERROR: missing filename as command line argument")
    quit()

# Use regex to extract filename without extension to use for output
file_name = re.search(r"([^/]*)\.\w+$", sys.argv[1])

# If successful, add extension to output file name
if file_name:
    file_name = file_name[1] + ".tsv"
else:
    print("ERROR: could not parse filename")
    quit()

print(file_name)

# Open file in converted_files folder
with open("converted_files/" + file_name, "w") as outFile:
    for line in sys.stdin:
        # Attempt to match line as either a question, answer option, or correct answer
        matchQuestion = re.search("Q. (.+)", line)
        matchOption = re.match("[ABCDabcd][).]\s+(.+)", line)
        matchAnswer = re.match("Answer:\s+(.)", line)
        # Write matched line to file
        #  questions and options get a tab
        #  answers come last on the line and get a newline
        if matchQuestion:
            outFile.write('"' + matchQuestion[1] + '"\t')
        elif matchOption:
            outFile.write('"' + matchOption[1] + '"\t')
        elif matchAnswer:
            outFile.write('"' + matchAnswer[1] + '"\n')

print("File Successfully Converted!\n")
