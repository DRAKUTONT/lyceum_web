from flask import Flask, url_for

app = Flask(__name__)


@app.route('/astronaut_selection')
def handler_main():
    return f'''<!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Отбор Астронавтов</title>
                      </head>
                      <body>
                        <h1>Анкета претендента на участие в миссии</h1>
                        <div>
                            <form class="login_form" method="post">
                                <input type="text" class="form-control" placeholder="Введите фамилию" aria-label="Username" aria-describedby="basic-addon1" name='surname'>
                                <input type="text" class="form-control" placeholder="Введите имя" aria-label="Username" aria-describedby="basic-addon1" name='name'>
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                <div class="form-group">
                                    <label for="classSelect">Какое у вас образование?</label>
                                    <select class="form-control" id="classSelect" name="education">
                                      <option>начальное</option>
                                      <option>среднее</option>
                                      <option>высшее</option>
                                    </select>
                                </div>
                                <div class="form-group">
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">
                                            пилот
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">
                                            врач
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">
                                            инженер
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">
                                            экзобиолог
                                        </label>
                                    </div>
                                    
                                </div>
                                <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label for="about">Почему вы хотите принять участие в миссии</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                </div>
                                <button type="submit" class="btn btn-primary">отправить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
