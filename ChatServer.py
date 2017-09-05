import json
from flask import Flask, render_template, request
from flask_restful import Resource, Api
import time
import dbconnection
from config import HOST, CHAT_PORT

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    @staticmethod
    def post():
        try:
            data = json.loads(request.data)
            current_timestamp = time.time()
            dbconnection.add_chat_message_to_db(str(current_timestamp), data['user'], data['text'])
            return {"ok": True}
        except:
            return {"error": True}

class Users(Resource):
    @staticmethod
    def get():
        return dbconnection.get_unique_users()

class Messages(Resource):
    @staticmethod
    def get():
        return dbconnection.get_latest_records(count_of_records=100)

api.add_resource(Message, '/message')
api.add_resource(Users, '/users')
api.add_resource(Messages, '/messages')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host=HOST, port=CHAT_PORT, debug=True)





