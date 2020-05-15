from flask import *
from flask_restful import Resource, Api, reqparse
from datetime import *
import string
import random

# Notes:
# currentTime = datetime.now()

# intialization
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

# Data Base
ROOMS = {}
TOKENS = {}
CONNECTIONS = {}
TRANSFERS = {}
SYNCER = {}
global STARTED
STARTED = False
global BEGINING
BEGINING = True
W_TURN = True
FLAG = False


# HTTP functions
class Connect(Resource):
    # ask for connection (from server - An "open room" request)
    # gets name, returns room num
    def get(self):
        # Get User's Name
        parser.add_argument('name')
        args = parser.parse_args()
        if not args['name']:
            args['name'] = "Anonymous"
        # get user ip
        ip =  request.environ['REMOTE_ADDR']
        # create room number
        roomNum = random.randint(1, 1000)
        while roomNum in ROOMS:
            roomNum = random.randint(1, 1000)
        TRANSFERS[roomNum] = []
        # create password
        letters = string.ascii_lowercase
        password = ''.join(random.choice(letters) for i in range(4))
        while password in (ROOMS, args):
            password = ''.join(random.choice(letters) for i in range(4))
        # create the room
        ROOMS[roomNum] = [args['name'], ip, password, False]
        # create a token for the user re login
        TOKENS[ip] = roomNum
        # sends back the room number and its password
        answer = [roomNum, password]
        return jsonify(answer)
        

    # ask to connect (from client - A "join room" request)
    def post(self):
        # Get User's Name
        parser.add_argument('name')
        args = parser.parse_args()
        if not args['name']:
            args['name'] = "Anonymous"
        # it hurts when ip
        ip =  request.environ['REMOTE_ADDR']
        # get the room number he asks for
        parser.add_argument('room')
        args = parser.parse_args()
        if int(args['room']) not in ROOMS:
            return "The Room Wasn't Found", 404
        # check password
        parser.add_argument('password')
        args = parser.parse_args()
        if str(args['password']) not in ROOMS[int(args['room'])]:
            return "Your Password Was Incorrect", 401
        # log the client to the room
        ROOMS[int(args['room'])].append(args['name'])
        ROOMS[int(args['room'])].append(ip)
        ROOMS[int(args['room'])][3] = True
        # create a token for the user re login
        TOKENS[ip] = int(args['room'])
        # return the other player's name and ip
        return [ROOMS[int(args['room'])][0], ROOMS[int(args['room'])][1]]


# waiting room - waiting for the other player
class Approval(Resource):
    def get(self):
        # check for previous entry token - saved by ip
        ip =  request.environ['REMOTE_ADDR']
        if ip not in TOKENS:
            return "Unauthorized", 401
        # get the room number
        roomNum = TOKENS[ip]
        # check the room number is correct
        if roomNum not in ROOMS.keys():
            return "Bad Request", 400
        if len(ROOMS[roomNum]) == 6:
            return [True, ROOMS[roomNum][-2], ROOMS[roomNum][-1]]
        else:
            return [False, "", ""]

# syncs the players games
class Sync(Resource):
    # get move
    def get(self):
        global FLAG
        # check for previous entry token - saved by ip
        ip = request.environ['REMOTE_ADDR']
        # connect to the correct connection room
        roomNum = TOKENS[ip]
        if roomNum not in TRANSFERS.keys():
            return "Bad Request", 400
        if not FLAG:
            return [False, [0, 0, 0, 0]]
        else:
            FLAG = False
            return [True, TRANSFERS[roomNum]]
        
    # send move
    def post(self):
        global FLAG
        # check for previous entry token - saved by ip
        ip =  request.environ['REMOTE_ADDR']
        if ip not in TOKENS:
            return "Unauthorized", 401
        roomNum = TOKENS[ip]
        TRANSFERS[roomNum] = []
        # get move info from request
        parser.add_argument('move_x')
        parser.add_argument('move_y')
        parser.add_argument('was_x')
        parser.add_argument('was_y')
        args = parser.parse_args()
        moves = [args['was_x'], args['was_y'], args['move_x'], args['move_y']]
        TRANSFERS[roomNum] = moves
        FLAG = True
        return True
        
        


# internal functions


        


# manage resources
api.add_resource(Connect, '/connection/')
api.add_resource(Approval, '/approve/')
api.add_resource(Sync, '/sync/')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5000)