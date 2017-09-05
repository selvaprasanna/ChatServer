# Chat Server: Implemented via Flask

from config import HOST, CHAT_PORT
from flask import Flask, render_template, request
from flask_restful import Resource, Api
import dbconnection
import json
import time

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    @staticmethod
    def post():
        """
        This post method is called when below API is hit.
        API: curl -X POST -H "Content-Type: application/json" --data '{"user":"x", "text":"y"}' http://localhost:8081/message
        """
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
        """
        This get method is called when below API is hit.
        API: curl -H "Content-Type: application/json" http://localhost:8081/users
        """
        return dbconnection.get_unique_users()

class Messages(Resource):
    @staticmethod
    def get():
        """
        This get method is called when below API is hit.
        API: curl -H "Content-Type: application/json" http://localhost:8081/messages
        """
        return dbconnection.get_latest_records(count_of_records=100)

api.add_resource(Message, '/message')
api.add_resource(Users, '/users')
api.add_resource(Messages, '/messages')

@app.route('/')
def index():
    """
    Render the HTML page when navigated to http://localhost:8081
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host=HOST, port=CHAT_PORT, debug=True)





