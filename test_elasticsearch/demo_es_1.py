from elasticsearch import Elasticsearch
import json

ip = "192.168.25.136"

# es = Elasticsearch([{'host':'192.168.25.136','port':9200, 'scheme':"http"}], timeout=3600)
es = Elasticsearch(
    [
        'http://192.168.25.136:9200/',

    ],
    verify_certs=True,
)




body = {
    'from': 0,  # 从0开始
    'size': 2  # 取2个数据。类似mysql中的limit 0, 20。 注：size可以在es.search中指定，也可以在此指定，默认是10
}


# data = es.search(index='syslog*', body=body)  # index：选择数据库
data = es.search(index='syslog-security-20220709', body=body)  # index：选择数据库



with open("data.json", "a", encoding="utf8") as res:
    res.write(json.dumps(data))

print(data)

es.close()