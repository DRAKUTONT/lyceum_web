from flask import Flask, url_for

app = Flask(__name__)


@app.route('/promotion_image')
def handler_main():
    return f"""
        <!DOCTYPE HTML>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        </head>
        <body>
        <h1>Жди нас, Марс!</h1>
        <img src='{url_for('static', filename='img/mars.jpg')}'/>
        <div class="alert alert-primary" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-secondary" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-success" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-danger" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-warning" role="alert">
            Присоединяйся!
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
