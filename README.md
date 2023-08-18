# PySpark Starter

<!-- TOC -->
* [PySpark Starter](#pyspark-starter)
  * [Get the Maven coordinates for Spark](#get-the-maven-coordinates-for-spark)
  * [Find Java & Python versions](#find-java--python-versions)
  * [Install Java](#install-java)
    * [MacOS (Apple Silicon)](#macos-apple-silicon)
      * [Note `JAVA_HOME`](#note-javahome)
  * [Install Python](#install-python)
    * [MacOS (Apple Silicon)](#macos-apple-silicon-1)
  * [Scala does not need to be explicitly installed](#scala-does-not-need-to-be-explicitly-installed)
  * [Install `pyspark`](#install-pyspark)
    * [Create a virtual environment](#create-a-virtual-environment)
    * [Install `pyspark` and other dependencies](#install-pyspark-and-other-dependencies)
  * [Test out basic pyspark run](#test-out-basic-pyspark-run)
<!-- TOC -->

Running PySpark requires is difficult because it requires three components:
1. Java 
2. Scala
3. Python

You need have the correct versions of each of these languages and the 
correct versions of dependencies for packages in all of these languages. 

This repository aims to provide
1. a combination of all versions that is known to work at of Aug 17, 2023 
2. starter code that you can easily run and check to see if your spark installation works

This repository supports MacOS (Apple Silicon) and Linux (Ubuntu) but may work on other 
operating system and architectures. 

## Get the Maven coordinates for Spark
Start at the Apache Spark [download](https://spark.apache.org/downloads.html) page. Note the 
version of Spark and maven coordinates of Spark. As of Aug 17, 2023, these were the 
[Maven](https://search.maven.org/search?q=g:org.apache.spark) coordinates:
```
groupId: org.apache.spark
artifactId: spark-core_2.12  
version: 3.4.1
```
The `version` refers to both spark (jar) and pyspark (wheel) versions, which are typically the same. 
For example, PySpark 3.4.1 corresponds to Spark 3.4.1. 
The suffix `2.12` in `artifactId` is the Scala version. 

You may be more familiar with Maven coordinates in `pom.xml` format:
```xml
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-core_2.12</artifactId>
    <version>3.4.1</version>
</dependency>
```

Using the Maven coordinates, find the link to the [Maven Central Repository](https://central.sonatype.com/artifact/org.apache.spark/spark-core_2.12/3.4.1) 
page. You'll need to find versions of dependencies from this page later on.

## Find Java & Python versions
The previous step tells you about the Scala version, but it didn't tell you the which version of Java or Python you 
need. Knowing these versions before installing anything is extremely important. 

We can find these versions on the relevant Spark documentation page, such as 
this page for [Spark 3.4.1](https://spark.apache.org/docs/3.4.1/). Find a paragraph that looks like this:

```
Spark runs on Java 8/11/17, Scala 2.12/2.13, Python 3.7+, and R 3.5+. Python 3.7 
support is deprecated as of Spark 3.4.0. Java 8 prior to version 8u362 support 
is deprecated as of Spark 3.4.0. When using the Scala API, it is necessary for 
applications to use the same version of Scala that Spark was compiled for. 
For example, when using Scala 2.13, use Spark compiled for 2.13, and compile 
code/applications for Scala 2.13 as well.
```

This narrows down the versions of Python and Java that are supported but does not provide 
one single answer. The Scala version in the Maven coordinates is supported.

Let's choose Java 17 and Python 3.11.

| Software | Version |
|----------|---------|
| Scala    | 2.12    |
| Java     | 17      |
| Python   | 3.11    |
| spark    | 3.4.1   |
| pypark   | 3.4.1   |

## Install Java
### MacOS (Apple Silicon)
Install Java using [brew](https://brew.sh/).
```shell
brew info openjdk@17
# ==> openjdk@17: stable 17.0.8 (bottled) [keg-only]
# Development kit for the Java programming language
# https://openjdk.java.net/
# Not installed
# From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/o/openjdk@17.rb
# License: GPL-2.0-only with Classpath-exception-2.0
# ==> Dependencies
# Build: autoconf ✘, pkg-config ✘
# Required: giflib ✔, harfbuzz ✔, jpeg-turbo ✔, libpng ✔, little-cms2 ✔
# ==> Requirements
# Build: Xcode (on macOS) ✔
# ==> Caveats
# For the system Java wrappers to find this JDK, symlink it with
#   sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
# 
# openjdk@17 is keg-only, which means it was not symlinked into /opt/homebrew,
# because this is an alternate version of another formula.
```
```shell
brew install openjdk@17
# ...
# ==> Pouring openjdk@17--17.0.8.arm64_ventura.bottle.tar.gz
# ==> Caveats
# For the system Java wrappers to find this JDK, symlink it with
#   sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
# 
# openjdk@17 is keg-only, which means it was not symlinked into /opt/homebrew,
# because this is an alternate version of another formula.
# 
# If you need to have openjdk@17 first in your PATH, run:
#   fish_add_path /opt/homebrew/opt/openjdk@17/bin
# 
# For compilers to find openjdk@17 you may need to set:
#   set -gx CPPFLAGS "-I/opt/homebrew/opt/openjdk@17/include"
# ==> Summary
# 🍺  /opt/homebrew/Cellar/openjdk@17/17.0.8: 635 files, 305MB
# ==> Running `brew cleanup openjdk@17`...
# Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
# Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

#### Note `JAVA_HOME`
The output of the last command contains the location of `JAVA_HOME` as 
`/opt/homebrew/opt/openjdk@17` (without the `/bin`). Any time you want to use this version of Java,
you don't need to modify path like the instructions above suggest. Instead, just set `JAVA_HOME`.
```shell
# For fish shell
set JAVA_HOME /opt/homebrew/opt/openjdk@17

# For bash shell
export JAVA_HOME=/opt/homebrew/opt/openjdk@17

# Check
echo $JAVA_HOME
# /opt/homebrew/opt/openjdk@17

java -version
# openjdk version "17.0.8" 2023-07-18
# OpenJDK Runtime Environment Homebrew (build 17.0.8+0)
# OpenJDK 64-Bit Server VM Homebrew (build 17.0.8+0, mixed mode, sharing)
```

It's better to not symlink brew-installed Java for system Java wrappers. This will help make 
debugging easier in case your pyspark installation fails to work.

## Install Python
### MacOS (Apple Silicon)
Install Python using [brew](https://brew.sh/).
```shell
brew info python@3.11
# ==> python@3.11: stable 3.11.4 (bottled)
# Interpreted, interactive, object-oriented programming language
# https://www.python.org/
# /opt/homebrew/Cellar/python@3.11/3.11.4_1 (3,395 files, 64.8MB) *
#   Poured from bottle using the formulae.brew.sh API on 2023-07-15 at 13:33:02
# From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/p/python@3.11.rb
# License: Python-2.0
# ==> Dependencies
# Build: pkg-config ✘
# Required: mpdecimal ✔, openssl@3 ✔, sqlite ✔, xz ✔
# ==> Caveats
# Python has been installed as
#   /opt/homebrew/bin/python3
# 
# Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
# `python3`, `python3-config`, `pip3` etc., respectively, have been installed into
#   /opt/homebrew/opt/python@3.11/libexec/bin
# 
# You can install Python packages with
#   pip3 install <package>
# They will install into the site-package directory
#   /opt/homebrew/lib/python3.11/site-packages
# ...
```
```shell
brew install python@3.11 
# Warning: python@3.11 3.11.4_1 is already installed and up-to-date.
# To reinstall 3.11.4_1, run:
#  brew reinstall python@3.11
```

Find the path of brew-installed Python 3.11. If `python3.11` executable is not in your 
`PATH`, edit your path to include `/opt/homebrew/bin`. 
```shell
# It's typically better to prepend /opt/homebrew/bin to PATH
# For fish shell 
set -g -x PATH /opt/homebrew/bin $PATH

# For bash
export PATH="/opt/homebrew/bin:$PATH"

# Check
echo $PATH
# ... /opt/homebrew/bin ... /usr/bin /bin /usr/sbin /sbin ... 

which python3.11
# /opt/homebrew/bin/python3.11
```

## Scala does not need to be explicitly installed
Scala would be provided by the `pyspark` package.

## Install `pyspark`
### Create a virtual environment
Create a virtual environment using your favorite package.
Here, we use [virtualfish](https://github.com/justinmayer/virtualfish).
```shell
vf new pyspark -p python3.11
vf deactivate

# You can reuse the virtual environment `pyspark` anytime  
vf activate pyspark
python --version
# Python 3.11.4 
# ... run your python code here ...
vf deactivate
```

### Install `pyspark` and other dependencies
Use the `requirements.txt` file. 
```shell
vf activate pyspark
pip install --upgrade pip
pip install -r requirements.txt
```

Ensure that you have the correct version of `pyspark`. Typically, `pip`-installing the latest version of 
`pyspark` would match the Maven coordinates we saw in the first step.
```shell
# Still within the virtual environment
pip show pyspark
# Name: pyspark
# Version: 3.4.1
# Summary: Apache Spark Python API
# Home-page: https://github.com/apache/spark/tree/master/python
# Author: Spark Developers
# Author-email: dev@spark.apache.org
# License: http://www.apache.org/licenses/LICENSE-2.0
# Location: /Users/ankur/.virtualenvs/pyspark/lib/python3.11/site-packages
# Requires: py4j
# Required-by:
```

`pyspark` python package comes with Scala jars. You can verify this by searching in the `pyspark` installation location.
```shell
ls /Users/ankur/.virtualenvs/pyspark/lib/python3.11/site-packages/pyspark/jars | grep "spark"
# spark-catalyst_2.12-3.4.1.jar
# spark-core_2.12-3.4.1.jar  <- Note the Scala version! 
# spark-graphx_2.12-3.4.1.jar
# spark-hive-thriftserver_2.12-3.4.1.jar
# spark-hive_2.12-3.4.1.jar
# spark-kubernetes_2.12-3.4.1.jar
# spark-kvstore_2.12-3.4.1.jar
# spark-launcher_2.12-3.4.1.jar
# spark-mesos_2.12-3.4.1.jar
# spark-mllib-local_2.12-3.4.1.jar
# spark-mllib_2.12-3.4.1.jar
# spark-network-common_2.12-3.4.1.jar
# spark-network-shuffle_2.12-3.4.1.jar
# spark-repl_2.12-3.4.1.jar
# spark-sketch_2.12-3.4.1.jar
# spark-sql_2.12-3.4.1.jar
# spark-streaming_2.12-3.4.1.jar
# spark-tags_2.12-3.4.1.jar
# spark-unsafe_2.12-3.4.1.jar
# spark-yarn_2.12-3.4.1.jar
```

## Run pyspark without any extra packages
The basic run does not include any jars needed for additional activities like accessing data over S3.
This is how a successful run should look like.
Note that we set `JAVA_HOME` to `/opt/homebrew/opt/openjdk@17` in `run_basic_pyspark.py`.

```shell
# Still within the virtual environment
python run_basic_pyspark.py
# 23/08/17 22:11:34 WARN Utils: Your hostname, greyshark.local resolves to a loopback address: 127.0.0.1; using 192.168.1.7 instead (on interface en0)
# 23/08/17 22:11:34 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
# Setting default log level to "WARN".
# To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
# 23/08/17 22:11:34 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
# 23/08/17 22:11:34 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
# +---+---+
# |  x|  y|
# +---+---+
# |  0|  0|
# |  1|  1|
# |  2|  2|
# |  3|  3|
# |  4|  4|
# +---+---+
```

If this step fails, please check your versions again. Do not proceed to the next step which will have even more 
perplexing errors.

## Failures
Debugging failures is necessary (not just desirable) skill when using pyspark. Most errors happen because of one of 
these reasons. 
1. Missing dependencies
2. Wrong dependency versions 
3. Multiple versions of the same dependency in the classpath 
4. Wrong Java, Scala, or Python versions
5. Not setting the environment variables (eg: `JAVA_HOME`) before starting a pyspark session

### Try to read parquet from S3
For this demo, let's find publicly available parquet data on S3 from 
[Registry of Open Data on AWS](https://registry.opendata.aws/). After searching for "parquet", let's use 
[Genome Aggregation Database (gnomAD)](https://registry.opendata.aws/gnomad-data-lakehouse-ready/) dataset,
which contains the S3 URI.

You need to have [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed.
On MacOS (Apple Silicon), AWS CLI is best installed via the GUI route (`AWSCLIV2.pkg`).

Let's check the data we want to read using pyspark:
```shell
aws s3 ls --no-sign-request s3://aws-roda-hcls-datalake/gnomad/chrm/
# 2021-09-08 12:22:56     260887 run-DataSink0-1-part-block-0-r-00000-snappy.parquet
# ...
# 2021-09-08 12:22:55     263581 run-DataSink0-1-part-block-0-r-00019-snappy.parquet
```

Now, let's run `fail_s3_spark.py` and see the failure. 
```shell
python fail_s3_spark.py
# 23/08/17 22:47:32 WARN FileStreamSink: Assume no metadata directory. Error while looking for metadata directory in the path: s3a://aws-roda-hcls-datalake/gnomad/chrm/*.parquet.
# java.lang.RuntimeException: java.lang.ClassNotFoundException: Class org.apache.hadoop.fs.s3a.S3AFileSystem not found
# 	at org.apache.hadoop.conf.Configuration.getClass(Configuration.java:2688)
#     ...
# Caused by: java.lang.ClassNotFoundException: Class org.apache.hadoop.fs.s3a.S3AFileSystem not found
```

This error is caused by the [lack](https://stackoverflow.com/questions/58415928/spark-s3-error-java-lang-classnotfoundexception-class-org-apache-hadoop-f) 
of `org.apache.hadoop:hadoop-aws` jar. In order to use additional features like accessing data from S3, we need to 
start the pyspark session with the relevant jars. We don't need to download the jars manually, but we need to specify 
the maven coordinates of the jars in the correct format. Most importantly, we need to find the correct version 
of `org.apache.hadoop:hadoop-aws` jar.

https://central.sonatype.com/artifact/org.apache.spark/spark-core_2.12/3.4.1

https://central.sonatype.com/artifact/org.apache.hadoop/hadoop-aws/3.3.4




### Use pyspark with packages
 We specify these dependencies (jars) in `run_s3_spark.py` itself.

Find the correct Maven coordinates for the jars is extremely important.


