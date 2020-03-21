from database.connection import Database
import json
from tqdm import tqdm


def collaborativefiltering():
    conn = Database.Mysql()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM profiles_previously_viewed")
    result = mycursor.fetchall()

    viewedPerProfile = {}

    for item in result:
        if item[0] in viewedPerProfile:
            viewedPerProfile[item[0]].append(item[1])
        else:
            viewedPerProfile[item[0]] = [item[1]]

    for key in list(viewedPerProfile):
        value = viewedPerProfile[key]
        if len(value) <= 1:
            del viewedPerProfile[key]

    for item in tqdm(viewedPerProfile):
        key = item
        values = viewedPerProfile[item]
        recommendations = []
        counter = 0
        for compare in viewedPerProfile:
            compareValues = viewedPerProfile[compare]
            if len(list(set(compareValues) - set(values))) != 0:
                for value in values:
                    for compareValue in compareValues:
                        if value == compareValue:
                            counter += 1
                        else:
                            continue
            if counter > 2:
                recommendations = values + compareValues
        mycursor.execute('INSERT IGNORE INTO recommendations (profid, recommendations) VALUES (%s, %s)',
                             (key, json.dumps(recommendations)))
        conn.commit()
