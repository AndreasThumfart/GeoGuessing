import sqlite3
import random

class Games:
    def getGamesCount():
        query = "SELECT count(*) FROM users"      
        result = DbAccess.executeQuery(query)
        count = result[0]["count(*)"]
        return int(count)
    
    def createGame():
        questionsCount = Questions.getQuestionCount()
        gamesCount = Games.getGamesCount()
        
        gameId = gamesCount +1
        questionIds = random.sample(range(0, questionsCount ), 10)

        game = {
            "id": gameId,
            "questions": questionIds
        }
        return game
    
    def saveGame(game):
        gamesQuery = '''
            INSERT INTO users

            '''
        DbAccess.executeWriteQuery(gamesQuery)


    def getLeaderboard():
        query = "SELECT * FROM users ORDER BY game_points DESC LIMIT 10"
        result = DbAccess.executeQuery(query)
        return result       

class Questions:
    def getQuestion(id):
        query = f"SELECT * FROM question_sights WHERE id={id}"
        result = DbAccess.executeQuery(query)
        return result
    
    def getQuestionCount():
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
        result = cursor.execute(query)
        conn.commit()
        conn.close()
        return result