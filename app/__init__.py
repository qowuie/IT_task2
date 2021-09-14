from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	data = {
			'title': 'hello page',
			'username': 'Vasya'}
	return render_template('index.html', data=data)


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

