# Use package pandas to read url or other csv, txt file
# Split by \t and place to two columns named "number" and "word"
# add number and word into a dictionary
def readFile(url):
    import pandas as pd
    data = pd.read_csv(url,sep='delimiter')
    colname = data.columns[0]
    data['number'], data['word'] = data[colname].str.split("\t").str
    data.number = data.number.astype(float)
    dic = {}
    for word, number in zip(data.word, data.number):
        dic[word] = number
    return dic
