from connection import connection	
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'
		
@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        c, conn = connection()
        return("okay")
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
   app.run()