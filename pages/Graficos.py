import streamlit as st
import pandas as pd
import altair as alt

# Carregar o arquivo CSV
file_path = "penalties.csv"
df = pd.read_csv(file_path)

# Criar novas colunas para percentual de jardas em casa e fora
df['Home_Yards_Percentage'] = df['Home_Yards'] * 100
df['Away_Yards_Percentage'] = df['Away_Yards'] * 100

# Criar novas colunas para percentual de contagem em casa e fora
df['Home_Percentage'] = df['Home_Count'] / df['Count'] * 100
df['Away_Percentage'] = df['Away_Count'] / df['Count'] * 100

# Título do aplicativo Streamlit
st.title("Análise de Penalties")

# Adicionar filtro interativo na barra lateral
selected_team = st.sidebar.selectbox("Selecione um time", df['Name'].unique())

# Filtrar o DataFrame com base no time selecionado
filtered_df = df[df['Name'] == selected_team]

# Mostrar os dados brutos filtrados
st.subheader("Dados brutos filtrados")
st.write(filtered_df)

# Gráfico de barras para percentual de jardas em casa e contagem em casa
st.subheader("Percentual de Jardas e Contagem em Casa por Time")
bar_chart_home = alt.Chart(filtered_df).mark_bar(opacity=0.7).encode(
    x=alt.X('Name:N', title='Time'),
    y=alt.Y('Home_Yards_Percentage:Q', axis=alt.Axis(format='%')),
    color=alt.Color('Name:N', scale=alt.Scale(scheme='category20')),
    tooltip=['Name', 'Home_Yards_Percentage', 'Home_Percentage']
).properties(width=600, height=400)

bar_chart_home_count = alt.Chart(filtered_df).mark_bar(opacity=0.7).encode(
    x=alt.X('Name:N', title='Time'),
    y=alt.Y('Home_Percentage:Q', axis=alt.Axis(format='%')),
    color=alt.Color('Name:N', scale=alt.Scale(scheme='category20')),
    tooltip=['Name', 'Home_Percentage', 'Home_Count']
).properties(width=600, height=400)

st.altair_chart(bar_chart_home, use_container_width=True)
st.altair_chart(bar_chart_home_count, use_container_width=True)

# Gráfico de barras para percentual de jardas fora e contagem fora
st.subheader("Percentual de Jardas e Contagem Fora por Time")
bar_chart_away = alt.Chart(filtered_df).mark_bar(opacity=0.7).encode(
    x=alt.X('Name:N', title='Time'),
    y=alt.Y('Away_Yards_Percentage:Q', axis=alt.Axis(format='%')),
    color=alt.Color('Name:N', scale=alt.Scale(scheme='category20')),
    tooltip=['Name', 'Away_Yards_Percentage', 'Away_Percentage']
).properties(width=600, height=400)

bar_chart_away_count = alt.Chart(filtered_df).mark_bar(opacity=0.7).encode(
    x=alt.X('Name:N', title='Time'),
    y=alt.Y('Away_Percentage:Q', axis=alt.Axis(format='%')),
    color=alt.Color('Name:N', scale=alt.Scale(scheme='category20')),
    tooltip=['Name', 'Away_Percentage', 'Away_Count']
).properties(width=600, height=400)

st.altair_chart(bar_chart_away, use_container_width=True)
st.altair_chart(bar_chart_away_count, use_container_width=True)