  import re
import sys

inFile = sys.argv[1]
outFile = re.match("(.+).txt$", inFile)

if (inFile and outFile):
    outFile = outFile[1] + ".tsv"
    
if (outFile != None):
    w = open(outFile, 'w', encoding ='utf-16')
    r = open(inFile, 'r', encoding='utf-8')
    for line in r:
        matchQuestion = re.search("Q. (.+)", line)
        matchOption = re.match("[ABCDabcd][).]\s+(.+)", line)
        matchAnswer = re.match("Answer:\s+(.)", line)
        if matchQuestion:
            w.write('"' + matchQuestion[1] + '"\t')
        elif matchOption:
            w.write('"' + matchOption[1] + '"\t')
        elif matchAnswer:
            w.write('"' + matchAnswer[1] + '"\n')
print("File Successfully Converted!\n")
