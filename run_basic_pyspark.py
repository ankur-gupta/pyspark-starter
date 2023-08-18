import os
from pyspark.sql import SparkSession

JAVA_HOME = '/opt/homebrew/opt/openjdk@17'
os.environ['JAVA_HOME'] = JAVA_HOME

spark = SparkSession.builder.appName('PySparkShell').getOrCreate()

# Turn on case sensitivity
# https://stackoverflow.com/questions/42946104/enable-case-sensitivity-for-spark-sql-globally
spark.conf.set('spark.sql.caseSensitive', True)

df = spark.createDataFrame([(x, str(x)) for x in range(5)], 'x INT, y STRING')
df.show()
