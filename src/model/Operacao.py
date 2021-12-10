from src import db

class Operacao(db.Model):
    __tablename__= 'operacao'
    id_operacao = db.Column(db.Integer, primary_key=True)
    tipo_operacao = db.Column(db.String(15), nullable=False)
    operacao_especifica = db.Column(db.String(15), nullable=False)

    def _init_(self, id_operacao, tipo_operacao, operacao_especifica):
        self.id_operacao = id_operacao
        self.tipo_operacao = tipo_operacao
        self.operacao_especifica = operacao_especifica


    def _repr_(self):
        return json.dumps({
            'id_operacao': self.id_operacao,
            'tipo_operacao': self.tipo_operacao,
            'operacao_especifica': self.operacao_especifica
        })
