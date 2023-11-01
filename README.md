**Script de Coleta de Dados Cambiais**

Este repositório fornece informações e orientações sobre o script Python que coleta dados cambiais a partir da API do Open Exchange Rates e armazena esses dados em um banco de dados SQLite. O script utiliza a biblioteca requests para fazer solicitações à API, processa os dados retornados em formato JSON com a biblioteca json, e utiliza o SQLite para criação do banco de dados, tabela e ingestão dos dados.

**Bibliotecas Python:**

**requests:** Utilizado para fazer solicitações HTTP à API.

**json:** Utilizado para processar os dados retornados em formato JSON.

**sqlite3:** Utilizado para interagir com o banco de dados SQLite.

```pip install requests json sqlite3```

**Campos**

**api_key:** Substitua pela sua chave de API do Open Exchange Rates. Você pode obter uma chave em (https://openexchangerates.org/).

**data_inicio** e **data_fim**: O período utilizado na extração foi de 21 de julho de 2022 a 31 de agosto de 2022. Você pode ajustar essas datas conforme necessário.

**moedas:** As moedas extraídas foram BRL(Real), EUR(Euro) e CLP(Peso Chileno). Você pode adicionar ou remover moedas conforme necessário.

**conexao:** Foi criado um banco de dados "desafio_pismo.db" para a ingestão dos dados extraídos da API.
