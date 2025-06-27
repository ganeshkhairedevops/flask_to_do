from flask import Flask, request, render_template, url_for
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.flask_database

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():
  
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)

    collection.insert_one(form_data)
    #print(form_data)

    return 'Data Submited Successfully'

@app.route('/api')
def api():

    data = collection.find()

    data = list(data)
    for item in data:
        print(item)

        del item["_id"]
    data = {
        'data' : data
    }
  
    return data

if __name__ == '__main__':

    app.run(debug=True)