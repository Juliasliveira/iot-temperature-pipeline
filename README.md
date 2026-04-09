# 🌡️ IoT Temperature Pipeline

Pipeline de dados para processamento e visualização de leituras de temperatura de dispositivos IoT, utilizando Python, Docker, PostgreSQL e Streamlit.

## 📌 Descrição do Projeto

Este projeto coleta dados reais de sensores de temperatura IoT, armazena em um banco de dados PostgreSQL rodando em Docker, e exibe visualizações interativas em um dashboard Streamlit.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13** — processamento e ingestão dos dados
- **Docker** — containerização do banco de dados
- **PostgreSQL** — armazenamento dos dados
- **SQLAlchemy** — conexão Python com o banco
- **Pandas** — leitura e manipulação do CSV
- **Streamlit** — dashboard interativo
- **Plotly** — gráficos interativos

## 📁 Estrutura do Projeto

iot-temperature-pipeline/
├── src/
│   └── ingest.py        # Script de ingestão dos dados
├── data/
│   └── IOT-temp.csv     # Dataset de leituras IoT
├── docs/
│   └── dashboard.png    # Print do dashboard
├── sql/
│   └── views.sql        # Views SQL criadas no PostgreSQL
├── dashboard.py         # Dashboard Streamlit
└── README.md


## ⚙️ Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/iot-temperature-pipeline.git
cd iot-temperature-pipeline
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências
```bash
pip install pandas psycopg2-binary sqlalchemy streamlit plotly
```

### 4. Suba o container PostgreSQL
```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=senha123 -p 5433:5432 -d postgres
```

### 5. Execute o script de ingestão
```bash
python src/ingest.py
```

### 6. Execute o dashboard
```bash
streamlit run dashboard.py
```

Acesse em: http://localhost:8501

## 🗄️ Views SQL

### View 1 — `avg_temp_por_dispositivo`
Calcula a média de temperatura agrupada por data/hora. Permite visualizar a evolução da temperatura ao longo do tempo.

### View 2 — `leituras_por_hora`
Conta o número de leituras agrupadas por hora do dia. Identifica os horários de maior atividade dos sensores.

### View 3 — `temp_max_min_por_dia`
Retorna a temperatura máxima e mínima registrada por dia. Permite analisar a amplitude térmica diária.

## 📊 Dashboard

O dashboard possui 3 gráficos interativos:
- **Média de temperatura por data** — evolução temporal
- **Leituras por hora do dia** — distribuição horária
- **Temperaturas máximas e mínimas por dia** — amplitude térmica

## 💡 Insights

- O pico de leituras ocorre entre 13h e 15h, horário de maior atividade dos dispositivos
- A temperatura média se mantém entre 25°C e 50°C ao longo do período
- Há variação significativa entre temperatura máxima e mínima diária, indicando ambientes com grande oscilação térmica
- Os dados cobrem o período de julho a dezembro de 2018

## 🔧 Comandos Git Utilizados

```bash
git init
git add .
git commit -m "Projeto inicial: Pipeline de Dados IoT"
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```

## 📦 Dataset

Dataset utilizado: [Temperature Readings: IoT Devices](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices)