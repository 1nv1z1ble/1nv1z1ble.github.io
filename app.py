from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to our website!'

@app.route('/tos')
def tos():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    print(f'Your IP address is {ip_data}')
    return render_template('tos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
