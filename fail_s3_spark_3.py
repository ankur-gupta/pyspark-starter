import os
from pyspark.sql import SparkSession

JAVA_HOME = '/opt/homebrew/opt/openjdk@17'
os.environ['JAVA_HOME'] = JAVA_HOME
SPARK_PACKAGES = [
    # From
    # https://central.sonatype.com/artifact/org.apache.spark/spark-core_2.12/3.4.1/dependencies
    # https://central.sonatype.com/artifact/org.apache.hadoop/hadoop-aws/3.3.4
    'org.apache.hadoop:hadoop-aws:3.3.4'  # For S3
]
os.environ['PYSPARK_SUBMIT_ARGS'] = f'--packages {",".join(SPARK_PACKAGES)} pyspark-shell'
os.environ['AWS_ACCESS_KEY'] = '<access-key>'
os.environ['AWS_SECRET_KEY'] = '<secret-key>'
spark = SparkSession.builder.appName('PySparkShell').getOrCreate()

# Turn on case sensitivity
# https://stackoverflow.com/questions/42946104/enable-case-sensitivity-for-spark-sql-globally
spark.conf.set('spark.sql.caseSensitive', True)

# 1. We need 's3a://'; 's3://' will not work.
# 2. We need to add the glab pattern '*.parquet' at the end.
spark.read.parquet('s3a://aws-roda-hcls-datalake/gnomad/chrm/*.parquet')
