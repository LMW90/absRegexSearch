#! python3
# opens all .txt files in a folder and searches for lines matching user supplied regex, prints out result
# required libraries
import re
import os
# ask for directory to search
while True:
    dirName = input('Enter absolute path to a directiory, press enter to use cwd:\n')
    if dirName == '':
        dirName = os.getcwd()
        break
    elif os.path.exists(dirName) and os.path.isdir(dirName):
        break

print('Searching directory:', dirName)
# user inputs regex to match
searchInput = input('Enter a regular expression to search for:\n')
# create regexs object ; r'{}'.format(string) returns string as a raw string
extRE = re.compile(r'.*\.txt$')
searchRE = re.compile(r'{}'.format(searchInput))
# list files in directory
fileList = os.listdir(dirName)
print('Files in directory {dirname}:\n', fileList)
# lists to store names of .txt files and results (matching lines)
txtFiles = []
results = []
# find text files
for file in fileList:
    txtFiles += extRE.findall(file)
print('Found .txt files:\n', txtFiles)
print(f'Searching files for {searchRE}')
# open each file and search lines for match
for file in txtFiles:
    with open(file) as currentFile:
        for line in currentFile:
            if searchRE.match(line):
                # if line matches add to result list with newline removed
                results.append(line.rstrip('\n'))
# handling no matches
if results == []:
    print('No matches found')
# print out results
else:
    print('Found lines:')
    for result in results:
        print(result)
