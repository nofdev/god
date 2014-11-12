#!/usr/bin/env python
__author__ = 'Taio'

import os
import sys
import time
import logging
import ConfigParser

config_file = ConfigParser.RawConfigParser(allow_no_value=True)
config_file.read('/etc/god/god.conf')

logLevel = config_file.get('logging', 'log_level')

logger = logging.getLogger('god')
logging.basicConfig(filename='/var/log/god.log', level=logLevel,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

service_name = config_file.get('service', 'name')
command_line = config_file.get('service', 'command_line')
delay_loop = config_file.get('global', 'delay_loop')
delay_before_retry = config_file.get('global', 'delay_before_retry')

while True:
    time.sleep(int(delay_loop))
    try:
        ret = os.popen('ps -C %s -o pid,cmd' % service_name).readlines()
        if len(ret) < 2:
            print '%s process error, %s seconds after the restart...' % (service_name, delay_before_retry)
            time.sleep(int(delay_before_retry))
            os.system('%s' % command_line)
    except:
        print "Error", sys.exc_info()[1]
