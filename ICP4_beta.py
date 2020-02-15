import pdb

import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkFiles


sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

df = sqlContext.read.csv(SparkFiles.get("D:/spring 2020/Knowledge Discovery/ICP 4/data.csv"), header=True, inferSchema= True)
df.printSchema()

df1 = df.select('gender','SeniorCitizen','InternetService')
print(df1.take(10))
print(df1.distinct().count())
##############INTERNET COVERAGE##############################################################################################################################
print("Senior Male Citizens Google Fiber",df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==1) & (df1['InternetService']=='Fiber optic')).count())
print("Young Male Citizens Google Fiber",df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==0) & (df1['InternetService']=='Fiber optic')).count())
print("Senior female Citizens Google Fiber",df1.filter((df1['gender'] == 'Female') & (df1['SeniorCitizen']==1) & (df1['InternetService']=='Fiber optic')).count())
print("Young Female Citizens Google Fiber",df1.filter((df1['gender'] == 'Female') & (df1['SeniorCitizen']==0) & (df1['InternetService']=='Fiber optic')).count(),"\n")


print("Senior Male Citizens DSL",df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==1) & (df1['InternetService']=='DSL')).count())
print("Young Male Citizens DSL",df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==0) & (df1['InternetService']=='DSL')).count())
print("Senior female Citizens DSL",df1.filter((df1['gender'] == 'Female') & (df1['SeniorCitizen']==1) & (df1['InternetService']=='DSL')).count())
print("Young Female Citizens DSL",df1.filter((df1['gender'] == 'Female') & (df1['SeniorCitizen']==0) & (df1['InternetService']=='DSL')).count(),"\n")


print("Senior Male Citizens No Internet",df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==1) & (df1['InternetService']=='No')).count())
print("Young Male Citizens No Internet",df1.filter((df1['gender'] == 'Male') & (df1['SeniorCitizen']==0) & (df1['InternetService']=='No')).count())
print("Senior female Citizens No Internet",df1.filter((df1['gender'] == 'Female') & (df1['SeniorCitizen']==1) & (df1['InternetService']=='No')).count())
print("Young Female Citizens No Internet",df1.filter((df1['gender'] == 'Female') & (df1['SeniorCitizen']==0) & (df1['InternetService']=='No')).count(),"\n")

df.write.format("csv").save("./Google_Fiber.csv")

df1 = df.select('SeniorCitizen','InternetService','StreamingTV','StreamingMovies')
print(df1.take(10))
print(df1.distinct().count())
##############STREAMING COVERAGE##############################################################################################################################
print("Senior Citizens With Services using Google Fiber",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='Fiber optic') & (df1['StreamingTV']=="Yes") & (df1['StreamingMovies']=='Yes')).count())
print("Young Citizens With Services using Google Fiber",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='Fiber optic') & (df1['StreamingTV']=="Yes") & (df1['StreamingMovies']=='Yes')).count(),"\n")

print("Senior Citizens With Services using DSL",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='DSL') & (df1['StreamingTV']=="Yes") & (df1['StreamingMovies']=='Yes')).count())
print("Young Citizens With Services using DSL",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='DSL') & (df1['StreamingTV']=="Yes") & (df1['StreamingMovies']=='Yes')).count(),"\n")

print("Senior Citizens With Services With out Internet",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='No') & (df1['StreamingTV']=="Yes") & (df1['StreamingMovies']=='Yes')).count())
print("Young Citizens With Services With out Internet",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='No') & (df1['StreamingTV']=="Yes") & (df1['StreamingMovies']=='Yes')).count(),"\n")

df.write.format("csv").save("./Streaming.csv")

df1 = df.select('SeniorCitizen','InternetService','OnlineSecurity','OnlineBackup', 'DeviceProtection','TechSupport')
print(df1.take(10))
print(df1.distinct().count())
##############SECURITY CONCERN##############################################################################################################################
print("Senior Citizens Security Concern using Google Fiber",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='Fiber optic') & (df1['OnlineSecurity']=="Yes") & (df1['OnlineBackup']=='Yes') & (df1['DeviceProtection']=='Yes') & (df1['TechSupport']=='Yes')).count())
print("Young Citizens Security Concern using Google Fiber",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='Fiber optic') & (df1['OnlineSecurity']=="Yes") & (df1['OnlineBackup']=='Yes') & (df1['DeviceProtection']=='Yes') & (df1['TechSupport']=='Yes')).count(),"\n")

print("Senior Citizens Security Concern using DSL",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='DSL') & (df1['OnlineSecurity']=="Yes") & (df1['OnlineBackup']=='Yes') & (df1['DeviceProtection']=='Yes') & (df1['TechSupport']=='Yes')).count())
print("Young Citizens Security Concern using DSL",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='DSL') & (df1['OnlineSecurity']=="Yes") & (df1['OnlineBackup']=='Yes') & (df1['DeviceProtection']=='Yes') & (df1['TechSupport']=='Yes')).count(),"\n")

print("Senior Citizens Security Concern With out Internet",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='No') & (df1['OnlineSecurity']=="Yes") & (df1['OnlineBackup']=='Yes') & (df1['DeviceProtection']=='Yes') & (df1['TechSupport']=='Yes')).count())
print("Young Citizens Security Concern With out Internet",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='No') & (df1['OnlineSecurity']=="Yes") & (df1['OnlineBackup']=='Yes') & (df1['DeviceProtection']=='Yes') & (df1['TechSupport']=='Yes')).count(),"\n")

df.write.format("csv").save("./Security.csv")

df1 = df.select('SeniorCitizen','InternetService','PaperlessBilling','PaymentMethod')
print(df1.take(10))
print(df1.distinct().count())
##############GO GREEN##############################################################################################################################
print("Senior Citizens Go Green using Google Fiber",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='Fiber optic') & (df1['PaperlessBilling']=="Yes") & ((df1['PaymentMethod']=="Bank transfer (automatic)") | (df1['PaymentMethod']=="Electronic check") |(df1['PaymentMethod']== "Credit card (automatic)"))).count())
print("Young Citizens Go Greenn using Google Fiber",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='Fiber optic') & (df1['PaperlessBilling']=="Yes") & ((df1['PaymentMethod']=="Bank transfer (automatic)") | (df1['PaymentMethod']=="Electronic check") |(df1['PaymentMethod']== "Credit card (automatic)"))).count(),"\n")

print("Senior Citizens Security Concern using DSL",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='DSL') & (df1['PaperlessBilling']=="Yes")& ((df1['PaymentMethod']=="Bank transfer (automatic)") | (df1['PaymentMethod']=="Electronic check") |(df1['PaymentMethod']== "Credit card (automatic)"))).count())
print("Young Citizens Security Concern using DSL",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='DSL') & (df1['PaperlessBilling']=="Yes") & ((df1['PaymentMethod']=="Bank transfer (automatic)") | (df1['PaymentMethod']=="Electronic check") |(df1['PaymentMethod']== "Credit card (automatic)"))).count(),"\n")

print("Senior Citizens Security Concern With out Internet",df1.filter( (df1['SeniorCitizen']==1) & (df1['InternetService']=='No') & (df1['PaperlessBilling']=="Yes") & ((df1['PaymentMethod']=="Bank transfer (automatic)") | (df1['PaymentMethod']=="Electronic check") |(df1['PaymentMethod']== "Credit card (automatic)"))).count())
print("Young Citizens Security Concern With out Internet",df1.filter( (df1['SeniorCitizen']==0) & (df1['InternetService']=='No') & (df1['PaperlessBilling']=="Yes") & ((df1['PaymentMethod']=="Bank transfer (automatic)") | (df1['PaymentMethod']=="Electronic check") |(df1['PaymentMethod']== "Credit card (automatic)"))).count(),"\n")

df.write.format("csv").save("./EcoFriendly.csv")


pdb.set_trace()

print(df1.take(3))