import logging
import os

def saveFile(fileName, content, directory='.'):
    '''
    Save content to the fileName, overwriting the content if the file exists
    The current directory is the default
    '''
    logging.debug('Saving content to {}'.format(fileName))
    with open(os.path.join(directory, fileName), 'w', encoding='utf-8') as f:
        f.write(content)

def readFileToList(fileName, directory='.'):
    '''
    Read the file contents from fileName,
    returning a list of lines
    with the strip() method called on each line
    
    .strip() removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns
    
    Example:
        test1
        test2

        test3
    Will return ['test1', 'test2', '', 'test3']
    The current directory is the default
    '''
    logging.debug('Reading {} line by line into list'.format(fileName))
    lines = []
    with open(os.path.join(directory, fileName), encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def findFilesWithExtension(extension, directory='.'):
    '''
    The current directory is the default
    '''
    extension = '.' + extension.replace('.', '')
    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file)
    return files    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    saveFile('test.txt', 'test1\ntest2 \n\ntest3\n')
    
    logging.debug('Output of readFileToList:\n' + str(readFileToList('test.txt')))

    logging.debug('Files with txt extension in current directory:\n' + str(findFilesWithExtension('.py')))
