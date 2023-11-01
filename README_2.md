**Script de Carregamento de Dados de Arquivo CSV para Banco de Dados SQLite**
Este repositório fornece informações sobre o script Python que carrega dados de um arquivo CSV para um banco de dados SQLite. O script utiliza a biblioteca sqlite3 para criar uma conexão com o banco de dados e a biblioteca pandas para ler e transformar o arquivo CSV em um DataFrame antes de carregá-lo no banco de dados.

O script lerá o arquivo CSV, transformará os dados em um DataFrame do pandas e carregará esses dados na tabela do banco de dados SQLite especificada.

Ao final da execução, você terá os dados do arquivo CSV armazenados no banco de dados.

**Bibliotecas Python:**

sqlite3: Utilizado para criar e gerenciar uma conexão com o banco de dados SQLite.

pandas: Utilizado para ler e manipular os dados do arquivo CSV.

Você pode instalar essas bibliotecas usando o gerenciador de pacotes pip, se ainda não estiverem instaladas:

```pip install sqlite3 pandas```

**Configuração**

conexao: O script se conecta a um banco de dados SQLite chamado "desafio_pismo.db".

nome_arquivo_csv: Defina o nome do arquivo CSV que deseja carregar para o banco de dados. No exemplo, o nome do arquivo é "coffee.csv". 

df.rename(): Se o arquivo CSV tiver colunas com nomes diferentes dos que são desejados na tabela do banco de dados, você pode usar o método df.rename() para renomear as colunas. 

dtype: Este dicionário especifica os tipos de dados (datatypes) que serão usados para as colunas no banco de dados. 
