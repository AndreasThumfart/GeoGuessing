from flask import Flask, render_template
from flask_restful import Api, Resource
from json import json

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
        # get question from DB
        question = {
            "id":1,
            "title": "Wo befindet sich der Stephansdom?",
            "hint": "",
            "img": "",
            "lat": 16.2213,
            "long": 40.3281 
        }
        return json.dumps(question, separators=(',', ':'))


api.add_resource(QuestionAPI, '/questions/<int:id>', endpoint = 'question')

class GameAPI(Resource):
    def get(self):
        # get question from DB
        game = {
            "id":1,
            "questions":[1,2,3,4,5,67]
            
        }
        return json.dumps(game, separators=(',', ':'))
    def post(self, result):
        #save result to database
        response = "ok"
        return response


api.add_resource(GameAPI, '/games/', endpoint = 'game')

class LeaderboardAPI(Resource):
    def get(self, id):
        # get question from DB
        results = [{
            "id":1,
            "name" : "Andreas",
            "points" : 80
        },
        {
            "id":2,
            "name" : "Philipp",
            "points" : 100
        }
        ]
        return json.dumps(results, separators=(',', ':'))
        

api.add_resource(QuestionAPI, '/leaderboard/', endpoint = 'leaderboard')