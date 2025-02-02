import sqlite3
import random
import datetime

class Games:
    """
    Games class provides all functions for games and leaderboard
    """
    def createGame():
        """
        Create a new game and generate random numbers for the questions 
        """
        questionsCount = Questions.getQuestionCount()
        questionIds = random.sample(range(0, questionsCount ), 10)
        game = {
            "questions": questionIds
        }
        return game
    
    def saveGame(game):
        """
        Save game to database
        """
        today = datetime.datetime.today()
        formatted_date = today.strftime('%Y-%m-%d')
        gamesQuery = f'INSERT INTO users (game_date,username,game_points) VALUES ("{formatted_date}","{game["name"]}",{game["points"]})'
        DbAccess.executeWriteQuery(gamesQuery)


    def getLeaderboard():
        """
        Get leaderboard list.
        Gets the 10 top scoring games from the database
        """
        query = "SELECT * FROM users ORDER BY game_points DESC LIMIT 10"
        result = DbAccess.executeQuery(query)
        return result       

class Questions:
    """
    Questions class provides methodes to retrieve questions from the database
    """
    def getQuestion(id):
        """
        Get a question by id
        """
        query = f"SELECT * FROM question_sights WHERE id={id}"
        result = DbAccess.executeQuery(query)
        return result
    
    def getQuestionCount():
        """
        Get the overall number of questions in the database
        """
        query = "SELECT count(*) FROM question_sights"
        result = DbAccess.executeQuery(query)
        count = result[0]["count(*)"]
        return int(count)


class DbAccess:
    """
    DB Access layer class
    """
    def executeQuery(query):
        """
        execute read query
        """
        conn = sqlite3.connect('geo_guessingDB.db')
        cursor = conn.cursor()
        result = cursor.execute(query)
        rows = result.fetchall()
        # Get column names from the cursor description
        column_names = [description[0] for description in cursor.description]
        # Convert rows to list of dictionaries
        response = [dict(zip(column_names, row)) for row in rows]
        conn.close()
        return response

    def executeWriteQuery(query):
        """
        execute write query
        """
        conn = sqlite3.connect('geo_guessingDB.db')
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        