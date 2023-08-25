#sorts the words in a file and writes a new file with sorted words

import sys

try:

    readfilename = input("Enter the name of the file you'd like to sort: ")

    words = open(readfilename, 'r')

    wordsort = []

    for line in words:
    
        wordsort.append(line)
    
    wordsort.sort()
    
    writefilename = input("Enter the name of the file you'd like to write to: ")
    
    with open(writefilename, 'wt') as output_file:
            
        output_file.writelines(wordsort)
        
except IOError as error:
    
    message = 'Error: {}' .format(error)
    
    sys.exit(message)