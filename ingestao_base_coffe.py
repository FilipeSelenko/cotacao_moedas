import sqlite3
import pandas as pd

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect("desafio_pismo.db")
cursor = conexao.cursor()

# Nome do arquivo CSV a ser carregado
nome_arquivo_csv = "coffee.csv"

# Ler o CSV usando pandas
df = pd.read_csv(nome_arquivo_csv)

# Renomear as colunas conforme necessário
df.rename(columns={"Date": "date", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume", "Currency": "currency"}, inplace=True)

# Criando um dicionário contendo os datatypes necessários das colunas
dtype = {
    'date': 'date',
    'open': 'float',
    'high': 'float',
    'low': 'float',
    'close': 'float',
    'volume': 'integer',
    'currency': 'text'
}

# Carregar os dados do DataFrame para a tabela no banco de dados
df.to_sql("coffee", conexao, if_exists="replace", index=False)

# Fechar a conexão
conexao.close()
