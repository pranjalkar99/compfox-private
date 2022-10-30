from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def main():
    data = json.load(open("./static/data/data.json"))
    return render_template('index.html', data=data)

@app.route('/get_data')
def get_data():
    data = json.load(open("./static/data/data.json"))
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')