import csv
from datetime import datetime
import os.path
import subprocess
import tkinter as tk
from tkinter import messagebox

# Função para calcular o total gasto
def calcular_total_gasto(dados):
    total_gastos = sum(dado['total_gastos'] for dado in dados)
    return total_gastos

# Função principal
def main():
    def salvar_dados():
        # Salvar dados em um arquivo CSV
        with open('planilha.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id','nome','preço','gasto','data','quantidade','total','total_gastos','parcerias'])

            # Escreve o cabeçalho apenas se o arquivo estiver vazio
            if not arquivo_existente:
                writer.writeheader()

            for dado in dados:
                writer.writerow(dado)

        # Adiciona, commita e faz push das mudanças para o repositório do GitHub
        subprocess.run(["git", "add", "Doce Raiz.csv"])
        subprocess.run(["git", "commit", "-m", "Adicionando resultados à planilha"])
        subprocess.run(["git", "push", "origin", "main"])

        messagebox.showinfo("Sucesso", "Dados salvos em planilha.csv e enviados para o repositório do GitHub.")

    def adicionar_produto():
        nome = entry_nome.get()
        preco = float(entry_preco.get())
        gasto = float(entry_gasto.get())
        data_input = entry_data.get()

        # Analisar a data e formatá-la como DD-MM-AAAA
        data = datetime.strptime(data_input, '%d%m%Y').strftime('%d-%m-%Y')

        quantidade = int(entry_quantidade.get())
        parcerias = entry_parcerias.get()

        total = preco * quantidade
        total_gastos = gasto * quantidade
        
        dados.append({
            'id': id,  # Adiciona o ID do produto
            'nome': nome,
            'preço': preco,
            'gasto': gasto,
            'data': data,
            'quantidade': quantidade,
            'total': total,
            'total_gastos': total_gastos,
            'parcerias': parcerias
        })

        id += 1  # Incrementa o contador de ID

        messagebox.showinfo("Produto Adicionado", "Produto adicionado com sucesso.")

    # Inicialização da interface
    root = tk.Tk()
    root.title("Cadastro de Produtos")

    # Frame para o formulário de adição de produtos
    frame_formulario = tk.Frame(root)
    frame_formulario.pack(padx=10, pady=10)

    # Labels e Entry para os campos do formulário
    label_nome = tk.Label(frame_formulario, text="Nome:")
    label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_nome = tk.Entry(frame_formulario)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    label_preco = tk.Label(frame_formulario, text="Preço:")
    label_preco.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_preco = tk.Entry(frame_formulario)
    entry_preco.grid(row=1, column=1, padx=5, pady=5)

    label_gasto = tk.Label(frame_formulario, text="Gasto:")
    label_gasto.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_gasto = tk.Entry(frame_formulario)
    entry_gasto.grid(row=2, column=1, padx=5, pady=5)

    label_data = tk.Label(frame_formulario, text="Data (DDMMAAAA):")
    label_data.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entry_data = tk.Entry(frame_formulario)
    entry_data.grid(row=3, column=1, padx=5, pady=5)

    label_quantidade = tk.Label(frame_formulario, text="Quantidade:")
    label_quantidade.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    entry_quantidade = tk.Entry(frame_formulario)
    entry_quantidade.grid(row=4, column=1, padx=5, pady=5)

    label_parcerias = tk.Label(frame_formulario, text="Parcerias:")
    label_parcerias.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    entry_parcerias = tk.Entry(frame_formulario)
    entry_parcerias.grid(row=5, column=1, padx=5, pady=5)

    # Botão para adicionar produto
    btn_adicionar = tk.Button(frame_formulario, text="Adicionar Produto", command=adicionar_produto)
    btn_adicionar.grid(row=6, column=0, columnspan=2, pady=10)

    # Dados
    dados = []
    id = 1  # Inicializa o contador de ID

    # Verifica se o arquivo CSV já existe
    arquivo_existente = os.path.isfile('Doce Raiz.csv')

    # Botão para salvar dados e enviar para o GitHub
    btn_salvar = tk.Button(root, text="Salvar Dados e Enviar para GitHub", command=salvar_dados)
    btn_salvar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
