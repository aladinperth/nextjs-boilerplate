from flask import Flask, request
app = Flask(__name__)

SCRIPT_CONTENT = """
-- Your Lua script here
print("Hello from hidden script!")
game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = 100
"""

@app.route("/")
def home():
    return "API is running", 200

@app.route("/get-script")
def get_script():
    executor_key = request.headers.get('X-Executor-Key')
    
    if not executor_key:
        return "Not Authorized", 403
    
    return SCRIPT_CONTENT
