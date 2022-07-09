import pandas as pd


csv = pd.read_csv("./月度数据.csv", encoding="utf-8", sep=",", index_col="指标")
print(type(csv))
print(csv)
print("=============")
print(csv.loc["居民消费价格指数(上年同月=100)"])
print("======")
print(csv.iloc[1, :2])

for x in csv.iloc[1, :2]:
    print(x)