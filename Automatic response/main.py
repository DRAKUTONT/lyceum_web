from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def handler_main():
    data = {
        'title': 'Анкета',
        'surname': 'Петрович',
        'name': 'Иван',
        'education': 'Высшее',
        'profession': 'Сантехник',
        'sex': 'male',
        'motivation': 'Хочу чинить сантехнику на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
