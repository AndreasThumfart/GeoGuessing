import sqlite3

# Verbindung zur Datenbank herstellen (erstellt die Datei, wenn sie nicht existiert)
conn = sqlite3.connect('geo_guessing_database.db')
cursor = conn.cursor()


# Tabelle für Sehenswürdigkeiten erstellen (neu erstellen)
cursor.execute('''
CREATE TABLE question_sights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,   
    name TEXT NOT NULL,
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
    ("Wo auf der Karte befindet sich der \"Eiffelturm\"?", "Eiffelturm", 48.8584, 2.2945, "https://de.wikipedia.org/wiki/Datei:Tour_Eiffel_Wikimedia_Commons.jpg"),
    ("Wo auf der Karte befindet sich die \"Chinesische Mauer\"?", "Chinesische Mauer", 40.4319, 116.5704, "https://de.wikipedia.org/wiki/Datei:GreatWall_2004_Summer_4.jpg"),
    ("Wo auf der Karte befindet sich das \"Taj Mahal\"?", "Taj Mahal", 27.1751, 78.0421, "https://de.wikipedia.org/wiki/Datei:Taj_Mahal_in_March_2004.jpg"),
    ("Wo auf der Karte befinden sich die \"Pyramiden von Gizeh\"?", "Pyramiden von Gizeh", 29.9792, 31.1342, "https://de.wikipedia.org/wiki/Datei:All_Gizah_Pyramids.jpg"),
    ("Wo auf der Karte befindet sich die \"Freiheitsstatue\"?", "Freiheitsstatue", 40.6892, -74.0445, "https://de.wikipedia.org/wiki/Datei:Statue_of_Liberty_7.jpg"),
    ("Wo auf der Karte befindet sich das \"Machu Picchu\"?", "Machu Picchu", -13.1631, -72.5450, "https://de.wikipedia.org/wiki/Datei:80_-_Machu_Picchu_-_Juin_2009_-_edit.2.jpg"),
    ("Wo auf der Karte befindet sich das \"Kolosseum\"?", "Kolosseum", 41.8902, 12.4922, "https://de.wikipedia.org/wiki/Datei:Colosseo_2020.jpg"),
    ("Wo auf der Karte befindet sich die \"Petra\"?", "Petra", 30.3285, 35.4444, "https://de.wikipedia.org/wiki/Datei:Petra_Jordan_BW_21.JPG"),
    ("Wo auf der Karte befindet sich die \"Christusstatue in Rio de Janeiro\"?", "Christusstatue in Rio de Janeiro", -22.9519, -43.2105, "https://de.wikipedia.org/wiki/Datei:Christ_the_Redeemer_-_Cristo_Redentor.jpg"),
    ("Wo auf der Karte befindet sich das \"Angkor Wat\"?", "Angkor Wat", 13.4125, 103.8670, "https://de.wikipedia.org/wiki/Datei:Angkor_Wat.jpg"),
    ("Wo auf der Karte befindet sich der \"Burj Khalifa\"?", "Burj Khalifa", 25.1972, 55.2744, "https://de.wikipedia.org/wiki/Datei:Burj_Khalifa.jpg"),
    ("Wo auf der Karte befindet sich das \"Sydney Opera House\"?", "Sydney Opera House", -33.8568, 151.2153, "https://de.wikipedia.org/wiki/Datei:Sydney_Opera_House.jpg"),
    ("Wo auf der Karte befindet sich die \"Golden Gate Bridge\"?", "Golden Gate Bridge", 37.8199, -122.4783, "https://de.wikipedia.org/wiki/Datei:GoldenGateBridge.jpg"),
    ("Wo auf der Karte befindet sich die \"Alhambra\"?", "Alhambra", 37.1760, -3.5881, "https://de.wikipedia.org/wiki/Datei:Alhambra.jpg"),
    ("Wo auf der Karte befindet sich die \"Acropolis\"?", "Acropolis", 37.9715, 23.7257, "https://de.wikipedia.org/wiki/Datei:Acropolis_Athens.jpg"),
    ("Wo auf der Karte befindet sich der \"Big Ben\"?", "Big Ben", 51.5007, -0.1246, "https://de.wikipedia.org/wiki/Datei:Big_Ben.jpg"),
    ("Wo auf der Karte befindet sich das \"Louvre Museum\"?", "Louvre Museum", 48.8606, 2.3376, "https://de.wikipedia.org/wiki/Datei:Louvre.jpg"),
    ("Wo auf der Karte befindet sich die \"Prager Burg\"?", "Prager Burg", 50.0901, 14.4006, "https://de.wikipedia.org/wiki/Datei:Prager_Burg.jpg"),
    ("Wo auf der Karte befindet sich der \"Times Square\"?", "Times Square", 40.7580, -73.9855, "https://de.wikipedia.org/wiki/Datei:Times_Square.jpg"),
    ("Wo auf der Karte befindet sich der \"Schiefe Turm von Pisa\"?", "Schiefer Turm von Pisa", 43.7228, 10.3966, "https://de.wikipedia.org/wiki/Datei:Pisa.jpg"),
    ("Wo auf der Karte befindet sich der \"Mount Everest\"?", "Mount Everest", 27.9881, 86.9250, "https://de.wikipedia.org/wiki/Datei:Mount_Everest.jpg"),
    ("Wo auf der Karte befindet sich der \"Grand Canyon\"?", "Grand Canyon", 36.1069, -112.1129, "https://de.wikipedia.org/wiki/Datei:Grand_Canyon_view_from_Pima_Point_2010.jpg"),
    ("Wo auf der Karte befindet sich das \"Stonehenge\"?", "Stonehenge", 51.1789, -1.8262, "https://de.wikipedia.org/wiki/Datei:Stonehenge2007_07_30.jpg"),
    ("Wo auf der Karte befinden sich die \"Niagarafälle\"?", "Niagarafälle", 43.0962, -79.0377, "https://de.wikipedia.org/wiki/Datei:3Falls_Niagara.jpg"),
    ("Wo auf der Karte befindet sich das \"Great Barrier Reef\"?", "Great Barrier Reef", -18.2871, 147.6992, "https://de.wikipedia.org/wiki/Datei:GreatBarrierReef-EO.JPG"),
    ("Wo auf der Karte befindet sich das \"Neuschwanstein Schloss\"?", "Schloss Neuschwanstein", 47.5576, 10.7498, "https://de.wikipedia.org/wiki/Datei:Schloss_Neuschwanstein.jpg"),
    ("Wo auf der Karte befindet sich die \"Christ the Redeemer\"-Statue?", "Christ the Redeemer", -22.9519, -43.2105, "https://de.wikipedia.org/wiki/Datei:Christ_the_Redeemer_-_Cristo_Redentor.jpg"),
    ("Wo auf der Karte befindet sich das \"Empire State Building\"?", "Empire State Building", 40.748817, -73.985428, "https://de.wikipedia.org/wiki/Datei:Empire_State_Building.jpg"),
    ("Wo auf der Karte befindet sich die \"Victoriafälle\"?", "Victoriafälle", -17.9243, 25.8572, "https://de.wikipedia.org/wiki/Datei:Victoria_Falls.jpg"),
    ("Wo auf der Karte befindet sich die \"Petra\"?", "Petra", 30.3285, 35.4444, "https://de.wikipedia.org/wiki/Datei:Petra_Jordan_BW_21.JPG")
]



# Daten einfügen
for sight in sights:
    question, name, latitude, longitude, image_url = sight
    cursor.execute('''
    INSERT INTO question_sights (question, name, latitude, longitude, image_url)
    VALUES (?, ?, ?, ?, ?)
    ''', (question, name, latitude, longitude, image_url))



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
