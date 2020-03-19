# checkYourRequests
Check your request using this web app!

## Installation of webapp
  - Install [Python](https://www.python.org/downloads/) and [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) on your machine
  - Setup your virtual environment
  - Clone the repository `$ git clone git@github.com:tokicnikolaus/checkYourRequests.git`
  - Change into the directory `$ cd path/checkYourRequests`
  - Install all required dependencies listed in requirements.txt file with `$ pip install -r requirements.txt` command
  - Start the application by running `python run.py` in same directory!
  
 ## Expose your port for public network
 
  - Download [ngrok](https://dashboard.ngrok.com/get-started) - you need to login and follow the instructions
  - After successful download run the ngrok binary: `./ngrok http 8000` 8000 - is the port on which web app is running
  - Now you can test the requests over public network!

  

