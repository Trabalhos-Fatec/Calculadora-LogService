class HistoricoSerializer:
    def serializer(self, historico):
        return {
            'id_historico': historico.id_historico,
            'id_operacao': historico.id_operacao,
            'argumento': historico.argumento,
            'resultado': historico.resultado,
            'dt_registro': historico.dt_registro
        }

    def serializerList(self, listHistorico):
        list_to_return = []

        for historico in listHistorico:
            list_to_return.append(self.serializer(historico))

        return list_to_return
