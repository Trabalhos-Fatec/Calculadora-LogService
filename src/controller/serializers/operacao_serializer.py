class OperacaoSerializer:
    def serializer(self, operacao):
        return {
            'id_operacao': operacao.id_operacao,
            'tipo_operacao': operacao.tipo_operacao,
            'operacao_especifica': operacao.operacao_especifica
        }

    def serializerList(self, listOperacao):
        list_to_return = []

        for operacao in listOperacao:
            list_to_return.append(self.serializer(operacao))

        return list_to_return
