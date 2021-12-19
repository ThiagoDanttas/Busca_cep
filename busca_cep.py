import requests


class BuscaCep:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('Cep Inválido!')

    def __str__(self):
        return self.acessa_via_cep()

    # validação de CEP
    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        return False

    # Retorna informações do cep | API
    def acessa_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return f"{dados['logradouro']}, {dados['bairro']}, {dados['localidade']}, {dados['uf']}, {dados['cep']}"

# Programa
cep_consulta = input('Insira o cep: ')
print(BuscaCep(cep_consulta))

