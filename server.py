from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.return_table_headers()

    return render_template('list.html', user_stories=user_stories)

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True
    )
