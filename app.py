from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Wayne Clinton, 2119113940, Sistem Informasi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
