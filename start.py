from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "I was built in jenkins and run in docker. version 7"
if __name__ == "__main__":
        app.run(threaded=True,debug=True,host='0.0.0.0')