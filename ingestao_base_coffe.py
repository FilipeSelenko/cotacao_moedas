import sqlite3
import pandas as pd

# Conectando ao banco de dados SQLite que criamos
conexao = sqlite3.connect("desafio_pismo.db")
cursor = conexao.cursor()

nome_arquivo_csv = "coffee.csv"

# Consultando a base coffee.csv pelo pandas
df = pd.read_csv(nome_arquivo_csv)

# Padronizando o nome das colunas
df.rename(columns={"Date": "date", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume", "Currency": "currency"}, inplace=True)

# Criando um dicionário para fazer o cast dos datatypes
dtype = {
    'date': 'date',
    'open': 'float',
    'high': 'float',
    'low': 'float',
    'close': 'float',
    'volume': 'integer',
    'currency': 'text'
}

# Carregando os dados do DataFrame para a tabela no banco de dados
df.to_sql("coffee", conexao, if_exists="replace", index=False)

# Fechando a conexão
conexao.close()
