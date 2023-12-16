import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo CSV
file_path = "penalties.csv"
penalties_data = pd.read_csv(file_path)

# Configurações iniciais do Streamlit
st.title("Informações sobre Penalidades na NFL")
st.sidebar.title("Filtros")

# Filtros
selected_year = st.sidebar.selectbox("Selecione o Ano", penalties_data["Year"].unique())
selected_week = st.sidebar.selectbox("Selecione a Semana", penalties_data["Week"].unique())

# Aplicar filtros
filtered_data = penalties_data[(penalties_data["Year"] == selected_year) & (penalties_data["Week"] == selected_week)]

# Exibir tabela com os resultados
st.write("Dados Filtrados:")
st.write(filtered_data)

# Número total de tabelas, colunas e quantidade geral
num_tables = len(filtered_data)
num_columns = len(filtered_data.columns)
total_penalties = filtered_data["Count"].sum()

st.write(f"Número Total de Tabelas: {num_tables}")
st.write(f"Número Total de Colunas: {num_columns}")
st.write(f"Quantidade Geral de Penalidades: {total_penalties}")

# Gráfico de barras para contagem de penalidades por time
st.write("Contagem de Penalidades por Time:")
penalty_counts = filtered_data.groupby("Name")["Count"].sum().sort_values(ascending=False)
st.bar_chart(penalty_counts)

# Gráfico de pizza para mostrar a distribuição de penalidades em casa, fora, etc.
st.write("Distribuição de Penalidades:")
penalty_distribution = filtered_data[["Home_Count", "Away_Count", "Off_Count", "Def_Count", "ST_Count"]].sum()
fig = px.pie(
    names=penalty_distribution.index,
    values=penalty_distribution.values,
    labels=penalty_distribution.index,
    title="Distribuição de Penalidades"
)
st.plotly_chart(fig)