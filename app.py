from flask import Flask, request
import os


def create_app():
    # app init
    PROJECT_ROOT = os.getcwd()
    os.environ['BASICWEB_PROJECT_ROOT'] = PROJECT_ROOT
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        message = 'Welcome team Blavor! Here is testing environment for Smart Scale.  ' + \
              '  Use /POST url to check your post parameters!'
        return message

    @app.route('/post', methods=['GET', 'POST'])
    def post_template():
        """ Here Print your post walues """
        if request.method == 'POST':
            print("Request data:", request.data)
            print("Request JSON:", request.get_json())
            print("Request form:", request.form)
            print("Request values:", request.values)
            return "Thanks for your post request!"
        elif request.method == 'GET':
            return "I think you want to use POST request?"

    return app
