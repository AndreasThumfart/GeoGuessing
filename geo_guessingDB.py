import sqlite3

# Verbindung zur Datenbank herstellen (erstellt die Datei, wenn sie nicht existiert)
conn = sqlite3.connect('geo_guessingDB.db')
cursor = conn.cursor()


# Tabelle für Sehenswürdigkeiten erstellen (neu erstellen)
cursor.execute('''
CREATE TABLE question_sights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,   
    name TEXT NOT NULL,
    hint TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    image_url TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE users (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_date DATE, 
    username TEXT NOT NULL,   
    game_points INTEGER
)
''')



#Daten für die Sehenswürdigkeiten, inklusive Fragen
sights = [
    ("Wo auf der Karte befindet sich der \"Eiffelturm\"?", "Eiffelturm", "Liegt in einer wunderschönen Stadt in Frankreich", 48.8584, 2.2945, "https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg"),
    ("Wo auf der Karte befindet sich die \"Chinesische Mauer\"?", "Chinesische Mauer", "Verläuft durch das nördliche China", 40.4319, 116.5704, "https://upload.wikimedia.org/wikipedia/commons/3/35/GreatWall_2004_Summer_4.jpg"),
    ("Wo auf der Karte befindet sich das \"Taj Mahal\"?", "Taj Mahal", "Steht in einem Land mit wunderbaren Bollywood-Filmen", 27.1751, 78.0421, "https://upload.wikimedia.org/wikipedia/commons/d/dd/Taj_Mahal_in_March_2004.jpg"),
    ("Wo auf der Karte befinden sich die \"Pyramiden von Gizeh\"?", "Pyramiden von Gizeh", "Befinden sich in der Nähe des Nils", 29.9792, 31.1342, "https://upload.wikimedia.org/wikipedia/commons/e/e3/All_Gizah_Pyramids.jpg"),
    ("Wo auf der Karte befindet sich die \"Freiheitsstatue\"?", "Freiheitsstatue", "Ist auf einer Insel in den USA zu finden", 40.6892, -74.0445, "https://upload.wikimedia.org/wikipedia/commons/a/a1/Statue_of_Liberty_7.jpg"),
    ("Wo auf der Karte befindet sich das \"Machu Picchu\"?", "Machu Picchu", "Eine alte Inkastadt in Südamerika", -13.1631, -72.5450, "https://upload.wikimedia.org/wikipedia/commons/e/eb/80_-_Machu_Picchu_-_Juin_2009_-_edit.2.jpg"),
    ("Wo auf der Karte befindet sich das \"Kolosseum\"?", "Kolosseum", "Ein antikes Amphitheater in Italien", 41.8902, 12.4922, "https://upload.wikimedia.org/wikipedia/commons/d/df/Colosseo_2020.jpg"),
    ("Wo auf der Karte befindet sich die \"Petra\"?", "Petra", "Eine berühmte Felsenstadt in Jordanien", 30.3285, 35.4444, "https://upload.wikimedia.org/wikipedia/commons/9/96/Petra_Jordan_BW_21.JPG"),
    ("Wo auf der Karte befindet sich die \"Christusstatue in Rio de Janeiro\"?", "Ein Wahrzeichen auf einem Berg in Südamerika", "Blickt über eine berühmte Stadt in Brasilien", -22.9519, -43.2105, "https://upload.wikimedia.org/wikipedia/commons/8/89/Christ_the_Redeemer_-_Cristo_Redentor.jpg"),
    ("Wo auf der Karte befindet sich das \"Angkor Wat\"?", "Angkor Wat", "Ist eine riesige Tempelanlage und liegt in Asien", 13.4125, 103.8670, "https://upload.wikimedia.org/wikipedia/commons/a/a0/Angkor_Wat.jpg"),
    ("Wo auf der Karte befindet sich der \"Burj Khalifa\"?", "Burj Khalifa", "Das höchste Gebäude der Welt", 25.1972, 55.2744, "https://upload.wikimedia.org/wikipedia/commons/9/93/Burj_Khalifa.jpg"),
    ("Wo auf der Karte befindet sich das \"Sydney Opera House\"?", "Sydney Opera House", "Eine ikonische Oper in Australien", -33.8568, 151.2153, "https://upload.wikimedia.org/wikipedia/commons/f/f4/Sydney_Opera_House.jpg"),
    ("Wo auf der Karte befindet sich die \"Golden Gate Bridge\"?", "Golden Gate Bridge", "Eine berühmte Brücke in Kalifornien", 37.8199, -122.4783, "https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge.jpg"),
    ("Wo auf der Karte befindet sich die \"Alhambra\"?", "Alhambra", "Eine historische Festung in Südspanien", 37.1760, -3.5881, "https://upload.wikimedia.org/wikipedia/commons/f/fc/Alhambra.jpg"),
    ("Wo auf der Karte befindet sich die \"Acropolis\"?", "Acropolis", "Liegt in der Hauptstadt von Griechenland", 37.9715, 23.7257, "https://upload.wikimedia.org/wikipedia/commons/a/af/Acropolis_Athens.jpg"),
    ("Wo auf der Karte befindet sich der \"Big Ben\"?", "Big Ben", "Ein berühmter Uhrturm in London", 51.5007, -0.1246, "https://upload.wikimedia.org/wikipedia/commons/9/91/Big_Ben.jpg"),
    ("Wo auf der Karte befindet sich das \"Louvre Museum\"?", "Louvre Museum", "Ein weltbekanntes Museum in Frankreich", 48.8606, 2.3376, "https://upload.wikimedia.org/wikipedia/commons/a/a8/Louvre.jpg"),
    ("Wo auf der Karte befindet sich die \"Prager Burg\"?", "Prager Burg", "Liegt in der Hauptstadt der Tschechischen Republik", 50.0901, 14.4006, "https://upload.wikimedia.org/wikipedia/commons/9/94/Prager_Burg.jpg"),
    ("Wo auf der Karte befindet sich der \"Times Square\"?", "Times Square", "Ein belebter Platz an der Ostküste der USA", 40.7580, -73.9855, "https://upload.wikimedia.org/wikipedia/commons/c/c7/Times_Square.jpg"),
    ("Wo auf der Karte befindet sich der \"Schiefe Turm von Pisa\"?", "Schiefer Turm von Pisa", "Ein schiefer Turm in Italien", 43.7228, 10.3966, "https://upload.wikimedia.org/wikipedia/commons/9/96/Pisa.jpg"),
    ("Wo auf der Karte befindet sich der \"Mount Everest\"?", "Mount Everest", "Der höchste Berg der Welt, liegt in Asien", 27.9881, 86.9250, "https://upload.wikimedia.org/wikipedia/commons/e/e4/Mount_Everest.jpg"),
    ("Wo auf der Karte befindet sich der \"Grand Canyon\"?", "Grand Canyon", "Eine riesige Schlucht im Südwesten der USA", 36.1069, -112.1129, "https://upload.wikimedia.org/wikipedia/commons/6/65/Grand_Canyon_view_from_Pima_Point_2010.jpg"),
    ("Wo auf der Karte befindet sich das \"Stonehenge\"?", "Stonehenge", "Ein mysteriöser Steinkreis in England", 51.1789, -1.8262, "https://upload.wikimedia.org/wikipedia/commons/3/3c/Stonehenge2007_07_30.jpg"),
    ("Wo auf der Karte befinden sich die \"Niagarafälle\"?", "Niagarafälle", "Wasserfälle an einer Grenze in Nordamerika", 43.0962, -79.0377, "https://upload.wikimedia.org/wikipedia/commons/4/41/3Falls_Niagara.jpg"),
    ("Wo auf der Karte befindet sich das \"Great Barrier Reef\"?", "Great Barrier Reef", "Ein Korallenriff vor der Küste Australiens", -18.2871, 147.6992, "https://upload.wikimedia.org/wikipedia/commons/6/63/GreatBarrierReef-EO.JPG"),
    ("Wo auf der Karte befindet sich das \"Neuschwanstein Schloss\"?", "Schloss Neuschwanstein", "Ein märchenhaftes Schloss in Deutschland", 47.5576, 10.7498, "https://upload.wikimedia.org/wikipedia/commons/c/ce/Schloss_Neuschwanstein.jpg"),
    ("Wo auf der Karte befindet sich das \"Empire State Building\"?", "Empire State Building", "Ein berühmtes Hochhaus in den USA", 40.748817, -73.985428, "https://upload.wikimedia.org/wikipedia/commons/6/6c/Empire_State_Building.jpg"),
    ("Wo auf der Karte befindet sich die \"Victoriafälle\"?", "Victoriafälle", "Große Wasserfälle im Süden Afrikas", -17.9243, 25.8572, "https://upload.wikimedia.org/wikipedia/commons/0/01/Victoria_Falls.jpg"),
    ("Wo auf der Karte befindet sich der \"Schloss Versailles\"?", "Schloss Versailles", "Ein prachtvolles Schloss in Frankreich", 48.8049, 2.1204, "https://upload.wikimedia.org/wikipedia/commons/e/e8/Chateau_de_Versailles.jpg"),
    ("Wo auf der Karte befindet sich die \"Chrysler Building\"?", "Chrysler Building", "Ein ikonisches Hochhaus in den USA", 40.7516, -73.9755, "https://upload.wikimedia.org/wikipedia/commons/a/a3/Chrysler_Building_New_York_City.jpg")
]



# Daten einfügen
for sight in sights:
    title, name, hint, latitude, longitude, image_url = sight
    cursor.execute('''
    INSERT INTO question_sights (title, name, hint, latitude, longitude, image_url)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, name, hint, latitude, longitude, image_url))



users_data = [
    ("2023-01-01", "PlayerOne", 150),
    ("2023-01-02", "PlayerTwo", 200),
    ("2023-01-03", "PlayerThree", 120)
]

cursor.executemany('''
INSERT INTO users (game_date, username, game_points)
VALUES (?, ?, ?)
''', users_data)


# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Alles wurde aktualisiert")
