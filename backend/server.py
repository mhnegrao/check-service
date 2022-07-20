from flask import Flask, send_from_directory
import psutil
import json

app = Flask(__name__)

# path para main page Svelte


@app.route('/')
def base():
    return send_from_directory('frontend/client/public', 'index.html')


@app.route('/home')
def hello():
    return 'Home do App'


@app.route('/checkservice')
def check_service():
    response = None
    json_data = None
    service = getService('Sys')

    json_data = json.dumps(service, indent=4)
    if service:
        response = "Serviço encontrado!"
    else:
        response = "Serviço não encontrado!!!"

    if service and service['status'] == 'running':
        return json_data
    else:
        return f"{response} - Serviço não está rodando!!!"


def getService(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service


if __name__ == '__main__':
    app.run(debug=True)
