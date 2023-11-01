## Sobre este serviço
* Este serviço coleta dados cambiais convertidos em **USD (Dólar)** das moedas **BRL (Real), EUR (Euro) e CLP (Pesos Chilenos)** a partir da **API do Open Exchange Rates** e armazena esses dados em um banco de dados SQLite.
* O script utiliza a biblioteca requests para fazer solicitações à API, processa os dados retornados em formato JSON com a biblioteca json, e utiliza o SQLite para criação do banco de dados, tabela e ingestão dos dados.
* Para fins de estudo e comparação, no repositório temos também o um script para carregamento de dados de arquivo CSV para um banco de dados SQLite. No estudo foi utilizado o arquivo (coffee.csv).
* O script utiliza a biblioteca sqlite3 para criar uma conexão com o banco de dados e a biblioteca pandas para ler e transformar o arquivo CSV em um DataFrame antes de carregá-lo no banco de dados.

## Pré requisitos do serviço

### Python

Este serviço utiliza o Python 3.8. Para baixar e instalar: [link](https://www.python.org/downloads/).

**API Key:** [link](https://openexchangerates.org)

**Base em CSV para fins de comparação:** No caso atual, foi utilizado uma base fornecida contendo histórico da cotação do valor do café em dólar.

## Extração da cotação das moedas, e criação do banco de dados e tabela

### Este projeto utiliza as seguintes bibliotecas:

* **requests:** Utilizado para fazer solicitações HTTP à API.

* **json:** Utilizado para processar os dados retornados em formato JSON.

* **sqlite3:** Utilizado para interagir com o banco de dados SQLite.

```pip install requests json sqlite3```

## Executando o Script

Após configurar as variáveis, você pode executar o script para coletar os dados cambiais. Para executar o script, basta abrir um terminal, navegar até o diretório onde o script está localizado e executar o seguinte comando:

```python extracao_cotacao.py```

### Campos

* **api_key:** Substitua pela sua chave de API do Open Exchange Rates. Você pode obter uma chave em (https://openexchangerates.org/).

* **data_inicio** e **data_fim**: O período utilizado na extração foi de 21 de julho de 2022 a 31 de agosto de 2022. Você pode ajustar essas datas conforme necessário.

* **moedas:** As moedas extraídas foram BRL(Real), EUR(Euro) e CLP(Peso Chileno), e sempre em comparação ao dólar (USD). Você pode adicionar ou remover moedas conforme necessário.

* **conexao:** Foi criado um banco de dados ```desafio_pismo.db``` e uma tabela ```cambio_moedas``` para a ingestão dos dados extraídos da API.

Ao final da execução, você terá os dados dos períodos selecionados e moedas inseridos no banco de dados ```desafio_pismo.db``` na tabela ```cambio_moedas```.


## Ingestão do arquivo CSV

O script ```ingestao_base_coffe.py``` será responsável por ler o arquivo CSV, transformar os dados em um DataFrame do pandas e carregar esses dados na tabela do banco de dados SQLite especificada. 

Ao final da execução, você terá os dados do arquivo CSV armazenados no banco de dados ```desafio_pismo.db``` na tabela ```coffee```.

### Este projeto utiliza as seguintes bibliotecas:

* **sqlite3:** Utilizado para criar e gerenciar uma conexão com o banco de dados SQLite.

* **pandas:** Utilizado para ler e manipular os dados do arquivo CSV.

Você pode instalar essas bibliotecas usando o gerenciador de pacotes **pip**, se ainda não estiverem instaladas:

```pip install sqlite3 pandas```

## Executando o Script

Após configurar as variáveis, você pode executar o script para carregar os dados do arquivo CSV no banco de dados. Para executar o script, basta abrir um terminal, navegar até o diretório onde o script está localizado e executar o seguinte comando:

```python ingestao_base_coffe.py```


### Campos

* **conexao:** O script se conecta a um banco de dados SQLite chamado "desafio_pismo.db".

* **nome_arquivo_csv:** Defina o nome do arquivo CSV que deseja carregar para o banco de dados. No exemplo, o nome do arquivo é "coffee.csv". 

* **df.rename():** Se o arquivo CSV tiver colunas com nomes diferentes dos que são desejados na tabela do banco de dados, você pode usar o método df.rename() para renomear as colunas. 

* **dtype:** Este dicionário especifica os tipos de dados (datatypes) que serão usados para as colunas no banco de dados. 

## Dashboard criado com os resultados no [Looker](https://lookerstudio.google.com/reporting/5eae0f7a-395f-4e67-b118-4666b9d06d7a):

<img width="902" alt="image" src="https://github.com/FilipeSelenko/cotacao_moedas/assets/66075126/6070c9e3-b86a-43f5-a4a6-31af105065de">

### Dados do dashboard: 
* Última cotação das moedas EUR, BRL e CLP

* Histórico dos últimos 30 dias das moedas
