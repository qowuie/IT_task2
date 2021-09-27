from flask import Flask, render_template, request
import requests, uuid, json, os


path = '/translate'

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['ru']
}


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
            "laptop": "ноутбук",
            "homework": "домашняя работа",
            "cup": "кружка",
            "glass": "стекло",
            "sand": "песок",
            "net": "сеть",
            "window": "окно", }


# @app.route('/dict', methods=['GET', 'POST'])
# def dict_page():
#     if request.method == 'POST':
#         if my_words.get(request.form["word"].lower()):
#             data = {"word": my_words[request.form["word"].lower()],
#                     "eng_word": request.form["word"].lower(), }
#         else:
#             data = {"word": "There is no word like that",
#                     "eng_word": "", }
#         return render_template('dict.html', data=data)
#     return render_template('dict.html')


@app.route('/translate', methods=['GET', 'POST'])
def index_post():
    if request.method == 'POST':
        lang_from = request.form['language_from']
        lang_to = request.form['language_to']
        print(lang_from, lang_to)
        original_text = request.form['word']
        key = "93cee1d75af34bd4a6b81c1f486089b5"
        endpoint = "https://api.cognitive.microsofttranslator.com"
        location = "germanywestcentral"


        path = '/translate?api-version=3.0&'

        target_language_parameter = 'from=' + lang_from + '&to=' + lang_to

        constructed_url = endpoint + path + target_language_parameter

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }


        body = [
            {
                'text': original_text
            }
        ]

        translator_request = requests.post(
            constructed_url, headers=headers, json=body)

        translator_response = translator_request.json()
        translated_text = translator_response[0]['translations'][0]['text']

        data = {'word_ru': original_text,
                'word_eng': translated_text}
        return render_template('dict.html', data=data)
    return render_template('dict.html')


# @app.route('/messages')
# def messages():
#     data = {
#         'title': 'Сообщения',
#         'username': 'Vasya',
#         'messages': [
#             {'author': 'Jack', 'body': 'massage1'},
#             {'author': 'swf', 'body': 'massage2'},
#             {'author': 'rgh', 'body': 'massage3'},
#             {'author': 'fbg', 'body': 'massage4'},
#             {'author': 'wefe', 'body': 'massage5'},
#         ]
#     }
#     return render_template('messages.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
