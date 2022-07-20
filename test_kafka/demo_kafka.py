"""

kafka消费范例
"""

import pymysql
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json

ip = "192.168.25.136:9092"
topic = "quickstart-events"
group_id = "test-id"


# kafka的消费
def consumer_kafaka():
    group_id = "group-segment-useractiveUpdate"
    consumer = KafkaConsumer(topic,
                             bootstrap_servers=ip,
                             group_id=group_id,
                             auto_offset_reset='earliest')
    # for msg in consumer:
    #     print(msg.value.decode(encoding="utf-8"))
    while True:
        for dicts in consumer:
            tmp = dicts.value.decode("utf-8")
            print(tmp)
            tmp_data = json.loads(tmp)
            print(type(tmp_data))
            data = list((tmp_data.get("name"), tmp_data.get("gender"), tmp_data.get("age"), tmp_data.get("project")))
            connection = get_mysql_connection()
            write_to_mysql(data, connection)


def get_mysql_connection():
    mysql_host = "192.168.25.136"
    port = 3386
    username = "root"
    password = "Asd@xxxxxx"
    database = "school"
    charset = "utf8"
    connection = pymysql.Connect(
        host = mysql_host,
        user=username,
        password=password,
        database=database,
        charset=charset
    )
    return connection

def write_to_mysql(data, connection):
    sql = "insert into teacher(name, gender, age, project) VALUES(%s, %s,%s, %s)"
    connection.ping(reconnect=True)
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()





if __name__ == '__main__':
    consumer_kafaka()