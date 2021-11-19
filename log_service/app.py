from src import app, db
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix
from src.model.Operacao import Operacao
from src.model.Historico import Historico
from flask import Flask, request, jsonify
from urllib import parse, request as req

Migrate(app, db)

@app.route('/saveLog', methods=['POST'])
def logService():
    try:
        data_request = request.get_data()
        data_request = dict(parse.parse_qsl(data_request.decode('utf8')))
        historico = Historico(argumento=data_request['argumento'], resultado=data_request['resultado'], id_operacao=data_request['id_operacao'])
        db.session.add(historico)
        db.session.commit()

        return jsonify({ 'status': 'Success' }), 200

    except Exception as error:
        res = {'error': str(error)}
        
        return jsonify(res), 500

@app.route('/getOperacao', methods=['GET'])
def getOperacao():
    try:
        queryOperacao = request.args.get('operacao')
        operacao = Operacao.query.filter_by(operacao_especifica=queryOperacao).first()
        return jsonify({ 'id_operacao': operacao.id_operacao }), 200

    except Exception as error:
        res = {'error': str(error)}
        return jsonify(res), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)
