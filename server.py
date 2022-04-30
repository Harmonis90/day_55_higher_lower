from flask import Flask
import random

answer = random.randint(0, 10)
server = Flask(__name__)


@server.route("/")
def get_homepage():
    return f'<h1 style= "text-align: center">GUESS A NUMBER BETWEEN 0 AND 9!</h1>' \
           f'<p style= "text-align: center"><img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></p>'


@server.route("/<n>")
def check_user_input(n):
    num = int(n)
    if num == answer:
        return f'<p style= "text-align: center"><img src= ' \
               f'"https://media.giphy.com/media/UXgf6pu1LlQp6CPDi0/giphy.gif"></p>'
    elif num < answer:
        return f'<h1 style= "text-align: center">HIGHER</h1>' \
               f'<p style= "text-align: center"><img src= ' \
               f'"https://media.giphy.com/media/PR3585ZZSvcHO9pa76/giphy.gif"></p>'
    else:
        return f'<h1 style= "text-align: center">LOWER</h1>' \
               f'<p style= "text-align: center"><img src= ' \
               f'"https://media.giphy.com/media/gZLl9szOpgbpS/giphy.gif"></p>'


if __name__ == "__main__":
    server.run(debug=True)
