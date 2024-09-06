import requests

def sobre_pokemons(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    retorno = requests.get(url)
    pokemons = retorno.json()

    # Movimentos
    print('\nMOVIMENTOS:----------------')
    for movimento in pokemons['moves']:
        print(movimento['move']['name'])

    # Jogos
    print('\nJOGOS:----------------')
    for jogo in pokemons['game_indices']:
        print(jogo['version']['name'])

    # Chama a função evoluções dentro da função sobre_pokemons
    evolucoes(pokemon)


def evolucoes(pokemon):
    # Obtenção das informações da espécie do Pokémon
    url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/'
    retorno = requests.get(url)
    dados_pokemons = retorno.json()

    # Acessar a URL da cadeia de evolução
    acessar_api_evolucao = dados_pokemons['evolution_chain']['url']
    dados = requests.get(acessar_api_evolucao)
    evolucoes_pk = dados.json()

    # Função recursiva para percorrer a cadeia de evoluções
    def imprimir_evolucoes(chain):
        print(chain['species']['name'])  # Nome do Pokémon atual
        for evolucao in chain['evolves_to']:
            imprimir_evolucoes(evolucao)  # Chama recursivamente para cada evolução

    print('\nEVOLUÇÕES:----------------')
    imprimir_evolucoes(evolucoes_pk['chain'])


sobre_pokemons('charmander')