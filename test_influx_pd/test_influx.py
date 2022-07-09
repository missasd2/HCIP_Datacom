from influxdb import InfluxDBClient

client = InfluxDBClient(host="192.168.25.136", port=8086, username="sw", password="123456", ssl=False, verify_ssl=False)

print(client.get_list_database())

client.create_database("consumer")

client.switch_database("consumer")


json_body = [
    {
        "measurement": "consumer_index",
        "tags": {
            "metric": "消费价格指数"
        },
        "fields":{
            "2022年5月": 101.3,
            "2022年6月": 101.1,
            "2022年7月": 101,
            "2022年8月": 100.8,
            "2022年9月": 100.7,
            "2022年10月": 101.5,
            "2022年11月": 102.3,
            "2022年12月": 101.5,
            "2022年1月": 100.9,
            "2022年2月": 100.9,
            "2022年3月": 101.5,
            "2022年4月": 102.1,
            "2022年5月": 102.1,
        },
        "time": "2022-05-01T0:00:00Z"

    }
]




json_body_5 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "5月": 102.3,

        },
        "time": "2022-05-01T0:00:00Z"
    }
]

json_body_6 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "6月": 102.1,

        },
        "time": "2022-06-01T0:00:00Z"
    }
]

json_body_7 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "7月": 102,

        },
        "time": "2022-07-01T0:00:00Z"
    }
]


json_body_8 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "8月": 101.8,

        },
        "time": "2022-08-01T0:00:00Z"
    }
]


json_body_9 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "9月": 101.7,

        },
        "time": "2022-09-01T0:00:00Z"
    }
]

json_body_10 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "10月": 102.5,

        },
        "time": "2022-10-01T0:00:00Z"
    }
]


json_body_11 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "11月": 103.3,

        },
        "time": "2022-11-01T0:00:00Z"
    }
]


json_body_12 = [
    {
        "measurement": "消费价格指数",
        "tags": {
            "year": "2022年"
        },
        "fields":{
            "12月": 102.5,

        },
        "time": "2022-12-07T0:00:00Z"
    }
]



json_body = [
            json_body_5,
            json_body_6,
            json_body_7,
            json_body_8,
            json_body_9,
            json_body_10,
            json_body_11,
            json_body_12,
             ]

for x in json_body:
    client.write_points(x)