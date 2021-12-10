from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib import parse, request as req
import json


app = Flask(__name__)
CORS(app)


# This simulates service data that should come from database or
# configuration file.
soma_service = {'operation':'/soma', 'address':'localhost', 'port':5000, 'route':'/soma'}
subtracao_service = {'operation':'/subtracao', 'address':'localhost', 'port':5001, 'route':'/subtracao'}
cosseno_service = {'operation':'/cosseno', 'address':'localhost', 'port':5002, 'route':'/cosseno'}
cossecante_service = {'operation':'/cossecante', 'address':'localhost', 'port':5002, 'route':'/cossecante'}
get_operacao_service = {'operation':'/getOperacao', 'address':'localhost', 'port':5005, 'route':'/getOperacao'}
get_historico_service = {'operation':'/getHistorico', 'address':'localhost', 'port':5005, 'route':'/getHistorico'}
service_registry = [soma_service, subtracao_service, cosseno_service, cossecante_service, get_operacao_service, get_historico_service]

def convertRequestArgsToDict(listParameters):
    dictToReturn = {}

    for parameters in listParameters:
        dictToReturn[parameters] = listParameters[parameters]

    return dictToReturn

def get_id_operacao(tipo_operacao):
    parameters = { 'operacao': tipo_operacao }
    url = 'http://localhost:5005/getOperacao'
    url_request = req.urlopen(url+'?'+parse.urlencode(parameters))
    result = url_request.read()
    result = json.loads(result.decode('utf8'))

    return result['id_operacao']

def save_log(data_request, tipo_operacao):
    data_request = json.loads(data_request.decode('utf8'))
    id_operacao = get_id_operacao(tipo_operacao)

    data = {
        'id_operacao': id_operacao,
        'argumento': data_request['argumento'],
        'resultado': data_request['resultado']
    }

    url = 'http://localhost:5005/saveLog'
    data = parse.urlencode(data).encode()
    url_request = req.urlopen(url, data=data)

@app.route('/api_gateway/<operation>', methods=['GET', 'POST', 'PUT'])
def api_gateway(operation):
    list_service_get = ['getHistorico', 'getOperacao']

    for service_config in service_registry:
        if service_config['operation'] == ('/'+operation):
            url = 'http://' + service_config['address'] +':' + str(service_config['port']) + service_config['route']

            if operation in list_service_get:
                parameters = request.args
                url_request = req.urlopen(url+'?'+parse.urlencode(convertRequestArgsToDict(parameters)))
                result = url_request.read()

            else:
                data = parse.urlencode(request.json).encode()
                url_request = req.urlopen(url, data=data)

                result = url_request.read()
                save_log(result, operation)

            return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
