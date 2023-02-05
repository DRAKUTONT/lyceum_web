from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
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
                        <title>Пейзажи марса</title>
                      </head>
                      <body>
                        <div class="container-sm">
                            <h1>Пейзажи Марса</h1>
                            <div id="carouselExample" class="carousel slide">
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="{url_for('static', filename='img/1.jpg')}" class="d-block" alt="">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for('static', filename='img/2.jpg')}" class="d-block" alt="">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for('static', filename='img/3.jpg')}" class="d-block" alt="">
                                </div>
                              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                              </button>
                              <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                              </button>
                            </div>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js" integrity="sha384-mQ93GR66B00ZXjt0YO5KlohRA5SY2XofN4zfuZxLkoj1gXtW8ANNCe9d5Y3eG5eD" crossorigin="anonymous"></script>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
