from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def handler_main():
    names = ['Леонадро Ди Каприо', 'Джони Кэш', 'Шрек', 'Осел', 'Эдварт Нортон', 'Авраам Линкольн']
    return render_template('distribution.html', title='Размещение', names=names)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
