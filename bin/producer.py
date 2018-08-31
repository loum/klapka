"""Kafka producer.
"""
import ssl
from kafka import KafkaProducer
from kafka.errors import KafkaError
from logga import log, set_log_level

set_log_level('INFO')

BOOTSTRAP_SERVERS = 'CHANGE_ME'
SASL_PLAIN_USERNAME = 'CHANGE_ME'
SASL_PLAIN_PASSWORD = 'CHANGE_ME'

SASL_MECHANISM = 'PLAIN'
SECURITY_PROTOCOL = 'SASL_SSL'

# Create a new context using system defaults, disable all but TLS1.2
CONTEXT = ssl.create_default_context()
CONTEXT.options &= ssl.OP_NO_TLSv1
CONTEXT.options &= ssl.OP_NO_TLSv1_1

PRODUCER = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         sasl_plain_username=SASL_PLAIN_USERNAME,
                         sasl_plain_password=SASL_PLAIN_PASSWORD,
                         security_protocol=SECURITY_PROTOCOL,
                         ssl_context=CONTEXT,
                         sasl_mechanism=SASL_MECHANISM,
                         api_version=(1, 1, 1))

# Asynchronous by default
FUTURE = PRODUCER.send('tester', b'test message')

# Block for 'synchronous' sends
try:
    RECORD_METADATA = FUTURE.get(timeout=10)
except KafkaError as err:
    log.exception(err)

# Successful result returns assigned partition and offset
log.info('Record metadata topic: %s', RECORD_METADATA.topic)
log.info('Record metadata partition: %s', RECORD_METADATA.partition)
log.info('Record metadata offset: %s', RECORD_METADATA.offset)
