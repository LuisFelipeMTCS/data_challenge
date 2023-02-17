<h1 align="center"> Desafio Engenheiro de Dados <h1/>
  
  ## :memo: Descrição
  Este projeto foi um desafio para empresa Indicium,  tem como objetivo criar uma base de dados northwind, exportar seus dados para o disco local como arquivo CSV, realizar o processo de ETL(exportar, transformar e carregar) para outra base de dados. Após isso, realizar a importação de uma consulta escolhida pela empresa atráves do datawarehouse (Base de dados com seus dados já tratados).
  
  
  
## :books: Funcionalidades
* <b>Arquivo main.py</b>: Inicialização do projeto com schedule excutando o projeto duas vezes ao dia.
* <b>Arquivo file_get_csv.py</b>: Exportação de 13 arquivos no formato csv da base de dados Postgres para o disco local "data/postgres/{nome-tabela}/{dia-atual}".
* <b>Arquivo file_send_csv.py</b>: Envio de 14 arquivos Csv para o Datawarehouse Mysql, juntamente com uma tabela separada "order_details.csv" no diretório "data/csv/{data-atual}" que tem o intuito de realizar uma relação de muitos para muitos no banco de dados northwind.
* <b>Arquivo file_export_mysql.py</b>: Exportar consulta do banco de dados mysql que informa seus pedidos e detalhes para um arquivo csv "Orders_order_details" no seguinte diretório "data/select_import/{data-atual}
* <b>Arquivo file_check_folder.py</b>: Arquivo que verifica se existe um diretório ou não, e envia seu caminho como parâmetro.
* <b>Diretório db</b>: Realizo conexões e seleciono Querys com o banco de dados postgres e mysql, isso ocorre em diretórios distintos dentro do principal "db".
* <b>Diretório data</b>: Onde ocorre a importação e exportação de arquivos csv. 
  
## :wrench: Tecnologias utilizadas
 <img align="center" alt="" height="30" width="40" src="https://icongr.am/devicon/mysql-original.svg?size=148&color=a44141"><img align="center" alt="" height="30" width="40" src="https://icongr.am/devicon/postgresql-original.svg?size=148&color=262626"><img align="center" alt="Rafa-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">




  


