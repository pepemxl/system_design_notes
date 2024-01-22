from confluent_kafka import Consumer, KafkaException, KafkaError
import os
import sys
import time



env_var = os.environ

CURRENT_PATH = os.path.abspath(__file__)
SRC_PATH = os.path.dirname(CURRENT_PATH)
SERVICE_PATH = os.path.dirname(SRC_PATH)
SERVICES_PATH = os.path.dirname(SERVICE_PATH)
MONOREPO_PATH = os.path.dirname(SERVICES_PATH)
BASE_PATH = os.path.dirname(MONOREPO_PATH)
LOCAL_DATA_PATH = os.path.join(BASE_PATH, "LOCAL_DATA")
CONFIG_INPUT_PATH = os.path.join(LOCAL_DATA_PATH, "LOCAL_CONFIGS")
full_filename_config = os.path.join(CONFIG_INPUT_PATH, "config.yml")
if os.path.isfile(full_filename_config):
    import yaml
    with open(full_filename_config, 'r') as ptr_file:
        yaml_data = yaml.safe_load(ptr_file)
        config = yaml_data['data']
        os.environ.update(config)



def test_consumer():
    topics = os.environ['CLOUDKARAFKA_TOPIC'].split(",")
    conf = {
        'bootstrap.servers': os.environ['CLOUDKARAFKA_HOSTNAME']+":"+os.environ['CLOUDKARAFKA_PORT'],
        'group.id': os.environ['CLOUDKARAFKA_CONSUMER_GROUP_ID'],
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'SASL_SSL',
	    'sasl.mechanisms': 'SCRAM-SHA-512',
        'sasl.username': os.environ['CLOUDKARAFKA_USERNAME'],
        'sasl.password': os.environ['CLOUDKARAFKA_PASSWORD']
    }

    c = Consumer(**conf)
    c.subscribe(topics)
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                # Error or event
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    # Error
                    raise KafkaException(msg.error())
            else:
                # Proper message
                sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key())))
                print(msg.value())
            time.sleep(2.5)
            print("Waiting update")


    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    # Close down consumer to commit final offsets.
    c.close()


if __name__ == '__main__':
    test_consumer()
