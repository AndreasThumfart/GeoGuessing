# GeoGuessing

Players are presented with questions, hints, and images of various locations. Using an integrated map, they must guess the location's exact spot. Points are awarded based on the accuracy of their guesses, with closer guesses earning more points. Test your geographical knowledge and see how well you can pinpoint locations around the world!

## Disclaimer

This project was created as part of the Agile Software Engineering class at University of Applied Sciences Vienna and is intended solely for learning and testing purposes. The content and code provided in this repository are not intended for commercial use.

## Functional description

The application uses HTML pages with JavaScript for the front end and Python Flask for the back end. The game consists of various questions and games, which are stored in an SQLite database.

- Front End\
  The front end is built using HTML and JavaScript, providing an interactive and user-friendly interface. An integrated map allows players to guess the location of the place based on the provided hints and images. Points are awarded based on the accuracy of the player's guess, with closer guesses earning more points. After answering 10 questions, the players can submit their result for the integrated leaderboard. 
- Back End\
  The back end is powered by Python Flask, which handles the server-side logic and communication. Flask RESTful APIs are used to deliver game data (questions and hints) from the SQLite database to the front end. 
- Database\
  The SQLite database stores questions, hints and URLs of images in one table, and the game results in a second table. Questions and hints are fetched from the SQLite database and delivered to the front end via RESTful APIs.


## Data modell

The game consists of the following 2 tables:

### Users
This taable contains the users results including the following information:

| Column Name | Data Type | Primary Key | Nullable |
|-------------|------------|-------------|------------|
|game_id|INTEGER| TRUE | FALSE |
|game_date|DATE| | TRUE |
|username|TEXT| | FALSE |
|game_points|INTEGER| | TRUE |

### Questions
This table contains the questions including the following information:

| Column Name | Data Type | Primary Key | Nullable |
|-------------|------------|-------------|------------|
|id|INTEGER| TRUE | FALSE |
|title|TEXT| | TRUE |
|name|TEXT| | TRUE |
|hint|TEXT| | TRUE |
|latitude|REAL| | TRUE |
|longitude|REAL| | TRUE |
|image_url|TEXT| | TRUE |


## Flask Installation manual

I have looked into Flask and got it running. However, to make it work, you need to configure it yourself after checking it out from GitHub using this guide: [Flask VS Code Tutorial.](https://code.visualstudio.com/docs/python/tutorial-flask)

**Important:**

1. Create the Python project environment that sets up the `.venv` folder.
2. Activate the environment via PowerShell or Command (depending on Windows or Mac).
3. Install the two packages `flask` and `flask-restful`:
   ```bash
   python -m pip install flask
   python -m pip install flask-restful
   ```
4. Start the app with:
   ```bash
   python -m flask run
   ```
After that, it should be accessible in the browser via http://127.0.0.1:5000/.

Afterwards, the project in GitHub should look like this and be able to start as described in the guide:

- All HTML pages must be placed in the `/templates` subfolder.
- In `app.py`, there is a function that renders `index.html` when the page is called.
- Additionally, a test REST endpoint is defined in it, which is successfully called in `test.html`.
- I will define the correct endpoints for our project by the weekend.


## Team
Authors of this project are:
- BECKE Lennart Noah
- MIES Matthias
- ROITH Patrick
- SHOSHARE Nayef
- THUMFART Andreas

---
