from flask import Flask 

import os 
import socket

app = Flask(__name__) 

@app.route('/') 

def hello(): 
	return 'Hello IBM! I am now running on %s\n' % (socket.gethostname())

if __name__ == "__main__": 
	app.run(host="0.0.0.0", debug=True) 

