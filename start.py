from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello from Docker container!"
if __name__ == "__main__":
        app.run(threaded=True,debug=True,host='0.0.0.0')