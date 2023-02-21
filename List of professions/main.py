from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<string:list_type>')
def handler_main(list_type):
    prof_list = ['Врач', 'Инженер', 'Строитель', 'Уборщик', 'Программист', 'QA', 'Генеральный директор']
    return render_template('base.html', list_type=list_type, prof_list=prof_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
