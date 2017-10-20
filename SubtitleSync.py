import logging

import re
from datetime import timedelta

import FileUtils

def timeToSrtTime(t):
    logging.debug('Formatting: "' + str(t) + '"')
    li = str(t).split(':')
    temp = li[2].split('.')
    li = li[:2] + temp
    for i in range(3):
        li[i] = li[i].zfill(2)
    if len(li) == 3:
        li.append('0')
    li[3] = li[3][:3]

    out = '{:s}:{:s}:{:s},{:s}'.format(li[0], li[1], li[2], li[3])
    logging.debug('Formatted to: "' + out + '"')
    return out

def addTime(line, delta):
    pattern = re.compile('^(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})$')

    m = re.match(pattern, line)
    if m:
        logging.debug('Matched "' + line + '" adding delta')
        groups = [int(x) for x in  m.groups()]
        
        t1 = timedelta(hours=groups[0], minutes=groups[1], seconds=groups[2], milliseconds=groups[3])
        t2 = timedelta(hours=groups[4], minutes=groups[5], seconds=groups[6], milliseconds=groups[7])

        add = timedelta(milliseconds=delta)
        line = timeToSrtTime(t1 + add) + ' --> ' + timeToSrtTime(t2 + add)
    return line

def getDelta():
    delta = 0
    try:
        delta = int(input('Time Delta:'))
    except:
        print('Not a valid Integer')
        exit(1)
    logging.info('Delta set as: ' + str(delta))
    return delta

def getSubtitlesFile():
    files = FileUtils.findFilesWithExtension('.srt')
    if len(files) == 0:
        print('No subtitle files found')
        exit(1)
    if len(files) > 1:
        print('Multiple subtitle files found')
        exit(1)
    logging.info('Subtitles file: ' + files[0])
    return files[0]

if __name__ == '__main__':
    logging.basicConfig(format='', level=logging.DEBUG)
    
    delta = getDelta()
    sfile = getSubtitlesFile()
    
    lines = FileUtils.readFileToList(sfile)

    contents = ''
    for i in range(len(lines)):
        contents += addTime(lines[i], delta) + '\n'

    FileUtils.saveFile(sfile, contents)
