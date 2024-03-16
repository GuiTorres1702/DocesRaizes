import pandas as pd
import streamlit as st
import plotly_express as px

# Leitura do Arquivo
dataframe = pd.read_csv('Doce Raiz.csv', index_col=0)

# Configurações
st.set_page_config(
    page_title="DOCES RAIZES",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Barra de seleção de atributos
nome_options = dataframe["nome"].unique().tolist()
preço_options = dataframe["preço"].unique().tolist()
gasto_options = dataframe["gasto"].unique().tolist()
data_options = dataframe["data"].unique().tolist()
quantidade_options = dataframe["quantidade"].unique().tolist()
total_options = dataframe["total"].unique().tolist()
total_gastos_options = dataframe["total_gastos"].unique().tolist()
parcerias_options = dataframe["parcerias"].unique().tolist()

nome = st.sidebar.multiselect(
    key=1,
    label="Produtos",
    options=nome_options,
    default=nome_options
)
preço = st.sidebar.multiselect(
    key=2,
    label="Preço de Vendas",
    options=preço_options,
    default=preço_options
)
gasto = st.sidebar.multiselect(
    key=3,
    label="Gastos com Produto",
    options=gasto_options,
    default=gasto_options
)
data = st.sidebar.multiselect(
    key=4,
    label="Data de Pedido",
    options=data_options,
    default=data_options
)
quantidade = st.sidebar.multiselect(
    key=5,
    label="Quantidade de Pedido",
    options=quantidade_options,
    default=quantidade_options
)
total = st.sidebar.multiselect(
    key=6,
    label="Total de Vendas por Produto",
    options=total_options,
    default=total_options
)
total_gastos = st.sidebar.multiselect(
    key=7,
    label="Total de Gastos por Produto",
    options=total_gastos_options,
    default=total_gastos_options
)
parcerias = st.sidebar.multiselect(
    key=8,
    label="Parcerias de Venda",
    options=parcerias_options,
    default=parcerias_options
)

# Filtro da seleção de atributos
filtered_data = dataframe[
    (dataframe["nome"].isin(nome)) &
    (dataframe["preço"].isin(preço)) &
    (dataframe["gasto"].isin(gasto)) &
    (dataframe["data"].isin(data)) &
    (dataframe["quantidade"].isin(quantidade)) &
    (dataframe["total"].isin(total)) &
    (dataframe["total_gastos"].isin(total_gastos)) &
    (dataframe["parcerias"].isin(parcerias))
]

#----------------------------------Total de vendas---------------------------------------------------
total_de_vendas = round(filtered_data["total"].sum(), 2)
total_de_gastos = round(filtered_data["total_gastos"].sum(), 2)
Lucro_total = round(filtered_data["Lucro total"].sum(),2)
#----------------------------------print total metrica-----------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", total_de_vendas)
col2.metric("Total de Gastos", total_de_gastos)
col3.metric("Lucro total", Lucro_total)

# ---------------------------------Visual do site TxT-------------------------------------------------
st.header("📉Analise de Lucros - Doces Raizes🍬")

st.markdown("""---""")

# ----------------------------------- Gráfico de Vendas por Data -----------------------------------
vendas_por_data = dataframe.groupby('data').sum().reset_index()
fig_vendas_por_data = px.area(vendas_por_data, x='data', y='total', title='Vendas por Data', color_discrete_sequence=['#E9C46A'])


# ----------------------------------- Gráfico de Vendas por Quantidade -----------------------------------
vendas_por_quantidade = dataframe.groupby('quantidade').sum().reset_index()
fig_vendas_por_quantidade = px.bar(vendas_por_quantidade, x='quantidade', y='total', title='Vendas por Quantidade', color_discrete_sequence=['#E9C46A'])
#-------------------------------------Gráfico de vendas com parcerias------------------------------------------------
vendas_por_parcerias = dataframe.groupby('parcerias').sum().reset_index()
fig_vendas_por_parcerias = px.bar(vendas_por_data, x='parcerias', y='total', title='Vendas por Parceria', color_discrete_sequence=['#E9C46A'])
#--------------------------------------------------------------------------------------------------------------------

col1, col2,col3 = st.columns(3)
col1.plotly_chart(fig_vendas_por_data)
col2.plotly_chart(fig_vendas_por_quantidade)
col3.plotly_chart(fig_vendas_por_parcerias)
#--------------------------------------Print do arquivo------------------------------------------------
st.dataframe(filtered_data, width=10000)
