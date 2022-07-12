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
    'size': 10  # 取10个数据。类似mysql中的limit 0, 20。 注：size可以在es.search中指定，也可以在此指定，默认是10
}

# 使用DSL语句查询

query = {
    "query": {
        "term":{
            'message': "hello"
        }
    }
}

# insert = {
#
#
#         "type": "syslog",
#         "message": "<13>JJul  9 20:46:00.00 centos2 root: hello world 4",
#         "syslog_program": "root",
#         "@version": "1",
#         "received_at": "2022-07-09T20:46:00.000Z",
#         "syslog_hostname": "centos2",
#         "received_from": "192.168.25.138",
#         "syslog_message": "hello world 5",
#         "syslog_timestamp": "Jul  9 20:46:00.000",
#         "@timestamp": "2022-07-09T20:46:00.000Z",
#         "host": "192.168.25.138"
# }

insert = {


        "type": "syslog",
        "message": "<13>JJul  9 20:46:00.00 centos2 root: hello world 4",
        "syslog_program": "root",

        "received_at": "2022-07-09T20:46:00.000Z",
        "syslog_hostname": "centos2",
        "received_from": "192.168.25.138",
        "syslog_message": "hello world 7",
        "syslog_timestamp": "Jul  9 20:46:00.000",

        "host": "192.168.25.138"
}


data = es.search(index='syslog-security-20220709', body=body)  # index：选择数据库

# 带过滤条件的查询
data1 = es.search(index='syslog-security-20220709', body=query)  # index：选择数据库

print(type(data)) # dict


# 插入数据；不指定id，自动生成
index1 = es.create(index='syslog-security-20220709', body=insert, id=1)
print(index1)



# 将dict对象进行序列化，并写入json文件
with open("data.json", "w", encoding="utf8") as res:
    res.write(json.dumps(data))
    res.write(json.dumps(data1))

print(data)
print("=====")
print(data1)

es.close()