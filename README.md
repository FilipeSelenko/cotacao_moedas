**Script de Coleta de Dados Cambiais**

Este README fornece informações e orientações sobre o script Python que coleta dados cambiais a partir da API do Open Exchange Rates e armazena esses dados em um banco de dados SQLite. O script utiliza a biblioteca requests para fazer solicitações à API, processa os dados retornados em formato JSON com a biblioteca json, e utiliza o SQLite para armazenamento dos dados.

**Pré-requisitos**
Antes de executar o script, certifique-se de ter os seguintes pré-requisitos em seu ambiente de desenvolvimento:

Python: Certifique-se de que você possui o Python instalado em seu sistema. Você pode fazer o download em python.org.

**Bibliotecas Python:**

**requests:** Utilizado para fazer solicitações HTTP à API.
**json:** Utilizado para processar os dados retornados em formato JSON.
**sqlite3:** Utilizado para interagir com o banco de dados SQLite.
Você pode instalar essas bibliotecas usando o gerenciador de pacotes **pip**, se ainda não estiverem instaladas:

```pip install requests json sqlite3```

**Configuração**
Antes de executar o script, é necessário configurar algumas variáveis:

api_key: Substitua pela sua chave de API do Open Exchange Rates. Você pode obter uma chave em _openexchangerates.org._

data_inicio e data_fim: Defina as datas de início e fim desejadas para a coleta de dados cambiais. No exemplo, o período está definido de 21 de julho de 2022 a 31 de agosto de 2022. Você pode ajustar essas datas conforme necessário.

moedas: Defina a lista de moedas que deseja obter. No exemplo, estão incluídas as moedas "BRL", "EUR" e "CLP". Você pode adicionar ou remover moedas conforme necessário.

conexao: Especifique o nome do banco de dados SQLite onde os dados serão armazenados. O exemplo utiliza "desafio_pismo.db", mas você pode alterar o nome do arquivo.

**Executando o Script**
Após configurar as variáveis, você pode executar o script para coletar os dados cambiais. Para executar o script, basta abrir um terminal, navegar até o diretório onde o script está localizado e executar o seguinte comando:

```python nome_do_script.py```

Substitua ```nome_do_script.py``` pelo nome do arquivo onde o código está armazenado.

**Resultados**

O script irá coletar os dados cambiais para o período especificado, inseri-los no banco de dados SQLite e informar quando a operação estiver concluída. Os resultados serão armazenados na tabela "cambio_moedas" dentro do banco de dados.

Ao final da execução, você poderá acessar o banco de dados "desafio_pismo.db" e consultar a tabela "cambio_moedas" para obter os dados cambiais coletados.

Este **README** fornece uma visão geral do funcionamento do script e como configurá-lo. Certifique-se de que todas as dependências estão instaladas e as variáveis estejam configuradas corretamente antes de executar o script.




**README - Script de Carregamento de Dados de Arquivo CSV para Banco de Dados SQLite**
Este **README** fornece informações e orientações sobre o script Python que carrega dados de um arquivo CSV para um banco de dados SQLite. O script utiliza a biblioteca sqlite3 para criar uma conexão com o banco de dados e a biblioteca pandas para ler e transformar o arquivo CSV em um DataFrame antes de carregá-lo no banco de dados.

**Pré-requisitos**
Antes de executar o script, certifique-se de ter os seguintes pré-requisitos em seu ambiente de desenvolvimento:

**Python:** Certifique-se de que você possui o Python instalado em seu sistema. Você pode fazer o download em python.org.

**Bibliotecas Python:**

sqlite3: Utilizado para criar e gerenciar uma conexão com o banco de dados SQLite.
pandas: Utilizado para ler e manipular os dados do arquivo CSV.
Você pode instalar essas bibliotecas usando o gerenciador de pacotes pip, se ainda não estiverem instaladas:

```pip install sqlite3 pandas```

**Configuração**
Antes de executar o script, é necessário configurar algumas variáveis:

conexao: O script se conecta a um banco de dados SQLite chamado "desafio_pismo.db". Certifique-se de que o arquivo do banco de dados esteja no mesmo diretório em que o script será executado. Você pode alterar o nome do arquivo do banco de dados se necessário.

nome_arquivo_csv: Defina o nome do arquivo CSV que deseja carregar para o banco de dados. No exemplo, o nome do arquivo é "coffee.csv". Certifique-se de que o arquivo esteja no mesmo diretório em que o script será executado. Você pode alterar o nome do arquivo CSV conforme necessário.

df.rename(): Se o arquivo CSV tiver colunas com nomes diferentes dos que são desejados na tabela do banco de dados, você pode usar o método df.rename() para renomear as colunas. Certifique-se de que os nomes das colunas no script correspondam aos nomes reais no arquivo CSV.

dtype: Este dicionário especifica os tipos de dados (datatypes) que serão usados para as colunas no banco de dados. Certifique-se de que os tipos de dados estejam corretos de acordo com o conteúdo das colunas.

**Executando o Script**
Após configurar as variáveis, você pode executar o script para carregar os dados do arquivo CSV no banco de dados. Para executar o script, basta abrir um terminal, navegar até o diretório onde o script está localizado e executar o seguinte comando:

```python nome_do_script.py```

Substitua nome_do_script.py pelo nome do arquivo onde o código está armazenado.

**Resultados**
O script lerá o arquivo CSV, transformará os dados em um DataFrame do pandas e carregará esses dados na tabela do banco de dados SQLite especificada. Se a tabela já existir no banco de dados, os dados existentes serão substituídos (devido ao parâmetro if_exists="replace").

Ao final da execução, você terá os dados do arquivo CSV armazenados no banco de dados "desafio_pismo.db" na tabela "coffee".

Este README fornece uma visão geral do funcionamento do script e como configurá-lo. Certifique-se de que todas as dependências estão instaladas e as variáveis estejam configuradas corretamente antes de executar o script.
