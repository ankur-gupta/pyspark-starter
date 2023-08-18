import os
from pyspark.sql import SparkSession

JAVA_HOME = '/opt/homebrew/opt/openjdk@17'
os.environ['JAVA_HOME'] = JAVA_HOME

spark = SparkSession.builder.appName('PySparkShell').getOrCreate()

# Turn on case sensitivity
# https://stackoverflow.com/questions/42946104/enable-case-sensitivity-for-spark-sql-globally
spark.conf.set('spark.sql.caseSensitive', True)

# 1. We need 's3a://'; 's3://' will not work.
# 2. We need to add the glab pattern '*.parquet' at the end.
spark.read.parquet('s3a://aws-roda-hcls-datalake/gnomad/chrm/*.parquet')
