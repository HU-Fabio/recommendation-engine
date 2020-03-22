from engines.collaboritive_filtering import collaborativefiltering
from engines.content_based_filtering import content_based_filtering
from database.connection import Database


def initialize_data():
    print('Starting data generation \n'
          'Started creating collaboritive_filtering_data.csv')
    # collaborativefiltering()
    print('Finished creating collaboritive_filtering_data.csv \n',
          'Started creating content_based_filtering_data.csv')
    content_based_filtering()


def runApplication():
    running = True
    conn = Database.Mysql()
    mycursor = conn.cursor(buffered=True)
    while running:
        task = int(input('Welkom bij de recommendations engine van Fabio! \n'
                         'Selecteer om een opdracht uit te voeren: \n'
                         '1: Maak de recommendation data klaar \n'
                         '2: Doe een recommendation voor een profiel \n'
                         '3" Doe een recommendation voor een product \n'
                         '4: Sluit het programma af\n'))

        if task == 1:
            initialize_data()
        elif task == 2:
            profId = input('Voer een profiel id in: \n')
            mycursor.execute("SELECT * FROM recommendations_collaboritive WHERE '%s'" %profId)
            result = mycursor.fetchone()
            print(result)
        elif task == 3:
            productId = input('Voer een product id in: \n')
            mycursor.execute("SELECT * FROM recommendations_content_based WHERE '%s'" %productId)
            result = mycursor.fetchone()
            print(result)
        else:
            running = False

runApplication()
