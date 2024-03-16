import csv
from datetime import datetime
import os.path
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from git import Repo

# Função para calcular o total gasto
def calcular_total_gasto(preco, gasto, quantidade):
    return preco * quantidade, gasto * quantidade

# Função para atualizar a tabela
def atualizar_tabela():
    tree.delete(*tree.get_children())
    for produto in dados:
        tree.insert('', 'end', values=(produto['id'], produto['nome'], produto['preço'], produto['gasto'], produto['data'], produto['quantidade'], produto['total'], produto['total_gastos'], produto['parcerias']))

# Função para adicionar um produto
def adicionar_produto():
    nome = entry_nome.get()
    preco = float(entry_preco.get())
    gasto = float(entry_gasto.get())
    data_input = entry_data.get()
    quantidade = int(entry_quantidade.get())
    parcerias = entry_parcerias.get()

    # Analisar a data e formatá-la como DD-MM-AAAA
    data = datetime.strptime(data_input, '%d%m%Y').strftime('%d-%m-%Y')

    total, total_gastos = calcular_total_gasto(preco, gasto, quantidade)
    
    dados.append({
        'id': len(dados) + 1,  # Adiciona o ID do produto
        'nome': nome,
        'preço': preco,
        'gasto': gasto,
        'data': data,
        'quantidade': quantidade,
        'total': total,
        'total_gastos': total_gastos,
        'parcerias': parcerias
    })

    atualizar_tabela()
    limpar_campos()

# Função para limpar os campos de entrada após adicionar um produto
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_gasto.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_parcerias.delete(0, tk.END)

# Função para enviar as mudanças para o repositório do GitHub
def enviar_mudancas():
    repo = Repo('/caminho/para/o/repo/do/github')
    repo.git.add('Doce Raiz.csv')
    repo.index.commit('Adicionando resultados à planilha')
    origin = repo.remote(name='origin')
    origin.push()

# Criar uma janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")

# Criar campos de entrada para os dados do produto
tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Preço:").grid(row=1, column=0)
entry_preco = tk.Entry(root)
entry_preco.grid(row=1, column=1)

tk.Label(root, text="Gasto:").grid(row=2, column=0)
entry_gasto = tk.Entry(root)
entry_gasto.grid(row=2, column=1)

tk.Label(root, text="Data (DDMMAAAA):").grid(row=3, column=0)
entry_data = tk.Entry(root)
entry_data.grid(row=3, column=1)

tk.Label(root, text="Quantidade:").grid(row=4, column=0)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=4, column=1)

tk.Label(root, text="Parcerias:").grid(row=5, column=0)
entry_parcerias = tk.Entry(root)
entry_parcerias.grid(row=5, column=1)

# Botão para adicionar produto
button_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
button_adicionar.grid(row=6, column=0)

# Botão para enviar mudanças para o GitHub
button_enviar = tk.Button(root, text="Enviar para GitHub", command=enviar_mudancas)
button_enviar.grid(row=6, column=1)

# Criar uma tabela para exibir os dados dos produtos
columns = ('ID', 'Nome', 'Preço', 'Gasto', 'Data', 'Quantidade', 'Total', 'Total Gastos', 'Parcerias')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=7, column=0, columnspan=2)

# Lista para armazenar os dados dos produtos
dados = []

# Iniciar o loop principal da interface gráfica
root.mainloop()
