import requests

# Consumindo dados de uma API para retornar o endereço através do cep
def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    retorno = requests.get(url)
    info = retorno.json()

# 1 Informando somente dados selecionados por mim para exibir
    logradouro = info['logradouro']
    bairro = info['bairro']
    local = info["localidade"]
    uf = info['uf']
    print(f'{logradouro}, {bairro}, {local} - {uf}')

# 2 Percorrendo todas as informações dos dados da api
    for keys, values in info.items():
        print(f'{keys}: {values}')


consultar_cep('02877160')