<h1 align="center"> Desafio Engenheiro de Dados <h1/>
  
  ## :memo: Descrição
  Este projeto foi um desafio para empresa Indicium,  tem como objetivo criar uma base de dados northwind, exportar seus dados para o disco local como arquivo CSV, realizar o processo de ETL(exportar, transformar e carregar) para outra base de dados. Após isso, realizar a importação de uma consulta escolhida pela empresa atráves do datawarehouse (Base de dados com seus dados já tratados).
  
  
  
## :books: Funcionalidades
* <b>Arquivo main.py</b>: Inicialização do projeto com schedule excutando o projeto duas vezes ao dia.
* <b>Arquivo file_get_csv.py</b>: Exportação de 13 arquivos no formato csv da base de dados Postgres para o disco local "data/postgres/{nome-tabela}/{dia-atual}".
* <b>Arquivo file_send_csv.py</b>: Envio de 14 arquivos Csv para o Datawarehouse Mysql, juntamente com uma tabela separada "order_details.csv" no diretório "data/csv/{data-atual}" que tem o intuito de realizar uma relação de muitos para muitos no banco de dados northwind.



