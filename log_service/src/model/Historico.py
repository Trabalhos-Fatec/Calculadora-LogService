from src import db
from src.model import Operacao
from datetime import datetime
import json

class Historico(db.Model):

    __tablename__= 'historico'
    id_historico = db.Column(db.Integer, primary_key=True)
    argumento = db.Column(db.String(15), nullable=False)
    resultado = db.Column(db.String(15), nullable=False)
    dt_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_operacao = db.Column(db.Integer, db.ForeignKey('operacao.id_operacao'), nullable=False)

    def __init__(self, id_operacao, argumento, resultado):
        self.argumento = argumento
        self.resultado = resultado
        self.id_operacao = id_operacao


    def __repr__(self):
        return json.dumps({
            'id_historico': self.id_historico,
            'id_operacao': self.id_operacao,
            'argumento': self.argumento,
            'resultado': self.resultado,
            'dt_registro': self.dt_registro
            })
