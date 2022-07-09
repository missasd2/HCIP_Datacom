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
    "measurement": 'bl',
    "time": now_time,
    "fields": {

    'bl': "2.1",

        }
    }]
# 写入数据库
client.write_points(w_json)

# if __name__ == '__main__':
#     print(time.localtime())
