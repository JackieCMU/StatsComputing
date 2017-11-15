import re
import os
from functools import reduce
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def tokenize(path):
    '''
    path: the path of a folder containing all the documents
    return: a list of all the world in the documents
    '''
    fileList = os.listdir(path)
    wordList = []
    for filename in fileList:
        content = '|'
        if filename[-3:] == 'txt':
            with open(path + '/' + filename) as f:
                content = f.readlines()
            content = reduce(lambda x,y : x+y, content)
        elif filename[-3:] == 'xml':
            tree = ET.parse(path + '/' + filename)
            root = tree.getroot()
            xl = ET.tostring(root, encoding = 'utf-8', method = 'xml')
            soup = BeautifulSoup(xl, 'lxml')
            for item in soup.findAll("block", class_= "full_text"):
                content = content + item.text
        content = re.findall(r'[a-zA-Z]+', content)
        if len(content) != 0:
            wordList.append(content)
    return wordList