"""Kafka consumer.
"""
import ssl
import sys
from kafka import KafkaConsumer

from logga import log, set_log_level

set_log_level(level='DEBUG')

BOOTSTRAP_SERVERS = 'CHANGE_ME'
SASL_PLAIN_USERNAME = 'CHANGE_ME'
SASL_PLAIN_PASSWORD = 'CHANGE_ME'

SASL_MECHANISM = 'PLAIN'
SECURITY_PROTOCOL = 'SASL_SSL'

# Create a new context using system defaults, disable all but TLS1.2
CONTEXT = ssl.create_default_context()
CONTEXT.options &= ssl.OP_NO_TLSv1
CONTEXT.options &= ssl.OP_NO_TLSv1_1

CONSUMER = KafkaConsumer('tester',
                         bootstrap_servers=BOOTSTRAP_SERVERS,
                         sasl_plain_username=SASL_PLAIN_USERNAME,
                         sasl_plain_password=SASL_PLAIN_PASSWORD,
                         security_protocol=SECURITY_PROTOCOL,
                         ssl_context=CONTEXT,
                         sasl_mechanism=SASL_MECHANISM,
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=10000,
                         api_version=(1, 1, 1))
log.info("Consumer init OK")

for message in CONSUMER:
    sys.stdout.buffer.write(message.value)
    print()
