from flask import Flask, request, render_template
from ldatest import returnTopics

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def searchTopic():
    return render_template('base.html')


@app.route('/bubbles', methods=['GET', 'POST'])
def searchResults():
    s1 = request.form['s1']
    output = returnTopics(s1)
    return render_template('bubbles.html', result=output)


if __name__ == '__main__':
    app.run()
