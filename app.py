from flask import Flask, request, jsonify # imports statement syntax for Python
from games import Games # imports our simpleton dictionary from the games.py file

app = Flask(__name__) # Tells you this app is built by the 'Flask' framework.
# __name__ is a special variable in Python that holds the name of the file, by default it is set to '__main__ ' when running the file 

@app.route("/", methods=["GET"])
def test():
    if request.method == "GET":
        return jsonify({"response": "Hello There!"})
    
# GET request to retrieve all games 
@app.route("/games", methods=["GET"])
def get_games():
    return jsonify(Games) 

# GET request to retrieve a game by it's positon
@app.route("/games/<int:position>", methods=["GET"])
def get_game(position):  

# POST request to add a new game
@app.route("", methods=)
def add_game():

# DELETE request to delete a game by position
@app.route("", methods=)
def delete_game():
    
# PUT request to ammend an entire game
@app.route("", methods=)
def replace_game():
    
# PATCH request to partialy ammend a game
@app.route("", methods=)
def update_game():
        return jsonify({"message": "Game not found"}), 404  
    
if __name__ == "__main__":
    app.run(debug=True) # if *insert name of file* is our main file run the app in debug mode
    # this is Python's equivalent of npm run dev, it refereshes the server after each change.
