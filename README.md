## About this service
* This service collects exchange rate data, converted to USD (Dollar), for the currencies BRL (Real), EUR (Euro), and CLP (Chilean Peso) from the Open Exchange Rates API and stores it in a SQLite database.
* The script uses the requests library to make requests to the API, processes the JSON-formatted data with the json library, and uses SQLite to create the database, table, and ingest the data.
* For study and comparison purposes, a script is also provided in the repository for loading CSV data into a SQLite database. The file (coffee.csv) was used in this study.
* The script uses the sqlite3 library to establish a connection to the database and the pandas library to read and transform the CSV file into a DataFrame before loading it into the database.

## Service Prerequisites

### Python

This service requires Python 3.8. Download and install it here: [link](https://www.python.org/downloads/).

**API Key:** [link](https://openexchangerates.org)

**CSV-based Dataset for Comparison:** In this case, a provided dataset containing historical coffee price data in USD was used.

## Currency Rate Extraction, Database, and Table Creation

### This project uses the following libraries:

* **requests:** Used for making HTTP requests to the API.

* **json:** Used to process JSON-formatted data returned from the API.

* **sqlite3:** Used for interacting with the SQLite database.

```pip install requests json sqlite3```

## Running the Script

After configuring the variables, you can run the script to collect exchange rate data. To execute the script, open a terminal, navigate to the directory where the script is located, and run the following command:

```python extracao_cotacao.py```

### Fields

* **api_key:** Replace with your Open Exchange Rates API key, which you can obtain here (https://openexchangerates.org/).

* **data_inicio** e **data_fim**: The extraction period used was from July 21, 2022, to August 31, 2022. You can adjust these dates as needed.

* **moedas:** The extracted currencies were BRL (Real), EUR (Euro), and CLP (Chilean Peso), always in comparison to USD. You can add or remove currencies as needed.

* **conexao:** A database named ```desafio_pismo.db``` and a table named ```cambio_moedas``` were created to store the data extracted from the API.

Upon completion, the data for the selected periods and currencies will be stored in the ```desafio_pismo.db``` database in the ```cambio_moedas```.


## CSV File Ingestion

The script ```ingestao_base_coffe.py``` reads the CSV file, transforms the data into a pandas DataFrame, and loads it into the specified SQLite database table. 

### This project uses the following libraries:

* **sqlite3:** Used to create and manage a connection to the SQLite database.

* **pandas:** Used to read and manipulate data from the CSV file.

You can install these libraries using the pip package manager if they are not already installed:

```pip install sqlite3 pandas```

## Running the Script

After configuring the variables, you can run the script to load the CSV data into the database. To execute the script, open a terminal, navigate to the directory where the script is located, and run the following command:

```python ingestao_base_coffe.py```


### Fields

* **conexao:** The script connects to a SQLite database named "desafio_pismo.db."

* **nome_arquivo_csv:** Specify the name of the CSV file you want to load into the database. In the example, the file name is "coffee.csv."

* **df.rename():** f the CSV file has column names different from those desired in the database table, you can use the df.rename() method to rename the columns.

* **dtype:** This dictionary specifies the data types to be used for the columns in the database.

Upon completion, the data from the CSV file will be stored in the desafio_pismo.db database in the coffee table.

## Dashboard Created with the Results in [Looker](https://lookerstudio.google.com/reporting/5eae0f7a-395f-4e67-b118-4666b9d06d7a):

<img width="902" alt="image" src="https://github.com/FilipeSelenko/cotacao_moedas/assets/66075126/6070c9e3-b86a-43f5-a4a6-31af105065de">

### Dashboard Data:
* Latest exchange rate for EUR, BRL, and CLP

* Last 30-day historical exchange rate data for these currencies
