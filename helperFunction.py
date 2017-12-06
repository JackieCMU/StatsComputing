import psycopg2
import collections as cl

def rowToDict(row):
    '''
    row: a list
    return: a dictionary
    '''
    valueDict = cl.OrderedDict()
    keys = ['id', 'report_name', 'section', 'description',
            'arrest_time', 'address', 'neighborhood', 'zone']
    for i in range(len(keys)):
        valueDict[keys[i]] = row[i]
    valueDict['id'], valueDict['zone'] = int(valueDict['id']), int(valueDict['zone'])
    return valueDict

def match(row):
    '''
    row: a list
    return: a dictionary, a SQL script
    '''
    valueDict = rowToDict(row)
    neighbor = valueDict['neighborhood']
    script = "SELECT neighbor FROM neighborhoods" + \
    " WHERE LOWER(neighbor) LIKE LOWER('%" + neighbor + "%'" + ")" + \
    " OR LOWER(" + "'" + neighbor + "'" + ") LIKE format('%%%s%%', LOWER(neighbor));"
    return valueDict, script
