"""
kafka生产范例
"""
from kafka import KafkaProducer
import json
import random
import time

ip = "192.168.25.136:9092"
topic = "quickstart-events"
group_id = "test-id"


# kafka 的生产
def create_kafaka():
    """
    写入kafka数据，useractive数据，如果用户活跃，useractiveUpdata服务就会消费
    :return:
    """
    name_list = ["大卫", "小明", "流域", "hello", "Jack"]
    gender_list = ["male", "female"]
    project_list = ["生物", "数学", "物理", "语文", "外语"]
    producer = KafkaProducer(bootstrap_servers=ip,
                             value_serializer=lambda m: json.dumps(m).encode(encoding="utf-8"))
    while True:

        data = {
            "name": str(random.choice(name_list)),
            "gender": random.choice(gender_list),
            "age": random.randint(18, 65),
            "project": str(random.choice(project_list)),

        }
        result=producer.send(topic, data)
        time.sleep(5)
        print(data)


if __name__ == '__main__':
    create_kafaka()
    # consumer_kafaka()