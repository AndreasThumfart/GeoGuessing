from flask import Flask, render_template, request, abort
from flask_restful import Api, Resource
from flask_cors import CORS
import json
import GeoGuessing

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/', defaults={'page':None})
@app.route('/<page>')
def home(page):
    if page == None:   
        return render_template('index.html')
    else:
        return render_template(page)
if __name__ == '__main__':
   app.run()

class QuestionAPI(Resource):
    """
    Question API to provide question details for the front end
    """
    def get(self, id):
        # get question from DB by ID
        question = GeoGuessing.Questions.getQuestion(id)
        return json.dumps(question, separators=(',', ':'))


api.add_resource(QuestionAPI, '/questions/<int:id>', endpoint = 'question')

class GameAPI(Resource):
    """
    Game API to start and safe game
    """
    def get(self):
        # get question from DB
        game = GeoGuessing.Games.createGame()
        return json.dumps(game, separators=(',', ':'))
    def post(self):
        #save result to database
        game = request.json
        GeoGuessing.Games.saveGame(game)

api.add_resource(GameAPI, '/games/', endpoint = 'game')

class LeaderboardAPI(Resource):
    """
    Leaderboard API to get the top 10 players
    """
    def get(self):
        # get question from DB
        leaderboard = GeoGuessing.Games.getLeaderboard()
        return json.dumps(leaderboard, separators=(',', ':'))
        

api.add_resource(LeaderboardAPI, '/leaderboard/', endpoint = 'leaderboard')



