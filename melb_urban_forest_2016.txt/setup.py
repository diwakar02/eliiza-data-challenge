import os
import sys

# NOTE: please change the path to current setup in your system
#windows
if sys.platform.startswith('win'):
    #location where all the programs will be stored this project location
    os.chdir(r"C:\Users\Diwakar Sharma\Pictures\PySparkV2")
    
    #path of spark installation
    os.environ['SPARK_HOME'] = "C:\spark"

#do same  if there are other platforms  
os.curdir

# Create variable for root path
SPARK_HOME = os.environ['SPARK_HOME']

# Add following paths
sys.path.insert(0,os.path.join(SPARK_HOME, "python"))
sys.path.insert(0,os.path.join(SPARK_HOME, "python", "lib"))
sys.path.insert(0,os.path.join(SPARK_HOME, "python", "lib", "pyspark.zip"))
sys.path.insert(0,os.path.join(SPARK_HOME, "python", "lib", "py4j-0.10.7-src.zip"))

# Initialize spark session and spark context
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import Row
from functools import reduce
from past.builtins import xrange
from polygon_utils import *

# create Spark Session
spSession = SparkSession \
    .builder \
    .master("local[2]") \
    .appName("Pyspark Tuts") \
    .config("spark.executor.memory", "8g") \
    .config("spark.cores.max", "2") \
    .config("spark.sql.warehouse.dir", "file:///C:/temp/spark-warehouse") \
    .getOrCreate()

# get the spark context from Spark Session
sparkContext = spSession.sparkContext
# -*- coding: utf-8 -*-