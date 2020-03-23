from database.connection import Database
import json
from tqdm import tqdm
import csv


def content_based_filtering():
    conn = Database.Mysql()
    mycursor = conn.cursor(buffered=True)
    mycursor.execute("SELECT * FROM products")
    result = mycursor.fetchall()
    file = open('engines/csv/content_based_filtering_data.csv', "w+")
    with file:
        for item in tqdm(result):
            print(item)
            # TODO: Vragen aan Rico hoe je 's in een where clause kan doen
            mycursor.execute("SELECT * FROM products WHERE brand = %s AND type = %s AND category = %s", (str(item[2]), str(item[3]), str(item[4])))
            similarItems = mycursor.fetchall()
            similarItems.pop(0)
            if len(similarItems) > 20:
                for similarItem in similarItems:
                    count = 0
                    words = similarItem[1].split()
                    for word in words:
                        if word in item[1]:
                            count += 1
                    if count < 3:
                        similarItems.remove(similarItem)
            products = []
            for product in similarItems:
                products.append(product[0])

            fnames = ['product', 'recommendations']
            writer = csv.DictWriter(file, fieldnames=fnames)
            linedic = {'product': item[0], 'recommendations':json.dumps(products)}
            writer.writerow(linedic)
    file.close()