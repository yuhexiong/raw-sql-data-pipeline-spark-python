# Raw SQL Data Pipeline Spark


A Spark-based data pipeline transfers data from MySQL to MySQL, using raw SQL syntax for data extraction, transformation, and loading.




## Overview

- Language: Python
- Data Processing Framework: Spark v3.5.1


## Yaml

edit connection infomation and sql query in [mysql_raw_query.yaml](./mysql_raw_query.yaml)  

```yaml
source:
  host: "localhost"
  port: 9030
  database: "database"
  user: "user"
  password: "password"
query: "SELECT * FROM Table1 LEFT JOIN Table2 ON Table1.table2_id = Table2.id"
sink:
  host: "localhost"
  port: 9030
  database: "database"
  user: "user"
  password: "password"
  table: "Table3"
```


## Run

### Run Docker Container

```
docker compose up -d
```

