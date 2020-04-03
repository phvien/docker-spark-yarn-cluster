from pyspark.sql import Row
from pyspark.ml.linalg import Vectors
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.classification import LinearSVC
from os import environ

environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
environ["PYSPARK_DRIVER_PYTHON"] = "/usr/bin/python3"

sc = SparkContext(master="yarn", appName="Innoria-ML")
spark = SparkSession(sc).builder.getOrCreate()

df = sc.parallelize([
        Row(label=1.0, features=Vectors.dense(1.0, 1.0, 1.0)),
        Row(label=0.0, features=Vectors.dense(1.0, 2.0, 3.0))]).toDF()

df.show()

# svm = LinearSVC(maxIter=5, regParam=0.01)

# model = svm.fit(df)

# print(model.coefficients)

