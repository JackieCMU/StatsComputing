import psycopg2
import webbrowser, os
import matplotlib.pyplot as plt, mpld3
import numpy as np
import csv
from datetime import timedelta, datetime, date

crimeType = {'3304':'Criminal mischief', '2709':'Harassment', '3502':'Burglary',
'13(a)(16)':'Possession of a controlled substance', '13(a)(30)':'Possession w/intent to deliver',
'3701':'Robbery', '3921':'Theft', '3921(a)':'Theft of movable property',
'3934':'Theft from a motor vehicle', '3929':'Retail theft',
'2701':'Simple assault', '2702':'Aggravated assualt', '2501':'Homicide'}

script1 = """SELECT
count(*), section, to_char(max(arrest_time), 'YYYY-MM-DD') FROM blotter
WHERE arrest_time > (SELECT date_trunc('week', max(arrest_time)) FROM blotter)
GROUP BY section;
"""

script2 = """SELECT count(*),
to_char(arrest_time, 'YYYY-MM-DD') as DATE FROM blotter
WHERE arrest_time >= (SELECT date_trunc('day', max(arrest_time) - interval '1' month) FROM blotter)
AND arrest_time < (SELECT date_trunc('day', max(arrest_time)) FROM blotter)
GROUP BY DATE
ORDER BY DATE;
"""

script3 =  """
SELECT
CASE
WHEN thisWeekneighbor IS NULL THEN lastWeekneighbor
ELSE thisWeekneighbor
END AS neighborhood,
CASE
WHEN thisWeekCount IS NULL THEN -lastWeekCount
WHEN lastWEEKCount IS NULL THEN thisWeekCount
ELSE thisWeekCount - lastWeekCount
END AS DIF
FROM
(SELECT neighborhood as thisWeekneighbor,
count(*) as thisWeekCount FROM blotter as this
WHERE arrest_time > (SELECT date_trunc('week', max(arrest_time)) FROM blotter)
AND arrest_time < (SELECT date_trunc('week', max(arrest_time)) FROM blotter) + interval '6 day'
GROUP BY neighborhood) thisWeek
FULL OUTER JOIN
(SELECT neighborhood as lastWeekneighbor,
count(*) as lastWeekCount FROM blotter as last
WHERE arrest_time > (SELECT date_trunc('week', max(arrest_time)) FROM blotter)  - interval '7 day'
AND arrest_time < (SELECT date_trunc('week', max(arrest_time)) FROM blotter) - interval '1 day'
GROUP BY neighborhood) lastWeek
ON thisWeek.thisWeekneighbor = lastWeek.lastWeekneighbor;
"""

script4 =  """
SELECT
CASE
WHEN thisWeekzone IS NULL THEN lastWeekzone
ELSE thisWeekzone
END AS zone,
CASE
WHEN thisWeekCount IS NULL THEN -lastWeekCount
WHEN lastWEEKCount IS NULL THEN thisWeekCount
ELSE thisWeekCount - lastWeekCount
END AS DIF
FROM
(SELECT zone as thisWeekzone,
count(*) as thisWeekCount FROM blotter as this
WHERE arrest_time > (SELECT date_trunc('week', max(arrest_time)) FROM blotter)
AND arrest_time < (SELECT date_trunc('week', max(arrest_time)) FROM blotter) + interval '6 day'
GROUP BY zone) thisWeek
FULL OUTER JOIN
(SELECT zone as lastWeekzone,
count(*) as lastWeekCount FROM blotter as last
WHERE arrest_time > (SELECT date_trunc('week', max(arrest_time)) FROM blotter)  - interval '7 day'
AND arrest_time < (SELECT date_trunc('week', max(arrest_time)) FROM blotter) - interval '1 day'
GROUP BY zone) lastWeek
ON thisWeek.thisWeekzone = lastWeek.lastWeekzone;
"""
time = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day)

# Produce a table of counts of crimes each week, split up by type of crime
def CountCrimePerWeek_Table():
    cur.execute(script1)
    output = cur.fetchall()
    count = [str(item[0]) for item in output]
    ctype = [crimeType[item[1]] for item in output]
    date = min([item[2] for item in output])

    data = {'Crime_type':ctype,
        'Count':count}
    html = '<table><tr><th>' + '</th><th><th>'.join(data.keys()) + '</th></tr>'
    for row in zip(*data.values()):
        html += '<tr><td>' + '</td><td><td><td>'.join(row) + '</td><td></tr>'
    html = html + date + '</table>'
    f = open(time + '_' + 'Crime_type' + '_table.html', 'w')
    f.write(html)
    f.close()

# Graph the total number of crimes per day over the past month
def TotalCrimePerMonth_plot():
    cur.execute(script2)
    output = cur.fetchall()
    count = [item[0] for item in output]
    date = [item[1] for item in output]
    Lastday = datetime.strptime(max(date), '%Y-%m-%d')
    dateList = []
    for i in range(29, -1, -1):
        date_ = Lastday - timedelta(days=i)
        dateList.append(date_.isoformat().split('T')[0])
    count_ = []
    for i in range(len(dateList)):
        if dateList[i] not in date:
            count_.append(0)
        else:
            count_.append(count[date.index(dateList[i])])
    y_pos = np.arange(len(dateList))
    plt.bar(y_pos, count_)
    plt.xlabel("Date")
    plt.ylabel("Total number of crimes")
    plt.xticks(y_pos, dateList, rotation='vertical')
    plt.title("Barplot of number fo crimes per day for past month")
    plt.savefig('graph.png', bbox_inches='tight')
    f = open(time + '_graph.html', 'w')
    f.write('<img src = "' + 'graph.png' + '" alt ="cfg">\n')
    f.write('</html>\n')
    f.close()

# List the change in number of crimes between this week and last week
# split up both by neighborhood and by police zone (in separate tables)
def Changeneighbor():
    cur.execute(script3)
    output = cur.fetchall()
    with open(time + 'change_of_neighbor_.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(output)

def Changezone():
    cur.execute(script4)
    output = cur.fetchall()
    with open(time + 'change_of_zone_.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(output)

conn = psycopg2.connect(host = 'sculptor.stat.cmu.edu', database = 'jiaqih1', user = 'jiaqih1', password = 'eu2Uenais')
cur = conn.cursor()

CountCrimePerWeek_Table()
webbrowser.open('file://' + os.path.realpath(time + '_' + 'Crime_type' + '_table.html'))

TotalCrimePerMonth_plot()
webbrowser.open('file://' + os.path.realpath(time + '_graph.html'))

Changeneighbor()

Changezone()

conn.close()
