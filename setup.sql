-- Create secret_location table
CREATE TABLE IF NOT EXISTS secret_location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    hint TEXT,
    lat FLOAT,
    long FLOAT,
    img TEXT
);

-- Insert locations
INSERT INTO secret_location (question, hint, lat, long, img) 
VALUES 
    ('Wo befindet sich der Stephansdom?', 'Hauptstadt von Österreich', 48.2082, 16.3738, 'https://upload.wikimedia.org/wikipedia/commons/d/dd/Wien_-_Stephansdom_%281%29.JPG'),
    ('Wo auf der Karte befindet sich der "Eiffelturm"?', 'Paris, Frankreich', 48.8584, 2.2945, 'https://upload.wikimedia.org/wikipedia/commons/e/e6/Tour_Eiffel_Wikimedia_Commons.jpg'),
    ('Wo auf der Karte befindet sich die "Chinesische Mauer"?', 'China', 40.4319, 116.5704, 'https://upload.wikimedia.org/wikipedia/commons/3/34/GreatWall_2004_Summer_4.jpg'),
    ('Wo auf der Karte befindet sich das "Taj Mahal"?', 'Indien', 27.1751, 78.0421, 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Taj_Mahal_in_March_2004.jpg'),
    ('Wo auf der Karte befinden sich die "Pyramiden von Gizeh"?', 'Ägypten', 29.9792, 31.1342, 'https://upload.wikimedia.org/wikipedia/commons/e/e3/All_Gizah_Pyramids.jpg'),
    ('Wo auf der Karte befindet sich die "Freiheitsstatue"?', 'New York, USA', 40.6892, -74.0445, 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Statue_of_Liberty_7.jpg'),
    ('Wo auf der Karte befindet sich das "Machu Picchu"?', 'Peru', -13.1631, -72.5450, 'https://upload.wikimedia.org/wikipedia/commons/9/94/80_-_Machu_Picchu_-_Juin_2009_-_edit.2.jpg'),
    ('Wo auf der Karte befindet sich das "Kolosseum"?', 'Rom, Italien', 41.8902, 12.4922, 'https://upload.wikimedia.org/wikipedia/commons/4/47/Colosseo_2020.jpg'),
    ('Wo auf der Karte befindet sich die "Petra"?', 'Jordanien', 30.3285, 35.4444, 'https://upload.wikimedia.org/wikipedia/commons/6/65/Petra_Jordan_BW_21.JPG'),
    ('Wo auf der Karte befindet sich die "Christusstatue in Rio de Janeiro"?', 'Brasilien', -22.9519, -43.2105, 'https://upload.wikimedia.org/wikipedia/commons/0/05/Christ_the_Redeemer_-_Cristo_Redentor.jpg'),
    ('Wo auf der Karte befindet sich das "Angkor Wat"?', 'Kambodscha', 13.4125, 103.8670, 'https://upload.wikimedia.org/wikipedia/commons/7/73/Angkor_Wat.jpg'),
    ('Wo auf der Karte befindet sich der "Burj Khalifa"?', 'Dubai, Vereinigte Arabische Emirate', 25.1972, 55.2744, 'https://upload.wikimedia.org/wikipedia/commons/9/93/Burj_Khalifa.jpg'),
    ('Wo auf der Karte befindet sich das "Sydney Opera House"?', 'Sydney, Australien', -33.8568, 151.2153, 'https://upload.wikimedia.org/wikipedia/commons/8/81/Sydney_Opera_House.jpg'),
    ('Wo auf der Karte befindet sich die "Golden Gate Bridge"?', 'San Francisco, USA', 37.8199, -122.4783, 'https://upload.wikimedia.org/wikipedia/commons/3/3e/GoldenGateBridge.jpg');

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_date DATE, 
    username TEXT NOT NULL,   
    game_points INTEGER
);
