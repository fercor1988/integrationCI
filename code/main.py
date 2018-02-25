from flask import Flask
from flask import jsonify

app = Flask(__name__)

def buildmessaje(name,hostname):
	return "Hello "+name+" from "+hostname

@app.route("/hello/<string:name>", methods=['GET'])
def hello(name):
	messaje=buildmessaje(name,'127.0.0.1')
    	return jsonify(messaje)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=82) 
