from pyspark.sql import SparkSession
import argparse
import yaml

# args
parser = argparse.ArgumentParser(description='process some yaml file.')
parser.add_argument('-f', '--file', type=str, required=True, help='yaml configuration file name')
args = parser.parse_args()

# setting yaml
with open(args.file, "r") as file:
    config = yaml.safe_load(file)

spark = SparkSession.builder \
    .appName("mysql_raw_query") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

source = config['source']
df = spark \
        .read \
        .format("jdbc") \
        .options(
            url=f"jdbc:mysql://{source['host']}:{source['port']}/{source['database']}",
            dbtable=f"({config['query']}) as temp",
            user=source['user'],
            password=source['password'],
            driver="com.mysql.cj.jdbc.Driver"
        ).load()

df.show()

sink = config['sink']
ds = df \
    .write \
    .mode("append") \
    .format("jdbc") \
    .option("url", f"jdbc:mysql://{sink['host']}:{sink['port']}/{sink['database']}") \
    .option("dbtable", sink['table']) \
    .option("user", sink['user']) \
    .option("password", sink['password']) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .save()