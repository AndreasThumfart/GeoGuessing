from flask import Flask, render_template
from flask_restful import Api, Resource

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

class UserAPI(Resource):
    def get(self, name):
        return "test successfull"
    def post(self, name):
        global id
        user = {'name' : name, 'id' : id}
        id += 1
        users.append(user)
        return user

api.add_resource(UserAPI, '/users/<string:name>', endpoint = 'user')