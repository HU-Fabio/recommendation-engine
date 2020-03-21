from database.connection import Database
import json
from tqdm import tqdm

def content_based_filtering():
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