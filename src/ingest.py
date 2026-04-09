# Script de ingestão de dados IoT para PostgreSQL
import pandas as pd
from sqlalchemy import create_engine, text

# Conexão com o banco (porta 5433)
engine = create_engine('postgresql://postgres:senha123@localhost:5433/postgres')

# Leitura do CSV
print("Lendo o arquivo CSV...")
df = pd.read_csv('data/IOT-temp.csv')

# Exibe as primeiras linhas para conferir
print(df.head())
print(f"Total de registros: {len(df)}")

# Renomeia colunas para facilitar
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Insere no banco de dados
print("Inserindo dados no PostgreSQL...")
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
print("Dados inseridos com sucesso!")