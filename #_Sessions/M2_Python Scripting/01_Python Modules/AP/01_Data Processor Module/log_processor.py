"""
Create a file named log_processor.py containing three separate functions:

One that returns the total number of lines in a file.
One that returns the total number of words.
One that returns the total number of characters (including spaces).
"""

def open_file(filePath):

    """
    Open the file and read contents 
    returns the content 
    """

    with open(filePath, "r") as loggerFile:
        loggerContent = loggerFile.read()
        #print(loggerContent)
        return loggerContent

def countLines(filePath):
    """
    Returns the total number of lines in a file.
    """
    countLine = 0
    countLines_content = open_file(filePath)
    for i in countLines_content.splitlines():
        countLine +=1

    return countLine

def countWords(filePath):
    """
    Returns the total number of words in a file.
    """
    countWords = 0
    countWords_content = open_file(filePath)
    for i in countWords_content.split():
        countWords +=1

    return countWords


def countcharacters(filePath):
    """
    Returns the total number of characters in a file,
    including spaces and newline characters.
    """
    countCharacter_content = open_file(filePath)
    return len(countCharacter_content)
    
