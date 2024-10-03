from veiculo import Carro, Moto
from pathlib import Path

def carregar():

    DIR = Path(__file__).parent
    FILE = DIR / 'dados.txt'

    veiculos = []
    with open(FILE, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            tipo, nome, ano, preço = linha.strip().split(',')
            ano = int(ano)
            preço = float(preço)
            if tipo == 'Carro':
                veiculos.append(Carro(nome, ano, preço))
            elif tipo == 'Moto':
                veiculos.append(Moto(nome, ano, preço)) 
    return veiculos

def main():

    veiculos = carregar()

    print('=------= Aluguel de Veículos =------=')
    print()
    print('Disponíveis:\n')

    c=1

    for veiculo in veiculos:
        print(f'{c} - Nome: {veiculo.nome:<30} Ano: {veiculo.ano:<30} Preço Diário: {veiculo.valor_diaria:<30}{veiculo.__class__.__name__}\n')
        c += 1
    while True:
        try:
            resposta = int(input('\nQual veículo deseja alugar ?[Número]: '))
        except:
            print(f'\nDigite um número válido entre 1 e {c - 1}!')
            continue
        else:
            if not 1 <= resposta <= c - 1:
                print(f'\nDigite um número válido entre 1 e {c - 1}!')
                continue
            resposta = int(resposta)
            break
    while True:
        try:
            dias = int(input('\nPor quantos dias deseja alugar ?: '))
        except:
            print('\nDigite um número inteiro positivo!')
        else:
            if dias < 0:
                print('\nDigite um número positivo!')
                continue
            break

    veiculo_selecionado = veiculos[resposta - 1]
    print(f'\nO preço total para o aluguel do {veiculo_selecionado.nome} será R${veiculo_selecionado.calcular_valor_aluguel(dias):.2f}')
    

main()

