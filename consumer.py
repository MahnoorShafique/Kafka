from kafka import KafkaConsumer

import json

if __name__ =="__main__":
    """ auto_offset_reset tells whether to consumer from start or end .earliest means first msg that was pubished on topic"""
    consumer=KafkaConsumer('mahnoor1',
                           bootstrap_servers='10.100.102.110:6667',
                           auto_offset_reset='earliest',
                           group_id='consumer-group-b'
                           )
    print("staring consumer")
    for msg in consumer:
        print("data from topic is={}".format(json.loads(msg.value)))

