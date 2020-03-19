import os

from app import create_app



if __name__ == '__main__':

    #env_name = os.getenv('BEESITE_ENV')
    #print("Environment:", env_name)
    app = create_app()
    # run app
    # app.run(ssl_context='adhoc')
    app.run(port=8000, debug=True)

