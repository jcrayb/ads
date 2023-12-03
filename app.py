from fetch.views import fetch

from flask import Flask, render_template
from init import initalize

app = Flask(__name__)
app.register_blueprint(fetch)

from flask_cors import CORS

CORS(app)

@app.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

@app.route('/')
def main():
    return render_template("test.html")

if __name__ == "__main__":
    initalize()
    app.run(host="0.0.0.0", port="1234", debug=True)