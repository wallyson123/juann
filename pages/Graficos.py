import streamlit as st
import pandas as pd
import altair as alt

# Carregar o arquivo CSV
file_path = "penalties.csv"
df = pd.read_csv(file_path)

# Título do aplicativo Streamlit
st.title("Análise de Penalties")

# Mostrar os dados brutos
st.subheader("Dados brutos")
st.write(df)

# Gráfico de barras para contagem de penalidades por nome
st.subheader("Contagem de penalidades por nome")
bar_chart = alt.Chart(df).mark_bar().encode(
    x='Name',
    y='Count',
    color='Name',
    tooltip=['Name', 'Count']
).interactive()
st.altair_chart(bar_chart, use_container_width=True)

# Gráfico de dispersão para jardas por nome
st.subheader("Jardas por nome")
scatter_chart = alt.Chart(df).mark_circle().encode(
    x='Name',
    y='Yards',
    color='Name',
    tooltip=['Name', 'Yards']
).interactive()
st.altair_chart(scatter_chart, use_container_width=True)

# Gráfico de pizza para contagem de penalidades em casa
st.subheader("Contagem de penalidades em casa")
pie_chart_home = alt.Chart(df).mark_arc().encode(
    theta='Home_Count',
    color='Home_Count',
    tooltip=['Home_Count']
).interactive()
st.altair_chart(pie_chart_home, use_container_width=True)