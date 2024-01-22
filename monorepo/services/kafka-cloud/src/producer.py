import sys
import os

from confluent_kafka import Producer


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


def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d]\n' %
                            (msg.topic(), msg.partition()))


def test_producer():
    topic = os.environ['CLOUDKARAFKA_TOPIC'].split(",")[0]
    conf = {
        'bootstrap.servers': os.environ['CLOUDKARAFKA_HOSTNAME']+":"+os.environ['CLOUDKARAFKA_PORT'],
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'SASL_SSL',
	    'sasl.mechanisms': 'SCRAM-SHA-512',
        'sasl.username': os.environ['CLOUDKARAFKA_USERNAME'],
        'sasl.password': os.environ['CLOUDKARAFKA_PASSWORD']
    }

    p = Producer(**conf)
    #for line in sys.stdin:
    for line in ['Hola', 'Mundo']:
        try:
            print("Sending message: {0} to topic: {1}".format(line, topic))
            p.produce(topic, line.rstrip(), callback=delivery_callback)
        except BufferError as e:
            sys.stderr.write('Local producer queue is full ({0} messages awaiting delivery): try again\n'.format(len(p)))
        p.poll(0)

    sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
    p.flush()

if __name__ == '__main__':
    test_producer()