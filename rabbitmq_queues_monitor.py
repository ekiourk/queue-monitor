#!/usr/bin/env python

import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

from backends.rabbitmq import RabbitMqBackend
from queue_monitor.strategy_parser import StrategyParser
from queue_monitor.queue_strategy import QueueStrategy

UNAC_STATE="status:FAIL | details + Cannot access to the rabbitmq engine"


def dict_to_monitis_query_str(data):
    """
    Takes a dictionary and returns a serialised string in the following format
    name:value;name2:value2;name3:value3
    """
    return ";".join([":".join([key, str(val)]) for key, val in data.items()])

while True:

    config = StrategyParser("monitoring_example.yaml")

    queues = []
    try:
        with RabbitMqBackend(config.backend) as backend:
            queues = backend.query('queues')
            #pp.pprint(queues)

    except Exception as e:
        print(UNAC_STATE+' - '+str(e))

    data = {}
    for queue in queues:
        data[queue["name"]] = queue["messages_ready"]

    for queue in config.strategies:
        queue_strategy = QueueStrategy(queue, config.strategies[queue])
        queue_strategy.run_strategies(data[queue])

    print(dict_to_monitis_query_str(data))

    time.sleep(30)


