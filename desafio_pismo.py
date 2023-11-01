import requests
import json
import sqlite3
from datetime import datetime, timedelta

api_key = 'abc232d21be4415d83620c03a8b0b05a'
base_url = "https://openexchangerates.org/api/historical/"

# Data de início e fim desejadas
data_inicio = datetime(2022, 7, 21)
data_fim = datetime(2022, 8, 31)

# Símbolos que você deseja obter
moedas = ["BRL", "EUR", "CLP"]

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect("desafio_pismo.db")
cursor = conexao.cursor()

# Crie a tabela "cambio_moedas" se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS cambio_moedas (
                    data TEXT,
                    valor REAL,
                    moeda TEXT
                )''')

while data_inicio <= data_fim:
    # Formate a data no formato necessário (YYYY-MM-DD)
    data_formatada = data_inicio.strftime('%Y-%m-%d')
    
    url = f"{base_url}{data_formatada}.json?app_id={api_key}&base=USD&symbols={','.join(moedas)}&show_alternative=false&prettyprint=false"
    
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        dados = json.loads(response.text)
        
        for moeda in moedas:
            valor = dados['rates'][moeda]
            cursor.execute("INSERT INTO cambio_moedas (data, valor, moeda) VALUES (?, ?, ?)",
                           (data_formatada, valor, moeda))
    else:
        print(f"Erro ao buscar dados para a data: {data_formatada}")

    # Avance para o próximo dia
    data_inicio += timedelta(days=1)

# Salve as alterações no banco de dados e feche a conexão
conexao.commit()
conexao.close()

print(f"Banco de dados 'desafio_pismo' e tabela 'cambio_moedas' criados e resultados inseridos.")
