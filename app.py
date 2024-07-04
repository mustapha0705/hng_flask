from flask import Flask, request, jsonify
# import requests

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr
    
    location = "New York"
    temperature = 11
    
    greeting = f'Hello {visitor_name}! the temperature is {temperature} degrees Celcius in {location}'
    
    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
