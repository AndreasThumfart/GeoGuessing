from flask import Flask, render_template
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)


@app.route('/', defaults={'page':None})
@app.route('/<page>')
def home(page):
    if page == None:   
        return render_template('index.html')
    else:
        return render_template(page)
if __name__ == '__main__':
   app.run()


users = []
id = 0

# class UserAPI(Resource):
#     def get(self, name):
#         return "test successfull"
#     def post(self, name):
#         global id
#         user = {'name' : name, 'id' : id}
#         id += 1
#         users.append(user)
#         return user

# api.add_resource(UserAPI, '/users/<string:name>', endpoint = 'user')

class QuestionAPI(Resource):
    def get(self, id):
        # get question from DB by ID
        question = {
            "id": 1,
            "title": "Wo befindet sich der Stephansdom?",
            "hint": "Tipp: Der Stephansdom befindet sich in der Hauptstadt von Österreich",
            "img": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Wien_-_Stephansdom_%281%29.JPG",
            "lat": 48.2082,  # Richtige Breite (Stephansdom)
            "long": 16.3738  # Richtige Länge (Stephansdom)
        }
        return json.dumps(question, separators=(',', ':'))


api.add_resource(QuestionAPI, '/questions/<int:id>', endpoint = 'question')

class GameAPI(Resource):
    def get(self):
        # get question from DB
        # randomly select 10 questions from DB questions
        # build json object
        # game id = next ID in DB (count users rows+1)
        game = {
            "id":1,
            "questions":[1,2,3,4,5,67]
            
        }
        return json.dumps(game, separators=(',', ':'))
    def post(self, result):
        #save result to database
        # extected json object
        # {
        #     "name":"Andreas",
        #     "points":100
        # }
        response = "ok"
        return response


api.add_resource(GameAPI, '/games/', endpoint = 'game')

class LeaderboardAPI(Resource):
    def get(self, id):
        # get question from DB
        # connect to db
        # get top 10 results from users table
        results = [{
            "id":1,
            "name" : "Andreas",
            "date": "2025-01-03",
            "points" : 80
        },
        {
            "id":2,
            "name" : "Philipp",
            "date": "2025-01-12",
            "points" : 100
        }
        ]
        return json.dumps(results, separators=(',', ':'))
        

api.add_resource(LeaderboardAPI, '/leaderboard/', endpoint = 'leaderboard')