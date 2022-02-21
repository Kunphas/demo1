#main.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from host'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
© 2022 GitHub, Inc.
Terms
Privacy
Security
