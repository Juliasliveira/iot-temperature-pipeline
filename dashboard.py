# Dashboard de Temperaturas IoT
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://postgres:senha123@localhost:5433/postgres')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('🌡️ Dashboard de Temperaturas IoT')
st.markdown('Pipeline de dados com leituras de sensores de temperatura.')

# Gráfico 1: Média de temperatura por data
st.header('Média de Temperatura por Data')
df_avg = load_data('avg_temp_por_dispositivo')
fig1 = px.line(df_avg, x='noted_date', y='avg_temp',
               title='Evolução da temperatura média ao longo do tempo')
st.plotly_chart(fig1)

# Gráfico 2: Leituras por hora do dia
st.header('Leituras por Hora do Dia')
df_hora = load_data('leituras_por_hora')
fig2 = px.bar(df_hora, x='hora', y='contagem',
              title='Quantidade de leituras por hora')
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_maxmin = load_data('temp_max_min_por_dia')
fig3 = px.line(df_maxmin, x='data', y=['temp_max', 'temp_min'],
               title='Variação de temperatura máxima e mínima diária')
st.plotly_chart(fig3) 