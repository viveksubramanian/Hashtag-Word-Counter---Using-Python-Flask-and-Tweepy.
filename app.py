# Working URL Example: http://127.0.0.1:5000/rest?hashtag=trump&duration=20 - Replace Trump with any other word and
# 20 seconds with any other duration in seconds
# http://127.0.0.1:5000/home - home page
# http://127.0.0.1:5000/about - about page
# Error Handling to be added - duration value of not an integer will crash

import tweetcollector as tc
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# Route to get a response for a hashtag
@app.route('/rest', methods=['GET'])
def rest():
    hashtag = request.args.get('hashtag')
    duration = int(request.args.get('duration'))

    my_result = tc.SetupTweetCollector(hashtag, duration)

    return jsonify(my_result.retrieve())


# Home page route
@app.route('/home')
def home():
    return render_template('home.html')


# About page route
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
