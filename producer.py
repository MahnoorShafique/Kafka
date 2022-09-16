from kafka import KafkaProducer
import json
import time
from kafka_app_demo.data import get_reg_user



""" this for sending data randomly to any partition in a topic"""

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
#  when you decode all the text are based on utf-8 encoding thats why using utf -8 encode method

producer=KafkaProducer(bootstrap_servers=['10.100.102.110:6667'],
                       value_serializer=json_serializer)

if __name__ =='__main__':
    while 1==1:
        reg_user=get_reg_user()
        print(reg_user)
        #  to send msgs to producer i will use send method that receive the topic name(mahnoor) as first argument and data as second argument
        producer.send("mahnoor",reg_user)
        time.sleep(4)


"""this for sending data to specific partition of our choice"""


def json_serializer(data):
    return json.dumps(data).encode('utf-8')
#  when you decode all the text are based on utf-8 encoding thats why using utf -8 encode method
def get_partition(key,all_partition,available):
    # this will always return 0 means data will send to first partition only
    return 0

producer=KafkaProducer(bootstrap_servers=['10.100.102.110:6667'],
                       value_serializer=json_serializer,
                       partitioner=get_partition)

if __name__ =='__main__':
    while 1==1:
        reg_user=get_reg_user()
        print(reg_user)
        #  to send msgs to producer i will use send method that receive the topic name(mahnoor) as first argument and data as second argument
        producer.send("mahnoor1",reg_user)
        time.sleep(4)


