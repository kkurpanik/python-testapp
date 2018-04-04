from flask import Flask 
from redis import Redis 

import os 
import socket

app = Flask(__name__) 
redis = Redis(host='redis', port=6379) 

@app.route('/') 

def hello(): 
	redis.incr('hits') 
	return 'Hello IBM! I have been seen %s times and I am now running on %s\n' % (redis.get('hits'), socket.gethostname())

if __name__ == "__main__": 
	app.run(host="0.0.0.0", debug=True) 

