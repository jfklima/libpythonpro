class Enviador:
    def enviar(self, remetente, destinatário, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f"Email do remetente inválido {remetente}")
        return remetente


class EmailInvalido(Exception):
    pass
