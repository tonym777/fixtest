"""
Created on Thu Aug 20 22:59:04 2020

SparkETL:
 use Spark connector to
    perform Extract (from csv file),
    Transform (remap columns)
    Load data into SQL

@author: Tony
"""

from src.stat.spark_connector import SparkConnector

class SparkETL:

    def __init__(self):
        self.spark = SparkConnector.spark_session
        self.df = None

    def load_csv(self):
        self.df = self.spark.read.csv("data_file.csv", header=True, inferSchema=True)

    def transform(self, age):
        self.df.filter(self.df["Age"] < 18)

    def save_to_db(self):
        self.df.write.format("jdbc") \
            .option("url", "jdbc:mysql://sql_cluster:3306/database_name") \
            .option("dbtable", "data_table") \
            .option("user", "username") \
            .option("password", "password") \
            .mode("overwrite") \
            .save()