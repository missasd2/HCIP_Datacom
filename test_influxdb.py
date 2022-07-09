import time

from influxdb import InfluxDBClient
# 首先连接influxdb
client = InfluxDBClient(host='192.168.25.136', port=8086, username='sw', password='123456' ,ssl=False, verify_ssl=False, database="mydb")
# 创建数据库
# client.create_database('mydb')
# 查询数据库
client.get_list_database()

import datetime;

now_time = time.strftime("%Y%m%d", time.localtime(time.time()))
now_time = "2020/06/21"


w_json = [{
    "measurement": 'temperature',
    "time": now_time,
    "tags": {
        '00': '2023增长率',
        },
    "fields": {

    '01月': "2.1",
    '02月': "2.2",
    '03月': "2.13",
    '04月': "2.4",
    '05月': "2.5",
    '06月': "2.6",
    '07月': "2.7",
    '08月': "2.8",
    '09月': "2.9",
    '10月': "2.112",
    '11月': "2.113",
    '12月': "2.12",
        }
    }]
# 写入数据库
client.write_points(w_json)

# if __name__ == '__main__':
#     print(time.localtime())
