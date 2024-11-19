from pyspark.sql.connect.session import SparkSession

class SparkConnector:

    spark_session = None

    def __init__(self):
        self.spark_session = SparkSession.builder.remote("sc://spark_cluster:15002").getOrCreate()


    def __del__(self):
        self.spark_session.stop()