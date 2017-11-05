# Use package pandas to read url or other csv, txt file
# Split by \t and place to two columns named "number" and "word"
# add number and word as tuple into a list
def readFile(txt):
    import pandas as pd
    data = pd.read_csv(txt, sep='delimiter')
    colname = data.columns[0]
    data['number'], data['word'] = data[colname].str.split("\t").str
    data.number = data.number.astype(float)
    dic = list(zip(data.number, data.word))
    return dic
