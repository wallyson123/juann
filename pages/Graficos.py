import streamlit as st
import pandas as pd
import altair as alt

# Carregar o arquivo CSV
file_path = "penalties.csv"
df = pd.read_csv(file_path)

# Criar novas colunas para percentual de jardas em casa e fora
df['Home_Yards'] = df['Home_Count'] / df['Yards']
df['Away_Yards'] = df['Away_Count'] / df['Yards']

# Criar novas colunas para percentual de contagem em casa e fora
df['Home_Percentage'] = df['Home_Count'] / df['Count']
df['Away_Percentage'] = df['Away_Count'] / df['Count']

# Título do aplicativo Streamlit
st.title("Análise de Penalties")

# Adicionar filtro interativo na barra lateral
selected_name = st.sidebar.selectbox("Selecione um nome", df['Name'].unique())

# Filtrar o DataFrame com base no nome selecionado
filtered_df = df[df['Name'] == selected_name]

# Mostrar os dados brutos filtrados
st.subheader("Dados brutos filtrados")
st.write(filtered_df)

# Gráfico de barras para contagem de penalidades por nome
st.subheader("Contagem de penalidades por nome")
bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='Name',
    y='Count',
    color='Name',
    tooltip=['Name', 'Count']
).interactive()
st.altair_chart(bar_chart, use_container_width=True)

# Gráfico de dispersão para percentual de jardas por nome
st.subheader("Percentual de jardas por nome")
scatter_chart = alt.Chart(filtered_df).mark_circle().encode(
    x='Name',
    y='Home_Yards',
    color='Name',
    tooltip=['Name', 'Home_Yards']
).interactive()
st.altair_chart(scatter_chart, use_container_width=True)

# Gráfico de pizza para percentual de contagem de penalidades em casa
st.subheader("Percentual de penalidades em casa")
pie_chart_home = alt.Chart(filtered_df).mark_arc().encode(
    theta='Home_Percentage',
    color='Home_Percentage',
    tooltip=['Home_Percentage']
).interactive()
st.altair_chart(pie_chart_home, use_container_width=True)