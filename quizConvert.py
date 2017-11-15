import re
import sys


def fix_none(s):
    # Converts None to empty string
    if s is None:
        return ""
    return s

# Check for correct command line arguments
if len(sys.argv) != 2:
    print("ERROR: missing filename as command line argument")
    quit()

# Use regex to extract filename without extension to use for output
file_name = re.search(r"([^/]*)\.\w+$", sys.argv[1]).group(1)

# If successful, add extension to output file name
if file_name:
    file_name = file_name + ".csv"
else:
    print("ERROR: could not parse filename")
    quit()

print(file_name)

# Create output file in converted_files folder
with open("converted_files/" + file_name, encoding = "utf-8", mode = "w") as outFile:
    # read in file to be converted from STDIN
    file = sys.stdin.read()
    # Use regex to extract all questions as match objects
    #   Word auto-lists are converted as "  •   question"
    pattern = re.compile(r"""\s* [Qq][.)]\s* (.+)\n
                             \s* [Aa•][.)\s]+ (.+)\n
                             \s* [Bb•][.)\s]+ (.+)\n
                             \s* [Cc•][.)\s]+ (.+)\n
                             \s* [Dd•][.)\s]+ (.+)\n
                             (?:\s* [Ee•][.)\s]+ (.+)\n)?
                             \s* [Aa]nswer[\s:]* (.)""", re.X)
    matches_in_document = pattern.finditer(file)
    # Iterate through matches and write to outfile as comma separated entries
    #   If there is no answer E, then that match is None
    #   will convert that to an empty string
    for question_match in matches_in_document:
        cells = []
        for x in question_match.groups():
            x = fix_none(x)
            # Excel automatically converts fractions into dates
            #  Detect fractions and add "=" in front to force excel to treat as text
            fraction = re.match("^\d+/\d+", x) 
            if fraction:
                x = "\"=\"" + x
            cells.append(x)
        outFile.write('"' + '","'.join(cells) + '"\n')
print("File Successfully Converted!\n")
