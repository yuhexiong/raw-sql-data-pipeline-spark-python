# Raw SQL Data Pipeline Spark

基於 Spark 的數據管道，使用原始 SQL 語法進行數據提取、轉換和加載，將數據從 MySQL 傳輸到 MySQL。

## Overview

- 語言：Python
- 數據處理框架：Spark v3.5.1

## Yaml

編輯 [mysql_raw_query.yaml](./mysql_raw_query.yaml) 中的連接資訊和 SQL 查詢

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
