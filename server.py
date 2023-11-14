from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def test():
  return {"test": ["test1", "test2", "test3"]}

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)