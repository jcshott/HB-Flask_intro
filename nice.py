from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """Hi! This is the home page.
        <a href="/hello">Hello<a>
    """


# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet" method="POST">
                <label>What's your name? <input type="text" name="person"></label>
                <label>Choose a Compliment
                <select name="compliment">
                    <option value="awesome">awesome</option>
                    <option value="terrific">terrific</option>
                    <option value="coolio">coolio</option>
                    <option value="neato">neato</option>
                </select>
                </label>
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form.get("person")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)
    compliment = request.form.get("compliment")

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
    
