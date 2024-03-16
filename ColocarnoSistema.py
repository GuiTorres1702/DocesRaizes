import csv
from datetime import datetime
import os.path
import subprocess

# Função para calcular o total gasto
def calcular_total_gasto(dados):
    total_gastos = sum(dado['total_gastos'] for dado in dados)
    return total_gastos

# Função principal
def main():
    dados = []
    id_produto = 1  # Inicializa o contador de ID

    # Verifica se o arquivo CSV já existe
    arquivo_existente = os.path.isfile('Doce Raiz.csv')

    if arquivo_existente:
        # Se o arquivo já existe, carrega os dados existentes
        with open('Doce Raiz.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dados.append(row)
            # Define o próximo ID a ser utilizado
            id_produto = int(dados[-1]['id']) + 1

    continuar = True
    while continuar:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        gasto = float(input("Digite o gasto com o produto: "))
        data_input = input("Digite a data da compra (DDMMAAAA): ")

        # Analisar a data e formatá-la como DD-MM-AAAA
        data = datetime.strptime(data_input, '%d%m%Y').strftime('%d-%m-%Y')

        quantidade = int(input("Digite a quantidade comprada: "))
        parcerias = input("Digite as parcerias (separadas por vírgula): ")

        total = preco * quantidade
        total_gastos = gasto * quantidade
        
        dados.append({
            'id': id_produto,  # Adiciona o ID do produto
            'nome': nome,
            'preço': preco,
            'gasto': gasto,
            'data': data,
            'quantidade': quantidade,
            'total': total,
            'total_gastos': total_gastos,
            'parcerias': parcerias
        })

        id_produto += 1  # Incrementa o contador de ID

        continuar_input = input("Deseja inserir mais um produto? (s/n): ")
        if continuar_input.lower() != 's':
            continuar = False

    # Salvar dados em um arquivo CSV
    with open('Doce Raiz.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id','nome','preço','gasto','data','quantidade','total','total_gastos','parcerias'])

        # Escreve o cabeçalho apenas se o arquivo estiver vazio
        if not arquivo_existente:
            writer.writeheader()

        for dado in dados:
            writer.writerow(dado)

    print("Dados salvos em Doce Raiz.csv")

    # Adiciona, commita e faz push das mudanças para o repositório do GitHub
    subprocess.run(["git", "add", "Doce Raiz.csv"])
    subprocess.run(["git", "commit", "-m"])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    main()
