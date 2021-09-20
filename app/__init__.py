from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    data = {
        'title': 'hello page',
        'username': 'Vasya'}
    return render_template('index.html', data=data)


@app.route('/hello/<name>')
def hello_with_name(name):
    return f'Hello {name}'


my_words = {"hello": "привет",
            "car": "машина",
			"cat": "кошка",
			"python": "питон",
			"minesweeper": "сапер",
			"mouse": "мышь",
			"laptop": "ноутбук", }


@app.route('/dict', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = my_words[request.form["word"].lower()]
        return render_template('result.html', word=word)
    return render_template('dict.html')


@app.route('/messages')
def messages():
    data = {
        'title': 'Сообщения',
        'username': 'Vasya',
        'messages': [
            {'author': 'Jack', 'body': 'massage1'},
            {'author': 'swf', 'body': 'massage2'},
            {'author': 'rgh', 'body': 'massage3'},
            {'author': 'fbg', 'body': 'massage4'},
            {'author': 'wefe', 'body': 'massage5'},
        ]
    }
    return render_template('messages.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
